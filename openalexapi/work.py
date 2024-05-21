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
    doi: Optional[str] = None
    title: Optional[str] = None
    display_name: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[str] = None
    ids: Ids
    language: Optional[str] = None
    primary_location: Optional[Venue] = None
    type: Optional[WorkType] = None
    type_crossref: Optional[WorkType] = None
    open_access: Optional[OpenAccess] = None
    authorships: Optional[List[Authorship]] = None
    cited_by_count: Optional[int] = None
    biblio: Optional[Biblio] = None
    is_retracted: Optional[bool] = None
    is_paratext: Optional[bool] = None
    concepts: Optional[List[Concept]] = None
    mesh: Optional[List[Mesh]] = []
    location_count: Optional[int] = None
    locations: Optional[List[Venue]] = None
    referenced_works: Optional[List[str]] = None  # this is urls like https://openalex.org/W123
    related_works: Optional[List[str]] = None  # this is urls like https://openalex.org/W123
    ngrams_url: Optional[str] = None
    abstract_inverted_index: Optional[Dict[str, List[int]]] = None
    cited_by_api_url: Optional[str] = None
    counts_by_year: Optional[List[Year]] = None
    updated_date: Optional[str] = None
    created_date: Optional[str] = None
