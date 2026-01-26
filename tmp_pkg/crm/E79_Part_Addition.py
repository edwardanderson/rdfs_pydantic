from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E11_Modification import Modification

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing

class PartAddition(Modification):
    """Part Addition <http://www.cidoc-crm.org/cidoc-crm/E79_Part_Addition>.

    This class comprises activities that result in an instance of E18 Physical Thing being increased, enlarged, or augmented by the addition of a part.
    Typical scenarios include the attachment of an accessory, the integration of a component, the addition of an element to an aggregate object, or the accessioning of an object into a curated instance of E78 Curated Holding. Both the E18 Physical Thing being augmented and the E18 Physical Thing that is being added are treated as separate identifiable wholes prior to the instance of E79 Part Addition. Following the addition of parts, the resulting assemblages are treated objectively as single identifiable wholes, made up of constituent or component parts bound together either physically (for example the engine becoming a part of the car), or by sharing a common purpose (such as the 32 chess pieces that make up a chess set). This class of activities forms a basis for reasoning about the history and continuity of identity of objects that are integrated into other objects over time, such as precious gemstones being repeatedly incorporated into different items of jewellery, or cultural artefacts being added to different museum instances of E78 Curated Holding over their lifespan.
    """
    added: list[PhysicalThing] = []
    augmented: list[PhysicalThing] = []
