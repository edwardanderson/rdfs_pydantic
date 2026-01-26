from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..crm.E7_Activity import Activity

if TYPE_CHECKING:
    from ..crm.E1_CRM_Entity import CRMEntity
    from .Set import Set

class Addition(Activity):
    """Addition <https://linked.art/ns/terms/Addition>.

    The addition of some entity to a Set.
    """
    added_member: list[CRMEntity] = []
    added_to: list[Set] = []
