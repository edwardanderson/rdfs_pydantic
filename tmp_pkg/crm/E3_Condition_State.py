from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E2_Temporal_Entity import TemporalEntity

if TYPE_CHECKING:
    from .E14_Condition_Assessment import ConditionAssessment
    from .E18_Physical_Thing import PhysicalThing

class ConditionState(TemporalEntity):
    """Condition State <http://www.cidoc-crm.org/cidoc-crm/E3_Condition_State>.

    This class comprises the states of objects characterised by a certain condition over a time-span.
    An instance of this class describes the prevailing physical condition of any material object or feature during a specific instance of E52 Time-Span. In general, the time-span for which a certain condition can be asserted may be shorter than the real time-span, for which this condition held.
    The nature of that condition can be described using P2 has type. For example, the instance of E3 Condition State “condition of the SS Great Britain between 22-nd September 1846 and 27-th August 1847” can be characterized as an instance “wrecked” of E55 Type.
    """
    condition_identified_by: list[ConditionAssessment] = []
    condition_of: list[PhysicalThing] = []
    sub_state: list[ConditionState] = []
    sub_state_of: list[ConditionState] = []
