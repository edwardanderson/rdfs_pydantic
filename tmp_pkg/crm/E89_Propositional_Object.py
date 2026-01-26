from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E28_Conceptual_Object import ConceptualObject

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity

class PropositionalObject(ConceptualObject):
    """Propositional Object <http://www.cidoc-crm.org/cidoc-crm/E89_Propositional_Object>.

    This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions, algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real or imaginary things and that are documented as single units or serve as topic of discourse.
    This class also comprises items that are “about” something in the sense of a subject. In the wider sense, this class includes expressions of psychological value such as non-figural art and musical themes. However, conceptual items such as types and classes are not instances of E89 Propositional Object. This should not be confused with the definition of a type, which is indeed an instance of E89 Propositional Object.
    """
    about: list[CRMEntity] = []
    conceptual_part: list[PropositionalObject] = []
    conceptually_part_of: list[PropositionalObject] = []
    refers_to: list[CRMEntity] = []
