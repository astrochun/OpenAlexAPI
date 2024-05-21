"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional, List

from pydantic import BaseModel

from openalexapi.author import Author
from openalexapi.institution import Institution


class Authorship(BaseModel):
    author_position: str
    author: Optional[Author]
    institutions: Optional[List[Institution]]
    is_corresponding: Optional[bool]
    raw_affiliation_string: Optional[str]
    raw_affiliation_strings: Optional[List[str]]
