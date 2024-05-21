"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional
from typing_extensions import Annotated

from pydantic import StringConstraints

from openalexapi.basetype import OpenAlexBaseType


class Institution(OpenAlexBaseType):
    id: Optional[str]
    display_name: Optional[str]
    ror: Optional[str]
    country_code: Optional[Annotated[str, StringConstraints(max_length=2, min_length=2)]]
    type: Optional[str]
