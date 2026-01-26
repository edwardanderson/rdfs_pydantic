from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E5_Event import Event

if TYPE_CHECKING:
    from .E77_Persistent_Item import PersistentItem

class EndOfExistence(Event):
    """End of Existence <http://www.cidoc-crm.org/cidoc-crm/E64_End_of_Existence>.

    This class comprises events that end the existence of any instance of E77 Persistent Item.
    It may be used for temporal reasoning about things (physical items, groups of people, living beings) ceasing to exist; it serves as a hook both a terminus post quem and a terminus ante quem. In cases where substance from an instance of E77 Persistent Item continues to exist in a new form, the process would be documented as instances of E81 Transformation.
    """
    took_out_of_existence: list[PersistentItem] = []
