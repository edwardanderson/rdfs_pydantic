from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E5_Event import Event

if TYPE_CHECKING:
    from .E1_CRM_Entity import CRMEntity
    from .E29_Design_or_Procedure import DesignOrProcedure
    from .E39_Actor import Actor
    from .E55_Type import Type
    from .E5_Event import Event
    from .E70_Thing import Thing
    from .E71_Human_Made_Thing import HumanMadeThing

class Activity(Event):
    """Activity <http://www.cidoc-crm.org/cidoc-crm/E7_Activity>.

    This class comprises actions intentionally carried out by instances of E39 Actor that result in changes of state in the cultural, social, or physical systems documented.
    This notion includes complex, composite, and long-lasting actions such as the building of a settlement or a war, as well as simple, short-lived actions such as the opening of a door.
    """
    carried_out_by: list[Actor] = []
    continued: list[Activity] = []
    continued_by: list[Activity] = []
    general_purpose: list[Type] = []
    influenced_by: list[CRMEntity] = []
    intended_use_of: list[HumanMadeThing] = []
    motivated_by: list[CRMEntity] = []
    specific_purpose: list[Event] = []
    specific_technique: list[DesignOrProcedure] = []
    technique: list[Type] = []
    used_object_of_type: list[Type] = []
    used_specific_object: list[Thing] = []
