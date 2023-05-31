"""
Copyright 2022 Dennis Priskorn
"""
from typing import Type

from pydantic import BaseModel, conint


class Year(BaseModel):
    year: Type[int] = conint(le=2023, ge=0)
    cited_by_count: int
