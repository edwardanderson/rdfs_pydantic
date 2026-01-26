from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E89_Propositional_Object import PropositionalObject
from .E90_Symbolic_Object import SymbolicObject

if TYPE_CHECKING:
    from .E90_Symbolic_Object import SymbolicObject

class InformationObject(SymbolicObject, PropositionalObject):
    """Information Object <http://www.cidoc-crm.org/cidoc-crm/E73_Information_Object>.

    This class comprises identifiable immaterial items, such as poems, jokes, data sets, images, texts, multimedia objects, procedural prescriptions, computer program code, algorithm or mathematical formulae, that have an objectively recognizable structure and are documented as single units. The encoding structure known as a “named graph” also falls under this class, so that each “named graph” is an instance of E73 Information Object.
    An instance of E73 Information Object does not depend on a specific physical carrier, which can include human memory, and it can exist on one or more carriers simultaneously.
    Instances of E73 Information Object of a linguistic nature should be declared as instances of the E33 Linguistic Object subclass. Instances of E73 Information Object of a documentary nature should be declared as instances of the E31 Document subclass. Conceptual items such as types and classes are not instances of E73 Information Object, nor are ideas without a reproducible expression.
    """
    presence_of: list[SymbolicObject] = []
