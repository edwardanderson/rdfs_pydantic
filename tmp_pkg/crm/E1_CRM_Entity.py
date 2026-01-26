from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel

if TYPE_CHECKING:
    from ..la.Addition import Addition
    from ..la.Removal import Removal
    from ..la.Set import Set
    from .E13_Attribute_Assignment import AttributeAssignment
    from .E17_Type_Assignment import TypeAssignment
    from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing
    from .E31_Document import Document
    from .E32_Authority_Document import AuthorityDocument
    from .E36_Visual_Item import VisualItem
    from .E41_Appellation import Appellation
    from .E42_Identifier import Identifier
    from .E55_Type import Type
    from .E7_Activity import Activity
    from .E83_Type_Creation import TypeCreation
    from .E89_Propositional_Object import PropositionalObject

class CRMEntity(OptimizedBaseModel):
    """CRM Entity <http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity>.

    This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.
    It is an abstract concept providing for three general properties:.
    Identification by name or appellation, and in particular by a preferred identifier.
    Classification by type, allowing further refinement of the specific subclass to which an instance belongs.
    Attachment of free text and other unstructured data for the expression of anything not captured by formal properties.
    All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity.
    """
    added_member_by: list[Addition] = []
    assigned_by: list[AttributeAssignment] = []
    attributed_by: list[AttributeAssignment] = []
    classified_as: list[Type] = []
    classified_by: list[TypeAssignment] = []
    depicted_by: list[PhysicalHumanMadeThing] = []
    documented_in: list[Document] = []
    equivalent: list[CRMEntity] = []
    exemplifies: list[Type] = []
    identified_by: list[Appellation] = []
    influenced: list[Activity] = []
    listed_in: list[AuthorityDocument] = []
    member_of: list[Set] = []
    motivated: list[Activity] = []
    note: str | None = None
    preferred_identifier: list[Identifier] = []
    referred_to_by: list[PropositionalObject] = []
    removed_member_by: list[Removal] = []
    representation: list[VisualItem] = []
    subject_of: list[PropositionalObject] = []
    supported_type_creation: list[TypeCreation] = []
