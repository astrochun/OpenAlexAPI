"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional
from typing_extensions import Annotated

from pydantic import StringConstraints

from openalexapi.basetype import OpenAlexBaseType


class Institution(OpenAlexBaseType):
    id: Optional[str] = None
    display_name: Optional[str] = None
    ror: Optional[str] = None
    country_code: Optional[
        Annotated[str, StringConstraints(max_length=2, min_length=2)]
    ] = None
    type: Optional[str] = None
