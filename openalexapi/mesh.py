"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional
from typing_extensions import Annotated

from pydantic import BaseModel, StringConstraints


class Mesh(BaseModel):
    """This models the mesh object at OpenAlex.
    Unfortunately it does not contain the year when the term
    was added to MESH nor if it is still a valid MESH term"""

    descriptor_ui: Optional[
        Annotated[str, StringConstraints(max_length=10, min_length=7)]
    ]
    is_major_topic: bool
    descriptor_name: str
    qualifier_ui: Optional[str]
    qualifier_name: Optional[str]
