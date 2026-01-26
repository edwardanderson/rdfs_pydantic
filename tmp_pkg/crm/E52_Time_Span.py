from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E1_CRM_Entity import CRMEntity

if TYPE_CHECKING:
    from .E2_Temporal_Entity import TemporalEntity
    from .E54_Dimension import Dimension
    from .E92_Spacetime_Volume import SpacetimeVolume
    from .E93_Presence import Presence

class TimeSpan(CRMEntity):
    """Time-Span <http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span>.

    This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end, and a duration.
    Instances of E52 Time-Span have no semantic connotations about phenomena happening within the temporal extent they represent. They do not convey any meaning other than a positioning on the “time-line” of chronology. The actual extent of an instance of E52 Time-Span can be approximated by properties of E52 Time-Span giving inner and outer bounds in the form of dates (instances of E61 Time Primitive). Comparing knowledge about time-spans is fundamental for chronological reasoning.
    Some instances of E52 Time-Span may be defined as the actual, in principle observable, temporal extent of instances of E2 Temporal Entity via the property P4 has time-span (is time-span of): E52 Time-Span. They constitute phenomenal time-spans as defined in CRMgeo (Doerr &amp; Hiebel 2013). Since our knowledge of history is imperfect and physical phenomena are fuzzy in nature, the extent of phenomenal time-spans can only be described in approximation. An extreme case of approximation, might, for example, define an instance of E52 Time-Span having unknown beginning, end and duration. It may, nevertheless, be associated with other descriptions by which people can infer knowledge about it, such as in relative chronologies.
    Some instances of E52 may be defined precisely as representing a declaration of a temporal extent, as, for instance, done in a business contract. They constitute declarative time-spans as defined in CRMgeo (Doerr &amp; Hiebel 2013) and can be described via the property E61 Time Primitive P170 defines time (time is defined by): E52 Time-Span.
    When used as a common E52 Time-Span for two events, it will nevertheless describe them as being simultaneous, even if nothing else is known.
    """
    P160i_is_temporal_projection_of: list[SpacetimeVolume] = []
    P164i_temporally_specifies: list[Presence] = []
    P86_falls_within: list[TimeSpan] = []
    P86i_contains: list[TimeSpan] = []
    at_some_time_within: str | None = None
    begin_of_the_begin: str | None = None
    begin_of_the_end: str | None = None
    beginning_is_qualified_by: str | None = None
    duration: list[Dimension] = []
    end_is_qualified_by: str | None = None
    end_of_the_begin: str | None = None
    end_of_the_end: str | None = None
    ongoing_throughout: str | None = None
    time_is_defined_by: str | None = None
    timespan_of: list[TemporalEntity] = []
