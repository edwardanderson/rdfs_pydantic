from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E13_Attribute_Assignment import AttributeAssignment

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E55_Type import Type

class TypeAssignment(AttributeAssignment):
    """Type Assignment <http://www.cidoc-crm.org/cidoc-crm/E17_Type_Assignment>.

    This class comprises the actions of classifying items of whatever kind. Such items include objects, specimens, people, actions, and concepts.
    This class allows for the documentation of the context of classification acts in cases where the value of the classification depends on the personal opinion of the classifier, and the date that the classification was made. This class also encompasses the notion of “determination,” i.e. the systematic and molecular identification of a specimen in biology.
    """
    assigned_type: list[Type] = []
    classified: list[CRMEntity] = []
