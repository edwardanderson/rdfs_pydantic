from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Removal import Removal
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E39_Actor import Actor
    from .E74_Group import Group

class Leaving(Removal, Activity):
    """Leaving <http://www.cidoc-crm.org/cidoc-crm/E86_Leaving>.

    This class comprises the activities that result in an instance of E39 Actor to be disassociated from an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.
    Typical scenarios include the termination of membership in a social organisation, ending the employment at a company, divorce, and the end of tenure of somebody in an official position.
    """
    separated: list[Actor] = []
    separated_from: list[Group] = []
