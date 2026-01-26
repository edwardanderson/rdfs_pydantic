from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Addition import Addition
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E39_Actor import Actor
    from .E74_Group import Group

class Joining(Addition, Activity):
    """Joining <http://www.cidoc-crm.org/cidoc-crm/E85_Joining>.

    This class comprises the activities that result in an instance of E39 Actor becoming a member of an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.
    Typical scenarios include becoming a member of a social organisation, becoming an employee of a company, marriage, the adoption of a child by a family, and the inauguration of somebody into an official position.
    """
    joined: list[Actor] = []
    joined_with: list[Group] = []
