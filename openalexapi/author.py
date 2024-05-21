"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from openalexapi.basetype import OpenAlexBaseType


class Author(OpenAlexBaseType):
    display_name: Optional[str] = None
    orcid: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def orcid_url(self):
        return self.orcid

    @property
    def orcid_id(self):
        return self.orcid.replace("https://orcid.org/", "")
