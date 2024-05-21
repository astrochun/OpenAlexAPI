"""
Copyright 2022 Dennis Priskorn
"""

from typing import Optional, List, Dict

from openalexapi.basetype import OpenAlexBaseType
from openalexapi.authorship import Authorship
from openalexapi.biblio import Biblio
from openalexapi.concept import Concept
from openalexapi.enums import WorkType
from openalexapi.ids import Ids
from openalexapi.mesh import Mesh
from openalexapi.openaccess import OpenAccess
from openalexapi.venue import Venue
from openalexapi.year import Year


# Currently missing corresponding_author_ids, corresponding_institution_ids, apc_payment, best_oa_location, grants
class Work(OpenAlexBaseType):
    doi: Optional[str]
    title: Optional[str]
    display_name: Optional[str]
    publication_year: Optional[int]
    publication_date: Optional[str]
    ids: Ids
    language: Optional[str]
    primary_location: Optional[Venue]
    type: Optional[WorkType]
    type_crossref: Optional[WorkType]
    open_access: Optional[OpenAccess]
    authorships: Optional[List[Authorship]]
    cited_by_count: Optional[int]
    biblio: Optional[Biblio]
    is_retracted: Optional[bool]
    is_paratext: Optional[bool]
    concepts: Optional[List[Concept]]
    mesh: Optional[List[Mesh]] = []
    location_count: Optional[int]
    locations: Optional[List[Venue]]
    referenced_works: Optional[List[str]]  # this is urls like https://openalex.org/W123
    related_works: Optional[List[str]]  # this is urls like https://openalex.org/W123
    ngrams_url: Optional[str]
    abstract_inverted_index: Optional[Dict[str, List[int]]]
    cited_by_api_url: Optional[str]
    counts_by_year: Optional[List[Year]]
    updated_date: Optional[str]
    created_date: Optional[str]
