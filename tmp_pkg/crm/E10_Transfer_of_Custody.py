from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Transfer import Transfer
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E39_Actor import Actor

class TransferOfCustody(Transfer, Activity):
    """Transfer of Custody <http://www.cidoc-crm.org/cidoc-crm/E10_Transfer_of_Custody>.

    This class comprises transfers of the physical custody or the legal responsibility for the physical custody of objects. The recording of the donor or recipient is optional. It is possible that in an instance of E10 Transfer of Custody there is either no donor or no recipient.
    Depending on the circumstances, it may describe:.
    1. the beginning of custody (there is no previous custodian).
    2. the end of custody (there is no subsequent custodian).
    3. the transfer of custody (transfer from one custodian to the next).
    4. the receipt of custody from an unknown source (the previous custodian is unknown).
    5. the declared loss of an object (the current or subsequent custodian is unknown).
    In the event that only a single kind of transfer of custody occurs, either the legal responsibility for the custody or the actual physical possession of the object but not both, this difference should be expressed using the property P2 has type (is type of).
    The sense of physical possession requires that the object of custody be in the hands of the keeper at least with a part representative for the whole. The way, in which a representative part is defined, should ensure that it is unambiguous who keeps a part and who the whole and should be consistent with the identity criteria of the kept instance of E18 Physical Thing.
    The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore models legal ownership and physical custody separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.
    Theft is a specific case of illegal transfer of custody.
    """
    transferred_custody_from: list[Actor] = []
    transferred_custody_of: list[PhysicalThing] = []
    transferred_custody_to: list[Actor] = []
