from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E73_Information_Object import InformationObject

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity

class Document(InformationObject):
    """Document <http://www.cidoc-crm.org/cidoc-crm/E31_Document>.

    This class comprises identifiable immaterial items that make propositions about reality.
    These propositions may be expressed in text, graphics, images, audiograms, videograms, or by other similar means. Documentation databases are regarded as instances of E31 Document. This class should not be confused with the concept “document” in Information Technology, which is compatible with E73 Information Object.
    """
    documents: list[CRMEntity] = []
