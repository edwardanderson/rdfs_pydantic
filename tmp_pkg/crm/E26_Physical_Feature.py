from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E18_Physical_Thing import PhysicalThing

if TYPE_CHECKING:
    from .E19_Physical_Object import PhysicalObject

class PhysicalFeature(PhysicalThing):
    """Physical Feature <http://www.cidoc-crm.org/cidoc-crm/E26_Physical_Feature>.

    This class comprises identifiable features that are physically attached in an integral way to particular physical objects.
    Instances of E26 Physical Feature share many of the attributes of instances of E19 Physical Object. They may have a one-dimensional, two-dimensional, or three-dimensional geometric extent, but there are no natural borders that separate them completely in an objective way from the carrier objects. For example, a doorway is a feature but the door itself, being attached by hinges, is not.
    Instances of E26 Physical Feature can be features in a narrower sense, such as scratches, holes, reliefs, surface colours, reflection zones in an opal crystal or a density change in a piece of wood. In the wider sense, they are portions of particular objects with partially imaginary borders, such as the core of the Earth, an area of property on the surface of the Earth, a landscape or the head of a contiguous marble statue. They can be measured and dated, and it is sometimes possible to state who or what is or was responsible for them. They cannot be separated from the carrier object, but a segment of the carrier object may be identified (or sometimes removed) carrying the complete feature.
    This definition coincides with the definition of “fiat objects”, with the exception of aggregates of “bona fide objects” (Smith &amp; Varzi, 2000).
    """
    found_on: list[PhysicalObject] = []
