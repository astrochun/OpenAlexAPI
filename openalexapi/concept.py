"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from openalexapi.basetype import OpenAlexBaseType


class Concept(OpenAlexBaseType):
    wikidata: Optional[str] = None
    display_name: Optional[str] = None
    level: Optional[int] = None
    score: Optional[float] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def wikidata_id(self):
        return self.wikidata.replace("https://www.wikidata.org/wiki/", "")

    @property
    def wikidata_wiki_url(self):
        return self.wikidata
