from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E73_Information_Object import InformationObject

if TYPE_CHECKING:
    from .E57_Material import Material
    from .E7_Activity import Activity
    from .E99_Product_Type import ProductType

class DesignOrProcedure(InformationObject):
    """Design or Procedure <http://www.cidoc-crm.org/cidoc-crm/E29_Design_or_Procedure>.

    This class comprises documented plans for the execution of actions in order to achieve a result of a specific quality, form, or contents. In particular, it comprises plans for deliberate human activities that may result in new instances of E71 Human-Made Thing or for shaping or guiding the execution of an instance of E7 Activity.
    Instances of E29 Design or Procedure can be structured in parts and sequences or depend on others.
    This is modelled using P69 has association with (is associated with): E29 Design or Procedure.
    Designs or procedures can be seen as one of the following:.
    1. A schema for the activities it describes.
    2. A schema of the products that result from their application.
    3. An independent intellectual product that may have never been applied, such as Leonardo da Vinci’s famous plans for flying machines.
    Because designs or procedures may never be applied or only partially executed, the CIDOC CRM models a loose relationship between the plan and the respective product.
    """
    P69_has_association_with: list[DesignOrProcedure] = []
    P69i_is_associated_with: list[DesignOrProcedure] = []
    foresees_use_of: list[Material] = []
    production_plan_for: list[ProductType] = []
    used_by: list[Activity] = []
