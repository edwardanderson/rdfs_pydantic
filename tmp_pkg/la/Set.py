from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..crm.E72_Legal_Object import LegalObject
from ..crm.E89_Propositional_Object import PropositionalObject

if TYPE_CHECKING:
    from ..crm.E18_Physical_Thing import PhysicalThing
    from ..crm.E1_CRM_Entity import CRMEntity
    from .Addition import Addition
    from .Removal import Removal

class Set(PropositionalObject, LegalObject):
    """Set <https://linked.art/ns/terms/Set>."""
    added_to_by: list[Addition] = []
    has_member: list[CRMEntity] = []
    members_contained_by: list[PhysicalThing] = []
    members_exemplified_by: list[CRMEntity] = []
    removed_from_by: list[Removal] = []
