from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E1_CRM_Entity import CRMEntity

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E19_Physical_Object import PhysicalObject
    from .E39_Actor import Actor
    from .E4_Period import Period
    from .E92_Spacetime_Volume import SpacetimeVolume
    from .E93_Presence import Presence
    from .E9_Move import Move

class Place(CRMEntity):
    """Place <http://www.cidoc-crm.org/cidoc-crm/E53_Place>.

    This class comprises extents in the natural space where people live, in particular on the surface of the Earth, in the pure sense of physics: independent from temporal phenomena and matter. They may serve describing the physical location of things or phenomena or other areas of interest. Geometrically, instances of E53 Place constitute single contiguous areas or a finite aggregation of disjoint areas in space which are each individually contiguous. They may have fuzzy boundaries.
    The instances of E53 Place are usually determined by reference to the position of “immobile” objects such as buildings, cities, mountains, rivers, or dedicated geodetic marks, but may also be determined by reference to mobile objects. A Place can be determined by combining a frame of reference and a location with respect to this frame.
    It is sometimes argued that instances of E53 Place are best identified by global coordinates or absolute reference systems. However, relative references are often more relevant in the context of cultural documentation and tend to be more precise. In particular, people are often interested in position in relation to large, mobile objects, such as ships. For example, the Place at which Nelson died is known with reference to a large mobile object, i.e. H.M.S Victory. A resolution of this Place in terms of absolute coordinates would require knowledge of the movements of the vessel and the precise time of death, either of which may be revised, and the result would lack historical and cultural relevance.
    Any instance of E18 Physical Thing can serve as a frame of reference for an instance of E53 Place. This may be documented using the property P157 is at rest relative to (provides reference space for).
    """
    P161i_is_spatial_projection_of: list[SpacetimeVolume] = []
    P167i_includes: list[Presence] = []
    P89_falls_within: list[Place] = []
    P89i_contains: list[Place] = []
    approximated_by: list[Place] = []
    approximates: list[Place] = []
    at_rest_relative_to: list[PhysicalThing] = []
    at_some_place_within: str | None = None
    borders_with: list[Place] = []
    current_or_former_residence_of: list[Actor] = []
    current_permanent_location_of: list[PhysicalObject] = []
    currently_holds: list[PhysicalObject] = []
    defined_by: str | None = None
    destination_of: list[Move] = []
    former_or_current_location_of: list[PhysicalThing] = []
    located_on_or_within: list[PhysicalThing] = []
    location_of: list[Period] = []
    occupied_by: list[PhysicalThing] = []
    origin_of: list[Move] = []
    overlaps_with: list[Place] = []
    partially_covered_by: list[Presence] = []
    spatially_contains: str | None = None
