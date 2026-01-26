from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E11_Modification import Modification

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing

class PartRemoval(Modification):
    """Part Removal <http://www.cidoc-crm.org/cidoc-crm/E80_Part_Removal>.

    This class comprises the activities that result in an instance of E18 Physical Thing being decreased by the removal of a part.
    Typical scenarios include the detachment of an accessory, the removal of a component or part of a composite object, or the deaccessioning of an object from a curated collection, an instance of E78 Curated Holding. If the instance of E80 Part Removal results in the total decomposition of the original object into pieces, such that the whole ceases to exist, the activity should instead be modelled as an instance of E81 Transformation, i.e. a simultaneous destruction and production. In cases where the part removed has no discernible identity prior to its removal but does have an identity subsequent to its removal, the activity should be modelled as both an instance of E80 Part Removal and E12 Production. This class of activities forms a basis for reasoning about the history, and continuity of identity over time, of objects that are removed from other objects, such as precious gemstones being extracted from different items of jewellery, or cultural artifacts being deaccessioned from different museum collections over their lifespan.
    """
    diminished: list[PhysicalThing] = []
    removed: list[PhysicalThing] = []
