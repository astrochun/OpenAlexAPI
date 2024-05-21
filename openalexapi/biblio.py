"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from pydantic import BaseModel


class Biblio(BaseModel):
    volume: Optional[str] = None
    issue: Optional[str] = None
    first_page: Optional[str] = None
    last_page: Optional[str] = None
