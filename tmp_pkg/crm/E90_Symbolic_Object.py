from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E28_Conceptual_Object import ConceptualObject
from .E72_Legal_Object import LegalObject

if TYPE_CHECKING:
    from .E15_Identifier_Assignment import IdentifierAssignment
    from .E18_Physical_Thing import PhysicalThing
    from .E73_Information_Object import InformationObject

class SymbolicObject(LegalObject, ConceptualObject):
    """Symbolic Object <http://www.cidoc-crm.org/cidoc-crm/E90_Symbolic_Object>.

    This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers, traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code, or mathematical formulae that have an objectively recognizable structure and that are documented as single units.
    It includes sets of signs of any nature, which may serve to designate something, or to communicate some propositional content. An instance of E90 Symbolic Object may or may not have a specific meaning, for example an arbitrary character string.
    In some cases, the content of an instance of E90 Symbolic Object may completely be represented by a serialized digital content model, such as a sequence of ASCII-encoded characters, an XML or HTML document, or a TIFF image. The property P3 has note and its subproperty P190 has symbolic content allow for the description of this content model. In order to disambiguate which symbolic level is the carrier of the meaning, the property P3.1 has type can be used to specify the encoding (e.g. “bit”, “Latin character”, RGB pixel).
    """
    P106_is_composed_of: list[SymbolicObject] = []
    P106i_forms_part_of: list[SymbolicObject] = []
    carried_by: list[PhysicalThing] = []
    content: str | None = None
    digitally_carried_by: list[DigitalObject] = []
    incorporated_by: list[InformationObject] = []
    used_in: list[IdentifierAssignment] = []
