"""
Copyright 2022 Dennis Priskorn
"""
from typing import Optional, Type

from pydantic import constr

from openalexapi.basetype import OpenAlexBaseType


class Institution(OpenAlexBaseType):
    id: Optional[str]
    display_name: Optional[str]
    ror: Optional[str]
    country_code: Optional[Type[str]] = constr(max_length=2, min_length=2)
    type: Optional[str]
