"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from pydantic import ConstrainedStr

from openalexapi.basetype import OpenAlexBaseType


class CountryCode(ConstrainedStr):
    max_length = 2
    min_length = 2


class Institution(OpenAlexBaseType):
    id: Optional[str]
    display_name: Optional[str]
    ror: Optional[str]
    country_code: Optional[CountryCode]
    type: Optional[str]
