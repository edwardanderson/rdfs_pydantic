from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..crm.E7_Activity import Activity

if TYPE_CHECKING:
    from ..crm.E1_CRM_Entity import CRMEntity

class Transfer(Activity):
    """Transfer <https://linked.art/ns/terms/Transfer>.

    Abstract transferral of something between entities.
    """
    transferred: list[CRMEntity] = []
    transferred_from: list[CRMEntity] = []
    transferred_to: list[CRMEntity] = []
