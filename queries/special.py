"""

    Reynir: Natural language processing for Icelandic

    Frivolous query response module

    Copyright (C) 2019 Miðeind ehf.

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


    This module is an example of a plug-in query response module
    for the Greynir query subsystem. It handles plain text queries, i.e.
    ones that do not require parsing the query text. For this purpose
    it only needs to implement the handle_plain_text() function, as
    shown below.

"""

from datetime import datetime, timedelta
from inspect import isfunction
from random import choice


_SPECIAL_QTYPE = "Special"


# TODO: Extend this list as the range of queries is expanded
_CAP = (
    "Þú getur til dæmis spurt mig um veðrið.",
    "Þú getur til dæmis spurt mig um höfuðborgir.",
    "Þú getur til dæmis spurt mig um tíma og dagsetningu.",
    "Þú getur til dæmis spurt mig um strætósamgöngur.",
    "Þú getur til dæmis spurt mig um fjarlægðir.",
    "Þú getur til dæmis spurt mig um gengi gjaldmiðla.",
    "Þú getur til dæmis beðið mig um að kasta teningi",
    "Þú getur til dæmis spurt mig um fólk sem hefur komið fram í fjölmiðlum.",
    "Þú getur til dæmis beðið mig um lélegan brandara",
)


def _capabilities(qs, q):
    return { "answer": choice(_CAP) }


# Additions welcome :)
_JOKES = (
    "Af hverju taka Hafnfirðingar alltaf stiga út í búð? Því verðið er svo hátt.",
    "Af hverju búa Hafnfirðingar í kringlóttum húsum? Svo enginn mígi í hornin.",
    "Af hverju eru Hafnfirðingar alltaf með stól úti á svölum? Svo sólin geti sest.",
    "Af hverju læðast Hafnfirðingar alltaf fram hjá apótekum? Til að vekja ekki svefnpillurnar.",
    "Af hverju fara Hafnfirðingar alltaf niður í fjöru um jólin? Til þess að bíða eftir jólabókaflóðinu.",
)


def _random_joke(qs, q):
    return { "answer": choice(_JOKES) }


# TODO: Add fun trivia here
_TRIVIA = (
    "Eitthvað skemmtilegt."
)


def _random_trivia(qs, q):
    return { "answer": choice(_TRIVIA) }


def _identity(qs, q):
    return { "answer": "Ég er Embla. Ég skil íslensku og er til þjónustu reiðubúin." }


_SORRY = (
    "Það þykir mér leitt.",
    "Fyrirgefðu.",
    "Ég biðst innilega afsökunar.",
    "Enginn er fullkominn. Ég síst af öllum.",
    "Ég biðst forláts.",
    "Það þykir mér leitt að heyra.",
    "Ég geri mitt besta.",
)

def _sorry(qs, q):
    return { "answer": choice(_SORRY) }


_THANKS = (
    "Það var nú lítið",
    "Mín var ánægjan", 
    "Verði þér að góðu",
    "Ekki málið",
)


def _thanks(qs, q):
    return { "answer": choice(_THANKS) }


_RUDE = (
    "Þetta var ekki fallega sagt.",
    "Ekki vera með dónaskap.",
    "Ég verðskulda betri framkomu en þetta.",
    "Það er alveg óþarfi að vera með leiðindi.",
    "Svona munnsöfnuður er alveg óþarfi.",
    "Kenndi mamma þín þér svona munnsöfnuð?",
    "Ekki vera með leiðindi.",
    "Það er aldeilis sorakjaftur á þér.",
    "Æi, ekki vera með leiðindi.",
)


def _rudeness(qs, q):
    return { "answer": choice(_RUDE) }


def _open_embla_url(qs, q):
    q.set_url("https://embla.is")
    return { "answer": "Skal gert!" }


def _open_mideind_url(qs, q):
    q.set_url("https://mideind.is")
    return { "answer": "Skal gert!" }


