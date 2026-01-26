from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E18_Physical_Thing import PhysicalThing

if TYPE_CHECKING:
    from .E26_Physical_Feature import PhysicalFeature
    from .E39_Actor import Actor
    from .E53_Place import Place
    from .E99_Product_Type import ProductType
    from .E9_Move import Move

class PhysicalObject(PhysicalThing):
    """Physical Object <http://www.cidoc-crm.org/cidoc-crm/E19_Physical_Object>.

    This class comprises items of a material nature that are units for documentation and have physical boundaries that separate them completely in an objective way from other objects.
    The class also includes all aggregates of objects made for functional purposes of whatever kind, independent of physical coherence, such as a set of chessmen. Typically, instances of E19 Physical Object can be moved (if not too heavy).
    In some contexts, such objects, except for aggregates, are also called “bona fide objects”, i.e. naturally defined objects (Smith &amp; Varzi, 2000).
    The decision as to what is documented as a complete item, rather than by its parts or components, may be purely administrative or may be a result of the order in which the item was acquired.
    """
    bears: list[PhysicalFeature] = []
    current_location: list[Place] = []
    current_permanent_custodian: list[Actor] = []
    current_permanent_location: list[Place] = []
    moved_by: list[Move] = []
    number_of_parts: str | None = None
    production_tool_for: list[ProductType] = []
