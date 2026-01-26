from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E1_CRM_Entity import CRMEntity

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E52_Time_Span import TimeSpan
    from .E53_Place import Place
    from .E93_Presence import Presence

class SpacetimeVolume(CRMEntity):
    """Spacetime Volume <http://www.cidoc-crm.org/cidoc-crm/E92_Spacetime_Volume>.

    This class comprises 4-dimensional point sets (volumes) in physical spacetime (in contrast to mathematical models of it) regardless of their true geometric forms. They may derive their identity from being the extent of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime. Intersections of instances of E92 Spacetime Volume, E53 Place, and E52 Time-Span are also regarded as instances of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives from or due to the limited precision up to which defining expression can be identified with a real extent in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time.
    """
    P132_spatiotemporally_overlaps_with: list[SpacetimeVolume] = []
    P133_is_spatiotemporally_separated_from: list[SpacetimeVolume] = []
    during: list[SpacetimeVolume] = []
    includes: list[SpacetimeVolume] = []
    presence: list[Presence] = []
    spacetime_volume_is_defined_by: str | None = None
    spatial_projection: list[Place] = []
    temporal_projection: list[TimeSpan] = []
    thing_defined_by: list[PhysicalThing] = []
