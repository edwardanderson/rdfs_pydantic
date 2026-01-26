from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E41_Appellation import Appellation

if TYPE_CHECKING:
    from .E15_Identifier_Assignment import IdentifierAssignment
    from .E1_CRM_Entity import CRMEntity

class Identifier(Appellation):
    """Identifier <http://www.cidoc-crm.org/cidoc-crm/E42_Identifier>.

    This class comprises strings or codes assigned to instances of E1 CRM Entity in order to identify them uniquely and permanently within the context of one or more organisations. Such codes are often known as inventory numbers, registration codes, etc. and are typically composed of alphanumeric sequences. Postal addresses, telephone numbers, URLs and e-mail addresses are characteristic examples of identifiers used by services transporting things between clients.
    The class E42 Identifier is not normally used for machine-generated identifiers used for automated processing unless these are also used by human agents.
    """
    deassigned_by: list[IdentifierAssignment] = []
    identifier_assigned_by: list[IdentifierAssignment] = []
    preferred_identifier_of: list[CRMEntity] = []
