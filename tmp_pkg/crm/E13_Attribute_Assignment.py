from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E55_Type import Type

class AttributeAssignment(Activity):
    """Attribute Assignment <http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment>.

    This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts. The type of the property asserted to hold between two items or concepts can be described by the property P177 assigned property of type (is type of property assigned): E55 Type.
    For example, the class describes the actions of people making propositions and statements during certain scientific/scholarly procedures, e.g. the person and date when a condition statement was made, an identifier was assigned, the museum object was measured, etc. Which kinds of such assignments and statements need to be documented explicitly in structures of a schema rather than free text, depends on whether this information should be accessible by structured queries.
    This class allows for the documentation of how the respective assignment came about, and whose opinion it was. Note that all instances of properties described in a knowledge base are the opinion of someone. Per default, they are the opinion of the team maintaining the knowledge base. This fact must not individually be registered for all instances of properties provided by the maintaining team, because it would result in an endless recursion of whose opinion was the description of an opinion. Therefore, the use of instances of E13 Attribute Assignment marks the fact that the maintaining team is in general neutral to the validity of the respective assertion, but registers someone else’s opinion and how it came about.
    All properties assigned in such an action can also be seen as directly relating the respective pair of items or concepts. Multiple use of instances of E13 Attribute Assignment may possibly lead to a collection of contradictory values.
    """
    assigned: list[CRMEntity] = []
    assigned_property: list[Type] = []
    assigned_to: list[CRMEntity] = []
    property_classified_as: list[Type] = []
