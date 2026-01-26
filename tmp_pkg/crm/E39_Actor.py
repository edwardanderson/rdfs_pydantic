from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E77_Persistent_Item import PersistentItem

if TYPE_CHECKING:
    from .E10_Transfer_of_Custody import TransferOfCustody
    from .E18_Physical_Thing import PhysicalThing
    from .E19_Physical_Object import PhysicalObject
    from .E30_Right import Right
    from .E41_Appellation import Appellation
    from .E53_Place import Place
    from .E5_Event import Event
    from .E72_Legal_Object import LegalObject
    from .E74_Group import Group
    from .E78_Curated_Holding import CuratedHolding
    from .E7_Activity import Activity
    from .E85_Joining import Joining
    from .E86_Leaving import Leaving
    from .E8_Acquisition import Acquisition

class Actor(PersistentItem):
    """Actor <http://www.cidoc-crm.org/cidoc-crm/E39_Actor>.

    This class comprises people, either individually or in groups, who have the potential to perform intentional actions of kinds for which they can be held responsible.
    """
    P107i_is_current_or_former_member_of: list[Group] = []
    acquired_custody_through: list[TransferOfCustody] = []
    acquired_title_through: list[Acquisition] = []
    carried_out: list[Activity] = []
    contact_point: list[Appellation] = []
    current_custodian_of: list[PhysicalThing] = []
    current_or_former_curator_of: list[CuratedHolding] = []
    current_owner_of: list[PhysicalThing] = []
    current_permanent_custodian_of: list[PhysicalObject] = []
    former_or_current_keeper_of: list[PhysicalThing] = []
    former_or_current_owner_of: list[PhysicalThing] = []
    joined_by: list[Joining] = []
    left_by: list[Leaving] = []
    participated_in: list[Event] = []
    possesses: list[Right] = []
    residence: list[Place] = []
    right_on: list[LegalObject] = []
    surrendered_custody_through: list[TransferOfCustody] = []
    surrendered_title_through: list[Acquisition] = []
