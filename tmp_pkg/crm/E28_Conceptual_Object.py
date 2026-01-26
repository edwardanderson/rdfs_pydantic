from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E71_Human_Made_Thing import HumanMadeThing

if TYPE_CHECKING:
    from .E65_Creation import Creation

class ConceptualObject(HumanMadeThing):
    """Conceptual Object <http://www.cidoc-crm.org/cidoc-crm/E28_Conceptual_Object>.

    This class comprises non-material products of our minds and other human produced data that have become objects of a discourse about their identity, circumstances of creation, or historical implication. The production of such information might have been supported by the use of technical devices such as cameras or computers.
    Characteristically, instances of this class are created, invented or thought by someone, and then may be documented or communicated between persons. Instances of E28 Conceptual Object have the ability to exist on more than one particular carrier at the same time, such as paper, electronic signals, marks, audio media, paintings, photos, human memories, etc.
    They cannot be destroyed. They exist as long as they can be found on at least one carrier or in at least one human memory. Their existence ends when the last carrier and the last memory are lost.
    """
    created_by: list[Creation] = []
