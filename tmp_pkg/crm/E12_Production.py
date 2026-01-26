from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E11_Modification import Modification
from .E63_Beginning_of_Existence import BeginningOfExistence

if TYPE_CHECKING:
    from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing
    from .E99_Product_Type import ProductType

class Production(BeginningOfExistence, Modification):
    """Production <http://www.cidoc-crm.org/cidoc-crm/E12_Production>.

    This class comprises activities that are designed to, and succeed in, creating one or more new items.
    It specializes the notion of modification into production. The decision as to whether or not an object is regarded as new is context sensitive. Normally, items are considered “new” if there is no obvious overall similarity between them and the consumed items and material used in their production. In other cases, an item is considered “new” because it becomes relevant to documentation by a modification. For example, the scribbling of a name on a potsherd may make it a voting token. The original potsherd may not be worth documenting, in contrast to the inscribed one.
    This entity can be collective: the printing of a thousand books, for example, would normally be considered a single event.
    An event should also be documented using an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the originals. In this case, the new items have separate identities and matter is preserved, but identity is not.
    """
    produced: list[PhysicalHumanMadeThing] = []
    produced_thing_of_product_type: list[ProductType] = []
