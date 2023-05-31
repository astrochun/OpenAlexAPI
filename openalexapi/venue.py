"""
Copyright 2022 Dennis Priskorn
"""
from typing import Optional, List

from pydantic import BaseModel
from openalexapi.basetype import OpenAlexBaseType


class Source(OpenAlexBaseType):
    display_name: Optional[str]
    issn_l: Optional[str]  # What is this?
    issn: Optional[List[str]]
    host_organization: Optional[str]
    host_organization_name: Optional[str]
    host_organization_lineage: Optional[List[str]]
    host_organization_lineage_names: Optional[List[str]]
    type: Optional[str]


# This was host_venue but change to source
class Venue(BaseModel):
    is_oa: Optional[bool]
    landing_page_url: Optional[str]  # Was url in the original metadata schema
    pdf_url: Optional[str]  # This was later added
    source: Optional[Source]
    publisher: Optional[str]
    license: Optional[str]
    version: Optional[str]
