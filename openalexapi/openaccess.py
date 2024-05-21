"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional

from pydantic import BaseModel


class OpenAccess(BaseModel):
    is_oa: bool
    oa_status: Optional[str] = None
    oa_url: Optional[str] = None
    any_repository_has_fulltext: Optional[bool] = None
