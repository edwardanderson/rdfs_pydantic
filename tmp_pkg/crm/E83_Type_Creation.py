from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E65_Creation import Creation

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E55_Type import Type

class TypeCreation(Creation):
    """Type Creation <http://www.cidoc-crm.org/cidoc-crm/E83_Type_Creation>.

    This class comprises activities formally defining new types of items.
    It is typically a rigorous scholarly or scientific process that ensures a type is exhaustively described and appropriately named. In some cases, particularly in archaeology and the life sciences, E83 Type Creation requires the identification of an exemplary specimen and the publication of the type definition in an appropriate scholarly forum. The activity modelled as an instance of E83 Type Creation is central to research in the life sciences, where a type would be referred to as a “taxon,” the type description as a “protologue,” and the exemplary specimens as “original element” or “holotype”.
    """
    based_on: list[CRMEntity] = []
    created_type: list[Type] = []
