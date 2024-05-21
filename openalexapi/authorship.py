"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional, List

from pydantic import BaseModel

from openalexapi.author import Author
from openalexapi.institution import Institution


class Authorship(BaseModel):
    author_position: str
    author: Optional[Author] = None
    institutions: Optional[List[Institution]] = None
    is_corresponding: Optional[bool] = None
    raw_affiliation_string: Optional[str] = None
    raw_affiliation_strings: Optional[List[str]] = None
