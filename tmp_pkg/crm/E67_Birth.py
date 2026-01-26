from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E63_Beginning_of_Existence import BeginningOfExistence

if TYPE_CHECKING:
    from .E21_Person import Person

class Birth(BeginningOfExistence):
    """Birth <http://www.cidoc-crm.org/cidoc-crm/E67_Birth>.

    This class comprises the births of human beings. E67 Birth is a biological event focussing on the context of people coming into life. (E63 Beginning of Existence comprises the coming into life of any living being.).
    Twins, triplets, etc. are brought into life by the same instance of E67 Birth. The introduction of the E67 Birth event as a documentation element allows the description of a range of family relationships in a simple model. Suitable extensions may describe more details and the complexity of motherhood since the advent of modern medicine. In this model, the biological father is not seen as a necessary participant in the E67 Birth.
    """
    brought_into_life: list[Person] = []
    by_mother: list[Person] = []
    from_father: list[Person] = []
