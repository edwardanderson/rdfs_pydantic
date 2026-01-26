from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E63_Beginning_of_Existence import BeginningOfExistence
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E28_Conceptual_Object import ConceptualObject

class Creation(BeginningOfExistence, Activity):
    """Creation <http://www.cidoc-crm.org/cidoc-crm/E65_Creation>.

    This class comprises events that result in the creation of conceptual items or immaterial products, such as legends, poems, texts, music, images, movies, laws, types, etc.
    """
    created: list[ConceptualObject] = []
