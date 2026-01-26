from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E31_Document import Document

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity

class AuthorityDocument(Document):
    """Authority Document <http://www.cidoc-crm.org/cidoc-crm/E32_Authority_Document>.

    This class comprises encyclopaedia, thesauri, authority lists and other documents that define terminology or conceptual systems for consistent use.
    """
    lists: list[CRMEntity] = []
