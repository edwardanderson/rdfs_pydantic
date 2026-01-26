from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E92_Spacetime_Volume import SpacetimeVolume

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E52_Time_Span import TimeSpan
    from .E53_Place import Place
    from .E92_Spacetime_Volume import SpacetimeVolume

class Presence(SpacetimeVolume):
    """Presence <http://www.cidoc-crm.org/cidoc-crm/E93_Presence>.

    This class comprises instances of E92 Spacetime Volume, whose temporal extent has been chosen in order to determine the spatial extent of a phenomenon over the chosen time-span. Respective phenomena may, for instance, be historical events or periods, but can also be the diachronic extent and existence of physical things. In other words, instances of this class fix a slice of another instance of E92 Spacetime Volume in time.
    The temporal extent of an instance of E93 Presence typically is predetermined by the researcher so as to focus the investigation particularly on finding the spatial extent of the phenomenon by testing for its characteristic features. There are at least two basic directions such investigations might take. The investigation may wish to determine where something was during some time or it may wish to reconstruct the total passage of a phenomenon’s spacetime volume through an examination of discrete presences. Observation and measurement of features indicating the presence or absence of a phenomenon in some space allows for the progressive approximation of spatial extents through argumentation typically based on inclusion, exclusion and various overlaps.
    """
    P164_is_temporally_specified_by: list[TimeSpan] = []
    P167_was_within: list[Place] = []
    a_presence_of: list[SpacetimeVolume] = []
    covered_parts_of: list[Place] = []
    presence_of_thing: list[PhysicalThing] = []
