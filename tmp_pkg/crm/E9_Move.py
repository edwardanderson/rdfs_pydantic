from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Transfer import Transfer
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E19_Physical_Object import PhysicalObject
    from .E53_Place import Place

class Move(Transfer, Activity):
    """Move <http://www.cidoc-crm.org/cidoc-crm/E9_Move>.

    This class comprises changes of the physical location of the instances of E19 Physical Object.
    Note, that the class E9 Move inherits the property P7 took place at (witnessed): E53 Place. This property should be used to describe the trajectory or a larger area within which a move takes place, whereas the properties P26 moved to (was destination of), P27 moved from (was origin of) describe the start and end points only. Moves may also be documented to consist of other moves (via P9 consists of (forms part of)), in order to describe intermediate stages on a trajectory. In that case, start and end points of the partial moves should match appropriately between each other and with the overall event.
    """
    moved: list[PhysicalObject] = []
    moved_from: list[Place] = []
    moved_to: list[Place] = []