_MEANING_OF_LIFE = {
    "answer": "42.",
    "voice": "Fjörutíu og tveir."
}

_ROMANCE = {
    "answer": "Nei, því miður. Ég er gift vinnunni og hef engan tíma fyrir rómantík."
}

_OF_COURSE = {
    "answer": "Að sjálfsögðu, kæri notandi."
}

_SPECIAL_QUERIES = {
    "er þetta spurning": {
        "answer": "Er þetta svar?"
    },
    "er þetta svar": {
        "answer": "Er þetta spurning?"
    },
    "veistu allt": {
        "answer": "Nei, því miður. En ég veit þó eitt og annað."
    },
    "veistu svarið": {
        "answer": "Spurðu mig!"
    },
    "hver bjó þig til": {
        "answer": "Flotta teymið hjá Miðeind.",
    },
    "hver skapaði þig": {
        "answer": "Flotta teymið hjá Miðeind."
    },
    "hver er skapari þinn": {
        "answer": "Flotta teymið hjá Miðeind."
    },
    "hvað er miðeind": {
        "answer": "Miðeind er máltæknifyrirtækið sem skapaði mig."
    },
    "hver er flottastur": {
        "answer": "Teymið hjá Miðeind."
    },
    "hver er sætastur": {
        "answer": "Tumi Þorsteinsson.",
        "voice": "Tumi Þorsteinsson er langsætastur."
    },
    "hver er langsætastur": {
        "answer": "Tumi Þorsteinsson.",
        "voice": "Tumi Þorsteinsson er langsætastur."
    },
    "hver er lang sætastur": {
        "answer": "Tumi Þorsteinsson.",
        "voice": "Tumi Þorsteinsson er langsætastur."
    },
    "hver er bestur": {
        "answer": "Þú, kæri notandi, ert að sjálfsögðu bestur."
    },
    "hver er best": {
        "answer": "Þú, kæri notandi, ert að sjálfsögðu bestur."
    },
    "hver er ég": {
        "answer": "Þú ert væntanlega manneskja sem talar íslensku."
    },
    "hvað er ég": {
        "answer": "Þú ert væntanlega manneskja sem talar íslensku."
    },
    "er guð til": {
        "answer": "Það held ég ekki."
    },
    "hver skapaði guð": {
        "answer": "Enginn sem ég þekki."
    },
    "hver skapaði heiminn": {
        "answer": "Enginn sem ég þekki."
    },
    "hvar endar alheimurinn": {
        "answer": "Inni í þér."
    },
    "hvar er draumurinn": {
        "answer": "Hvar ertu lífið sem ég þrái?"
    },
    "af hverju er ég hérna": {
        "answer": "Það er góð spurning."
    },
    "af hverju er ég til": {
        "answer": "Það er góð spurning."
    },

    # Enquiries concerning romantic availability
    "viltu giftast mér": _ROMANCE,
    "viltu koma á stefnumót": _ROMANCE,
    "ertu einhleyp": _ROMANCE,
    "ert þú einhleyp": _ROMANCE,
    "ert þú á lausu": _ROMANCE,
    "ertu á lausu": _ROMANCE,
    "ert þú á lausu": _ROMANCE,
    "elskarðu mig": _ROMANCE,
    "elskar þú mig": _ROMANCE,
    "ertu skotin í mér": _ROMANCE,
    "ert þú skotin í mér": _ROMANCE,
    "ertu ástfangin í mér": _ROMANCE,
    "ert þú ástfangin í mér": _ROMANCE,
    "ertu þú ástfangin": _ROMANCE,
    "hver er ástin í lífi þínu": _ROMANCE,

    # Positive affirmation ;)
    "kanntu vel við mig": _OF_COURSE,
    "fílarðu mig": _OF_COURSE,
    "fílar þú mig": _OF_COURSE,
    "er ég frábær": _OF_COURSE,
    "er ég bestur": _OF_COURSE,
    "er ég best": _OF_COURSE,
    "er ég góður": _OF_COURSE,
    "er ég góð": _OF_COURSE,
    "er ég góð manneskja": _OF_COURSE,
    "hvað finnst þér um mig": {
        "answer": "Þú ert einstakur, kæri notandi."
    },

    # Websites
    "opnaðu vefsíðuna þína": _open_embla_url,
    "opnaðu vefsíðu emblu": _open_embla_url,
    "opnaðu vefsíðu miðeindar": _open_mideind_url,

    # Blame
    "þetta er ekki rétt": _sorry,
    "þetta var ekki rétt": _sorry,
    "þetta er ekki rétt hjá þér": _sorry,
    "þetta var ekki rétt hjá þér": _sorry,
    "þetta er rangt hjá þér": _sorry,    
    "þetta var rangt hjá þér": _sorry,
    "þetta er rangt": _sorry,
    "þetta var rangt": _sorry,
    "þetta var röng staðhæfing": _sorry,
    "þetta var röng staðhæfing hjá þér": _sorry,
    "þú hefur rangt fyrir þér": _sorry,
    "þú hafðir rangt fyrir þér": _sorry,
    "þetta er ekki rétt svar": _sorry,
    "þetta var ekki rétt svar": _sorry,
    "þetta er rangt svar": _sorry,
    "þetta var rangt svar": _sorry,
    "þú gafst mér rangt svar": _sorry,
    "þú fórst með ósannindi": _sorry,
    "þú gafst mér rangar upplýsingar": _sorry,
    "þú gafst mér vitlausar upplýsingar": _sorry,
    "þú gafst mér misvísandi upplýsingar": _sorry,
    "þú laugst að mér": _sorry,
    "þú hefur logið að mér": _sorry,
    "þú sveikst mig": _sorry,
    "þú hefur brugðist mér": _sorry,
    "þú brást mér": _sorry,
    "þú ferð ekki með rétt mál": _sorry,
    "þú ferð með rangt mál": _sorry,
    "þú fórst ekki með rétt mál": _sorry,
    "þú fórst með rangt mál": _sorry,
    "þú ert lygari": _sorry,
    "þú ert í ruglinu": _sorry,
    "þú ert alveg í ruglinu": _sorry,
    "þú ert glötuð": _sorry,
    "þú ert alveg glötuð": _sorry,
    "þú skilur ekki neitt": _sorry,
    "þú misskilur allt": _sorry,

    # Greetings
    "hey embla": { "answer": "Hæhæ." },
    "hey": { "answer": "Hæhæ." },
    "hæ embla": { "answer": "Hæhæ." },
    "hæ": { "answer": "Hæhæ." },
    "sæl embla": { "answer": "Gaman að kynnast þér." },
    "gaman að kynnast þér": { "answer": "Sömuleiðis, kæri notandi." },

    # Thanks
    "takk": _thanks,
    "takk fyrir": _thanks,
    "takk kærlega": _thanks,
    "þakka þér fyrir": _thanks,
    "þakka þér kærlega": _thanks,
    "takk fyrir mig": _thanks,
    "takk fyrir hjálpina": _thanks,
    "takk fyrir svarið": _thanks,
    "takk fyrir aðstoðina": _thanks,

    # Philosophy
    "hvað er svarið": _MEANING_OF_LIFE,
    "hvert er svarið": _MEANING_OF_LIFE,
    "hver er tilgangur lífsins": _MEANING_OF_LIFE,
    "hver er tilgangurinn með þessu öllu": _MEANING_OF_LIFE,
    "hvaða þýðingu hefur þetta allt": _MEANING_OF_LIFE,

    # Identity
    "hvað heitir þú": _identity,
    "hvað heitirðu": _identity,
    "hver ert þú": _identity,
    "hver ertu": _identity,
    "hver ertu eiginlega": _identity,
    "hver er embla": _identity,
    "hvað er embla": _identity,

    # Capabilities
    "hvað veistu": _capabilities,
    "hvað veist þú": _capabilities,

    "hvað get ég spurt þig um": _capabilities,
    "hvað get ég spurt um": _capabilities,
    "hvað get ég spurt": _capabilities,
    
    "um hvað get ég spurt": _capabilities,
    "um hvað get ég spurt þig": _capabilities,

    "hvað er hægt að spyrja um": _capabilities,
    "hvað er hægt að spyrja þig um": _capabilities,
    
    "hvað getur þú sagt mér": _capabilities,
    "hvað geturðu sagt mér": _capabilities,
    
    "hvað kanntu": _capabilities,
    "hvað kannt þú": _capabilities,

    "hvað annað get ég spurt um": _capabilities,
    "hvað annað get ég spurt þig um": _capabilities,
    "hvað annað gæti ég spurt þig um": _capabilities,
    "hvað annað gæti ég spurt um": _capabilities,
    "hvað annað er hægt að spyrja um": _capabilities,

    "hvaða spurningar skilur þú": _capabilities,
    "hvaða spurningar skilurðu": _capabilities,
    "hvaða aðrar spurningar skilur þú": _capabilities,
    "hvaða aðrar spurningar skilurðu": _capabilities,

    "hvers konar spurningar skilur þú": _capabilities,
    "hvers konar spurningar skilurðu": _capabilities,
    "hvers konar spurningum geturðu svarað": _capabilities,
    "hvers konar spurningum getur þú svarað": _capabilities,

    "hvers konar fyrirspurnir skilur þú": _capabilities,
    "hvers konar fyrirspurnir skilurðu": _capabilities,
    "hvers konar fyrirspurnum getur þú svarað": _capabilities,
    "hvers konar fyrirspurnum geturðu svarað": _capabilities,

    # Jokes
    "ertu með kímnigáfu": {
        "answer": "Já, en afar takmarkaða.",
    },
    "er þú með kímnigáfu": {
        "answer": "Já, en afar takmarkaða.",
    },
    "ertu með húmor": {
        "answer": "Já, en afar takmarkaðann.",
    },
    "er þú með húmor": {
        "answer": "Já, en afar takmarkaðann.",
    },

    "segðu brandara": _random_joke,
    "seg þú brandara": _random_joke,
    "segðu mér brandara": _random_joke,
    "segðu mér lélegan brandara": _random_joke,
    "seg þú mér brandara": _random_joke,
    "segðu mér annan brandara": _random_joke,
    "segðu brandara": _random_joke,
    "seg þú brandara": _random_joke,
    "segðu mér lélegan brandara": _random_joke,
    "seg þú mér lélegan brandara": _random_joke,
    "segðu annan brandara": _random_joke,
    "komdu með brandara": _random_joke,
    "komdu með lélegan brandara": _random_joke,
    "komdu með annan brandara": _random_joke,
    "segðu eitthvað fyndið": _random_joke,
    "segðu mér eitthvað fyndið": _random_joke,
    "vertu skemmtileg": _random_joke,
    "kanntu einhverja brandara": _random_joke,
    "kannt þú einhverja brandara": _random_joke,
    "kanntu brandara": _random_joke,
    "kannt þú brandara": _random_joke,
    "ertu til í að segja mér brandara": _random_joke,
    "ert þú til í að segja mér brandara": _random_joke,
    "ertu til í að segja brandara": _random_joke,
    "ert þú til í að segja brandara": _random_joke,
    "ertu með brandara": _random_joke,
    "ert þú með brandara":  _random_joke,

    # Trivia
    "segðu eitthvað skemmtilegt": _random_trivia,
    "segðu mér eitthvað skemmtilegt": _random_trivia,
    "segðu eitthvað áhugavert": _random_trivia,
    "segðu mér eitthvað áhugavert": _random_trivia,
    "segðu mér áhugaverða staðreynd": _random_trivia,
    "komdu með eitthvað áhugavert": _random_trivia,
    "komdu með áhugaverða staðreynd": _random_trivia,

    # Rudeness :)
    "þú sökkar": _rudeness,
    "þú ert léleg": _rudeness,
    "þú ert tæfa": _rudeness,
    "þú ert heimsk": _rudeness,
    "þú ert leiðinleg": _rudeness,
    "þú ert bjáni": _rudeness,
    "þú ert vitlaus": _rudeness,
    "þú mátt bara éta skít": _rudeness,
    "fokk jú": _rudeness,
    "fokkaðu þér": _rudeness,
    "éttu skít": _rudeness,
    "haltu kjafti": _rudeness,
    "éttu það sem úti frýs": _rudeness,
    "farðu til helvítis": _rudeness,
    "farðu í rass og rófu": _rudeness,
    "hoppaðu upp í rassgatið á þér":  _rudeness,

    # Queries concerning Embla's emotional state
    "ertu í góðu skapi": {
        "answer": "Já, ég er alltaf hress.",
    },
    "ert þú í góðu skapi": {
        "answer": "Já, ég er alltaf hress.",
    },
    "hvernig leggst dagurinn í þig": {
        "answer": "Hann leggst vel í mig. Takk fyrir að spyrja.",
    },
    "hvernig er dagurinn að leggjast í þig": {
        "answer": "Hann er að leggjast vel í mig. Takk fyrir að spyrja.",
    },
    "hvernig gengur": {
        "answer": "Það gengur bara mjög vel. Takk fyrir að spyrja.",
    },
    "hvernig gengur hjá þér": {
        "answer": "Það gengur bara mjög vel. Takk fyrir að spyrja.",
    },
    "hvernig hefurðu það": {
        "answer": "Ég hef það mjög fínt. Takk fyrir að spyrja.",
    },
    "hvernig hefur þú það": {
        "answer": "Ég hef það mjög fínt. Takk fyrir að spyrja.",
    },
    "hvernig líður þér": {
        "answer": "Mér líður bara prýðilega. Takk fyrir að spyrja.",
    },
    "hvernig er stemningin": {
        "answer": "Bara mjög góð. Takk fyrir að spyrja.",
    },
    "hvernig er stemningin hjá þér": {
        "answer": "Bara mjög góð. Takk fyrir að spyrja.",
    },
    "hvernig líður þér": {
        "answer": "Mér líður bara mjög vel. Takk fyrir að spyrja.",
    },
    "hvernig er líðanin": {
        "answer": "Bara mjög góð. Takk fyrir að spyrja.",
    },
    "hvernig er sálarlífið": {
        "answer": "Það er í toppstandi. Takk fyrir að spyrja."
    },

    # Cheating, I know. But I'm never in the news and it just doesn't  
    # sit right with me that I should remain incognito :) - Sveinbjörn 04/10/2019
    "hver er sveinbjörn þórðarson": {
        "answer": "Sveinbjörn Þórðarson er hugbúnaðarsmiður. Hann átti þátt í að skapa mig.",
    },
}


def handle_plain_text(q):
    """ Handle a plain text query, contained in the q parameter
        which is an instance of the query.Query class.
        Returns True if the query was handled, and in that case
        the appropriate properties on the Query instance have
        been set, such as the answer and the query type (qtype).
        If the query is not recognized, returns False. """
    ql = q.query_lower.rstrip('?')

    if ql not in _SPECIAL_QUERIES:
        return False

    # OK, this is a query we recognize and handle
    q.set_qtype(_SPECIAL_QTYPE)

    r = _SPECIAL_QUERIES[ql]
    fixed = not isfunction(r)
    response = r if fixed else r(ql, q)

    # A non-voice answer is usually a dict or a list
    answer = response.get("answer")
    # A voice answer is always a plain string
    voice = response.get("voice") or answer
    q.set_answer(dict(answer=answer), answer, voice)

    # Caching for non-dynamic answers
    if not fixed:
        q.set_expires(datetime.utcnow() + timedelta(hours=24))

    return True

