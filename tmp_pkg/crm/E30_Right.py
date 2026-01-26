from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E89_Propositional_Object import PropositionalObject

if TYPE_CHECKING:
    from ..la.RightAcquisition import RightAcquisition
    from .E39_Actor import Actor
    from .E72_Legal_Object import LegalObject

class Right(PropositionalObject):
    """Right <http://www.cidoc-crm.org/cidoc-crm/E30_Right>.

    This class comprises legal privileges concerning material and immaterial things or their derivatives.
    These include reproduction and property rights.
    """
    applies_to: list[LegalObject] = []
    established_by: list[RightAcquisition] = []
    invalidated_by: list[RightAcquisition] = []
    possessed_by: list[Actor] = []
