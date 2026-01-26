from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..crm.E7_Activity import Activity

if TYPE_CHECKING:
    from ..crm.E1_CRM_Entity import CRMEntity
    from .Set import Set

class Removal(Activity):
    """Removal <https://linked.art/ns/terms/Removal>.

    The removal of some entity from a Set.
    """
    removed_from: list[Set] = []
    removed_member: list[CRMEntity] = []
