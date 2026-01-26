from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E13_Attribute_Assignment import AttributeAssignment

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E3_Condition_State import ConditionState

class ConditionAssessment(AttributeAssignment):
    """Condition Assessment <http://www.cidoc-crm.org/cidoc-crm/E14_Condition_Assessment>.

    This class describes the act of assessing the state of preservation of an object during a particular period.
    The condition assessment may be carried out by inspection, measurement, or through historical research. This class is used to document circumstances of the respective assessment that is relevant to interpret its quality at a later stage, or to continue research on related documents.
    """
    concerned: list[PhysicalThing] = []
    identified: list[ConditionState] = []
