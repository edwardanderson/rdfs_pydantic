from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E77_Persistent_Item import PersistentItem

if TYPE_CHECKING:
    from .E54_Dimension import Dimension
    from .E55_Type import Type
    from .E7_Activity import Activity

class Thing(PersistentItem):
    """Thing <http://www.cidoc-crm.org/cidoc-crm/E70_Thing>.

    This general class comprises discrete, identifiable, instances of E77 Persistent Item that are documented as single units, that either consist of matter or depend on being carried by matter and are characterized by relative stability.
    They may be intellectual products or physical things. They may, for instance, have a solid physical form, an electronic encoding, or they may be a logical concept or structure.
    """
    dimension: list[Dimension] = []
    features_are_also_found_on: list[Thing] = []
    general_use: list[Type] = []
    shows_features_of: list[Thing] = []
    used_for: list[Activity] = []
