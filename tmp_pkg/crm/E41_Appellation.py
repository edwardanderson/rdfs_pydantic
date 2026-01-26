from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E90_Symbolic_Object import SymbolicObject

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E39_Actor import Actor

class Appellation(SymbolicObject):
    """Appellation <http://www.cidoc-crm.org/cidoc-crm/E41_Appellation>.

    This class comprises all signs, either meaningful or not, or arrangements of signs following a specific syntax, that are used or can be used to refer to and identify a specific instance of some class within a certain context.
    Instances of E41 Appellation do not identify things by their meaning, even if they happen to have one, but by convention, tradition, or agreement. Instances of E41 Appellation are cultural constructs; as such, they have a context, a history, and a use in time and space by some group of users. A given instance of E41 Appellation can have alternative forms, i.e. other instances of E41 Appellation that are regarded as equivalent, regardless of the thing it denotes.
    Different languages may use different appellations for the same thing, such as the names of major cities. Some appellations may be formulated using a valid noun phrase of a particular language. In these cases, the respective instances of E41 Appellation should also be declared as instances of E33 Linguistic Object. Then the language using the appellation can be declared with the property P72 has language: E56 Language.
    Instances of E41 Appellation may be used to identify any instance of E1 CRM Entity and sometimes are characteristic for instances of more specific subclasses of E1 CRM Entity, such as for instances of E52 Time-Span (for instance “dates”), E39 Actor, E53 Place or E28 Conceptual Object. Postal addresses and E-mail addresses are characteristic examples of identifiers used by services transporting things between clients.
    Even numerically expressed identifiers for extents in space or time are also regarded as instances of E41 Appellation, such as Gregorian dates or spatial coordinates, even though they allow for determining some time or location by a known procedure starting from a reference point and by virtue of that fact play a double role as instances of E59 Primitive Value.
    E41 Appellation should not be confused with the act of naming something. Cf. E15 Identifier Assignment.
    """
    P139i_is_alternative_form_of: list[Appellation] = []
    alternative: list[Appellation] = []
    identifies: list[CRMEntity] = []
    provides_access_to: list[Actor] = []
