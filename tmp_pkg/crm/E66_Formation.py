from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E63_Beginning_of_Existence import BeginningOfExistence
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E74_Group import Group

class Formation(BeginningOfExistence, Activity):
    """Formation <http://www.cidoc-crm.org/cidoc-crm/E66_Formation>.

    This class comprises events that result in the formation of a formal or informal E74 Group of people, such as a club, society, association, corporation, or nation.
    E66 Formation does not include the arbitrary aggregation of people who do not act as a collective.
    The formation of an instance of E74 Group does not require that the group is populated with members at the time of formation. In order to express the joining of members at the time of formation, the respective activity should be simultaneously an instance of both E66 Formation and E85 Joining.
    """
    formed: list[Group] = []
    formed_from: list[Group] = []
