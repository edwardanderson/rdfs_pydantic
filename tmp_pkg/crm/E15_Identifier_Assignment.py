from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E13_Attribute_Assignment import AttributeAssignment

if TYPE_CHECKING:
    from .E42_Identifier import Identifier
    from .E90_Symbolic_Object import SymbolicObject

class IdentifierAssignment(AttributeAssignment):
    """Identifier Assignment <http://www.cidoc-crm.org/cidoc-crm/E15_Identifier_Assignment>.

    This class comprises activities that result in the allocation of an identifier to an instance of E1 CRM Entity. An instance of E15 Identifier Assignment may include the creation of the identifier from multiple constituents, which themselves may be instances of E41 Appellation. The syntax and kinds of constituents to be used may be declared in a rule constituting an instance of E29 Design or Procedure.
    Examples of such identifiers include Find Numbers, Inventory Numbers, uniform titles in the sense of librarianship and Digital Object Identifiers (DOI). Documenting the act of identifier assignment and deassignment is especially useful when objects change custody or the identification system of an organization is changed. In order to keep track of the identity of things in such cases, it is important to document by whom, when, and for what purpose an identifier is assigned to an item.
    The fact that an identifier is a preferred one for an organisation can be expressed by using the property E1 CRM Entity. P48 has preferred identifier (is preferred identifier of): E42 Identifier. It can better be expressed in a context independent form by assigning a suitable E55 Type, such as “preferred identifier assignment”, to the respective instance of E15 Identifier Assignment through the P2 has type (is type of) property.
    """
    assigned_identifier: list[Identifier] = []
    deassigned: list[Identifier] = []
    used_constituent: list[SymbolicObject] = []
