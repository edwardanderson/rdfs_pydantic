from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E64_End_of_Existence import EndOfExistence

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing

class Destruction(EndOfExistence):
    """Destruction <http://www.cidoc-crm.org/cidoc-crm/E6_Destruction>.

    This class comprises events that destroy one or more instances of E18 Physical Thing, such that they lose their identity as the subjects of documentation.
    Some destruction events are intentional, while others are independent of human activity. Intentional destruction can be documented by classifying the event as both an instance of E6 Destruction and of E7 Activity.
    The decision to document an object as destroyed, transformed, or modified is context-sensitive:.
    1. If the matter remaining from the destruction is not documented, the event is modelled solely as an instance of E6 Destruction.
    2. An event should also be documented using E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the original. In this case, the new items have separate identities. Matter is preserved, but identity is not.
    3. When the initial identity of the changed instance of E18 Physical Thing is preserved, the event should be documented as an instance of E11 Modification.
    """
    destroyed: list[PhysicalThing] = []
