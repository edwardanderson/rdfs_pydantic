from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E28_Conceptual_Object import ConceptualObject

if TYPE_CHECKING:
    from .E13_Attribute_Assignment import AttributeAssignment
    from .E17_Type_Assignment import TypeAssignment
    from .E1_CRM_Entity import CRMEntity
    from .E70_Thing import Thing
    from .E71_Human_Made_Thing import HumanMadeThing
    from .E7_Activity import Activity
    from .E83_Type_Creation import TypeCreation

class Type(ConceptualObject):
    """Type <http://www.cidoc-crm.org/cidoc-crm/E55_Type>.

    This class comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize and classify instances of CIDOC CRM classes. Instances of E55 Type represent concepts, in contrast to instances of E41 Appellation which are used to name instances of CIDOC CRM classes.
    E55 Type provides an interface to domain specific ontologies and thesauri. These can be represented in the CIDOC CRM as subclasses of E55 Type, forming hierarchies of terms, i.e. instances of E55 Type linked via P127 has broader term (has narrower term): E55 Type. Such hierarchies may be extended with additional properties.
    """
    P127_has_broader_term: list[Type] = []
    P127i_has_narrower_term: list[Type] = []
    P177i_is_type_of_property_assigned: list[AttributeAssignment] = []
    defines_typical_parts_of: list[Type] = []
    defines_typical_wholes_for: list[Type] = []
    exemplified_by: list[CRMEntity] = []
    intention_of: list[HumanMadeThing] = []
    purpose_of: list[Activity] = []
    technique_of: list[Activity] = []
    type_assigned_by: list[TypeAssignment] = []
    type_created_by: list[TypeCreation] = []
    type_of: list[CRMEntity] = []
    type_of_object_used_in: list[Activity] = []
    use_of: list[Thing] = []
