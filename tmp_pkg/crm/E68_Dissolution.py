from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E64_End_of_Existence import EndOfExistence

if TYPE_CHECKING:
    from .E74_Group import Group

class Dissolution(EndOfExistence):
    """Dissolution <http://www.cidoc-crm.org/cidoc-crm/E68_Dissolution>.

    This class comprises the events that result in the formal or informal termination of an instance of E74 Group.
    If the dissolution was deliberate, the Dissolution event should also be instantiated as an instance of E7 Activity.
    """
    dissolved: list[Group] = []
