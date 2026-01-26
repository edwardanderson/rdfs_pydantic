from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E5_Event import Event

if TYPE_CHECKING:
    from .E77_Persistent_Item import PersistentItem

class BeginningOfExistence(Event):
    """Beginning of Existence <http://www.cidoc-crm.org/cidoc-crm/E63_Beginning_of_Existence>.

    This class comprises events that bring into existence any instance of E77 Persistent Item.
    It may be used for temporal reasoning about things (intellectual products, physical items, groups of people, living beings) beginning to exist; it serves as a hook for both a terminus post quem and a terminus ante quem.
    """
    brought_into_existence: list[PersistentItem] = []
