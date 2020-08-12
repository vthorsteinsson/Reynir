"""

    Greynir: Natural language processing for Icelandic

    Places query response module

    Copyright (C) 2020 Miðeind ehf.

       This program is free software: you can redistribute it and/or modify
       it under the terms of the GNU General Public License as published by
       the Free Software Foundation, either version 3 of the License, or
       (at your option) any later version.
       This program is distributed in the hope that it will be useful,
       but WITHOUT ANY WARRANTY; without even the implied warranty of
       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
       GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.


    This module handles queries related to places (shops, businesses, etc.)
    such as opening hours, location, distance, etc. Uses Google's Places API.

"""

# TODO: "Hvert er heimilisfangið á Forréttabarnum?"
# TODO: "Á hvaða götu er Slippbarinn?"
# TODO: "Hvenær lokar X? Hvenær opnar X? Hvenær"

import logging
from datetime import datetime, timedelta

from queries import gen_answer, query_places_api, query_place_details, icequote


_PLACES_QTYPE = "Places"


# Indicate that this module wants to handle parse trees for queries,
# as opposed to simple literal text strings
HANDLE_TREE = True

# The context-free grammar for the queries recognized by this plug-in module
GRAMMAR = """

Query →
    QPlacesQuery '?'?

QPlacesQuery →
    QPlacesOpeningHours

QPlacesOpeningHours →
    "hvað" "er" "opið" "lengi" QPlacesPrepAndSubject
    | "hvað" "er" "lengi" "opið" QPlacesPrepAndSubject
    | "hverjir" "eru" "opnunartímar" QPlacesPrepAndSubject
    | "hvaða" "opnunartímar" "eru" QPlacesPrepAndSubject
    | "er" "opið" QPlacesPrepAndSubject
    | "hversu" "lengi" "er" "opið" QPlacesPrepAndSubject
    | "hve" "lengi" "er" "opið" QPlacesPrepAndSubject
    | "klukkan" "hvað" "opnar" QPlacesPrepAndSubject
    | "klukkan" "hvað" "opnar" QPlacesSubjectNf
    | "hvenær" "lokar" QPlacesPrepAndSubject
    | "hvenær" "lokar" QPlacesSubjectNf
    | "hvenær" "opnar" QPlacesPrepAndSubject
    | "hvenær" "opnar" QPlacesSubjectNf
    | "klukkan" "hvað" "lokar" QPlacesPrepAndSubject
    | "klukkan" "hvað" "lokar" QPlacesSubjectNf
    | "hversu" "langt" "er" "í" "lokun" QPlacesPrepAndSubject
    | "er" "lokað" QPlacesPrepAndSubject

QPlacesPrepAndSubject →
    QPlacesPreposition QPlacesSubjectÞgf

QPlacesSubjectÞgf →
    Nl_þgf

QPlacesSubjectNf →
    Nl_nf

QPlacesPreposition →
    "á" | "í"

$score(+35) QPlacesQuery

"""


_PLACENAME_MAP = {}


def _fix_placename(pn):
    return _PLACENAME_MAP.get(pn, pn)


def QPlacesQuery(node, params, result):
    result["qtype"] = _PLACES_QTYPE


def QPlacesOpeningHours(node, params, result):
    result["qkey"] = "OpeningHours"


def QPlacesSubjectNf(node, params, result):
    result["subject_nom"] = result._nominative


QPlacesSubjectÞgf = QPlacesSubjectNf


_PLACES_API_ERRMSG = "Ekki tókst að fletta upp viðkomandi stað"


def answ_openhours(placename, loc):
    # Look up placename in places API
    res = query_places_api(placename, userloc=loc)

    if "candidates" not in res or not res["candidates"] or res["status"] != "OK":
        return gen_answer(_PLACES_API_ERRMSG)

    # Use top result
    place = res["candidates"][0]
    place_id = place["place_id"]

    # Look up place ID in Place Details API to get more information
    res = query_place_details(place_id, fields="opening_hours")
    if not res:
        return gen_answer(_PLACES_API_ERRMSG)

    now = datetime.utcnow()
    wday = now.weekday()

    try:
        # Get time period for current weekday
        periods = res["result"]["opening_hours"]["periods"]
        p = periods[wday]
        opens = p["open"]["time"]
        closes = p["close"]["time"]

        # Format correctly
        openstr = opens[:2] + ":" + opens[2:]
        closestr = closes[:2] + ":" + opens[2:]
        p_desc = "{0} - {1}".format(openstr, closestr)
        p_voice = p_desc.replace("-", "til")
    except:
        logging.warning("Exception generating answer for opening hours: {0}".format(e))
        return gen_answer(_PLACES_API_ERRMSG)

    # Generate answer
    answer = p_desc
    voice = "Í dag er opið frá {0}".format(p_voice)
    response = dict(answer=answer)

    return response, answer, voice


def sentence(state, result):
    """ Called when sentence processing is complete """
    q = state["query"]
    if "qtype" in result and "subject_nom" in result:
        # Successfully matched a query type
        subj = result["subject_nom"]
        q.set_qtype(result.qtype)
        q.set_key(subj)

        try:
            res = answ_openhours(subj, q.location)
            if res:
                q.set_answer(*res)
            else:
                errmsg = "Ekki tókst að fletta upp opnunartímum fyrir {0}".format(
                    icequote(subj)
                )
                q.set_answer(gen_answer(errmsg))
        except Exception as e:
            logging.warning("Exception answering places query: {0}".format(e))
            q.set_error("E_EXCEPTION: {0}".format(e))
            return
    else:
        q.set_error("E_QUERY_NOT_UNDERSTOOD")
