"""
Copyright 2022 Dennis Priskorn
"""
from typing import Optional

from pydantic import BaseModel, ConstrainedInt


class ConstrainedYear(ConstrainedInt):
    ge = 0


class Year(BaseModel):
    year: Optional[ConstrainedYear]
    cited_by_count: int
