"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional
from typing_extensions import Annotated

from pydantic import BaseModel, Field


class Year(BaseModel):
    year: Optional[Annotated[int, Field(strict=True, ge=0)]]
    cited_by_count: int
