from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E70_Thing import Thing

if TYPE_CHECKING:
    from .E35_Title import Title
    from .E55_Type import Type
    from .E7_Activity import Activity

class HumanMadeThing(Thing):
    """Human-Made Thing <http://www.cidoc-crm.org/cidoc-crm/E71_Human-Made_Thing>.

    This class comprises discrete, identifiable human-made items that are documented as single units.
    These items are either intellectual products or human-made physical things, and are characterized by relative stability. They may, for instance, have a solid physical form, an electronic encoding, or they may be logical concepts or structures.
    """
    intended_for: list[Type] = []
    made_for: list[Activity] = []
    title: list[Title] = []
