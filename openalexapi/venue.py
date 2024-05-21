"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional, List

from pydantic import BaseModel
from openalexapi.basetype import OpenAlexBaseType


class Source(OpenAlexBaseType):
    display_name: Optional[str] = None
    issn_l: Optional[str] = None  # What is this?
    issn: Optional[List[str]] = None
    host_organization: Optional[str] = None
    host_organization_name: Optional[str] = None
    host_organization_lineage: Optional[List[str]] = None
    host_organization_lineage_names: Optional[List[str]] = None
    type: Optional[str] = None


# This was host_venue but change to source
class Venue(BaseModel):
    is_oa: Optional[bool] = None
    landing_page_url: Optional[str] = None  # Was url in the original metadata schema
    pdf_url: Optional[str] = None  # This was later added
    source: Optional[Source] = None
    publisher: Optional[str] = None
    license: Optional[str] = None
    version: Optional[str] = None
