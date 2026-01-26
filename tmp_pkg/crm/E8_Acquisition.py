from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from ..la.Transfer import Transfer
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E18_Physical_Thing import PhysicalThing
    from .E39_Actor import Actor

class Acquisition(Transfer, Activity):
    """Acquisition <http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition>.

    This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more other instances of E39 Actor.
    The class also applies to the establishment or loss of ownership of instances of E18 Physical Thing. It does not, however, imply changes of any other kinds of rights. The recording of the donor and/or recipient is optional. It is possible that in an instance of E8 Acquisition there is either no donor or no recipient. Depending on the circumstances, it may describe:.
    1. the beginning of ownership.
    2. the end of ownership.
    3. the transfer of ownership.
    4. the acquisition from an unknown source.
    5. the loss of title due to destruction of the item.
    It may also describe events where a collector appropriates legal title, for example, by annexation or field collection. The interpretation of the museum notion of “accession” differs between institutions. The CIDOC CRM therefore models legal ownership (E8 Acquisition) and physical custody (E10 Transfer of Custody) separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.
    """
    transferred_title_from: list[Actor] = []
    transferred_title_of: list[PhysicalThing] = []
    transferred_title_to: list[Actor] = []
