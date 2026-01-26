from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E73_Information_Object import InformationObject

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing

class VisualItem(InformationObject):
    """Visual Item <http://www.cidoc-crm.org/cidoc-crm/E36_Visual_Item>.

    This class comprises the intellectual or conceptual aspects of recognisable marks and images.
    This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment of a visual item, but the underlying prototype. For example, a mark such as the ICOM logo is generally considered to be the same logo when used on any number of publications. The size, orientation, and colour may change, but the logo remains uniquely identifiable. The same is true of images that are reproduced many times. This means that visual items are independent of their physical support.
    The E36 Visual Item class provides a means of identifying and linking together instances of E24 Physical Human-Made Thing that carry the same visual symbols, marks, or images, etc. The property P62 depicts (is depicted by) between E24 Physical Human-Made Thing and the depicted subjects (E1 CRM Entity) can be regarded as a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65 shows visual item (is shown by), E36 Visual Item, P138 represents (has representation) to E1 CRM Entity, which in addition captures the optical features of the depiction.
    """
    digitally_shown_by: list[DigitalObject] = []
    represents: list[CRMEntity] = []
    shown_by: list[PhysicalHumanMadeThing] = []
