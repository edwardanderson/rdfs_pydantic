from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E1_CRM_Entity import CRMEntity

if TYPE_CHECKING:
    from .E52_Time_Span import TimeSpan

class TemporalEntity(CRMEntity):
    """Temporal Entity <http://www.cidoc-crm.org/cidoc-crm/E2_Temporal_Entity>.

    This class comprises all phenomena, such as the instances of E4 Periods and E5 Events, which happen over a limited extent in time. This extent in time must be contiguous, i.e., without gaps. In case the defining kinds of phenomena for an instance of E2 Temporal Entity cease to happen, and occur later again at another time, we regard that the former instance of E2 Temporal Entity has ended and a new instance has come into existence. In more intuitive terms, the same event cannot happen twice.
    In some contexts, such phenomena are also called perdurants. This class is disjoint from E77 Persistent Item and is an abstract class that typically has no direct instances. E2 Temporal Entity is specialized into E4 Period, which applies to a particular geographic area (defined with a greater or lesser degree of precision), and E3 Condition State, which applies to instances of E18 Physical Thing.
    """
    P175i_starts_after_or_with_the_start_of: list[TemporalEntity] = []
    after: list[TemporalEntity] = []
    before: list[TemporalEntity] = []
    ends_after_or_with_the_start_of: list[TemporalEntity] = []
    ends_after_the_end_of: list[TemporalEntity] = []
    ends_after_the_start_of: list[TemporalEntity] = []
    ends_before_or_with_the_end_of: list[TemporalEntity] = []
    ends_before_or_with_the_start_of: list[TemporalEntity] = []
    ends_before_the_end_of: list[TemporalEntity] = []
    ends_with_or_after_the_end_of: list[TemporalEntity] = []
    starts_after_or_with_the_end_of: list[TemporalEntity] = []
    starts_after_the_start_of: list[TemporalEntity] = []
    starts_before_or_with_the_end_of: list[TemporalEntity] = []
    starts_before_or_with_the_start_of: list[TemporalEntity] = []
    starts_before_the_end_of: list[TemporalEntity] = []
    starts_before_the_start_of: list[TemporalEntity] = []
    timespan: list[TimeSpan] = []
