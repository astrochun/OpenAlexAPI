"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from pydantic import BaseModel


class Ids(BaseModel):
    doi: Optional[str] = None
    pmid: Optional[str] = None
    mag: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def doi_id(self):
        if self.doi is not None:
            return self.doi.replace("https://doi.org/", "")
        return None

    @property
    def doi_url(self):
        return self.doi

    @property
    def pmid_id(self):
        if self.pmid is not None:
            return self.pmid.replace("https://pubmed.ncbi.nlm.nih.gov/", "")
        return None

    @property
    def pmid_url(self):
        return self.pmid
