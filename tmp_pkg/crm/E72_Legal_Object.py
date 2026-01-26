from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E70_Thing import Thing

if TYPE_CHECKING:
    from .E30_Right import Right
    from .E39_Actor import Actor

class LegalObject(Thing):
    """Legal Object <http://www.cidoc-crm.org/cidoc-crm/E72_Legal_Object>.

    This class comprises those material or immaterial items to which instances of E30 Right, such as the right of ownership or use, can be applied.
    This is generally true for all instances of E18 Physical Thing. In the case of instances of E28 Conceptual Object, however, the identity of an instance of E28 Conceptual Object or the method of its use may be too ambiguous to reliably establish instances of E30 Right, as in the case of taxa and inspirations. Ownership of corporations is currently regarded as out of scope of the CIDOC CRM.
    """
    right_held_by: list[Actor] = []
    subject_to: list[Right] = []
