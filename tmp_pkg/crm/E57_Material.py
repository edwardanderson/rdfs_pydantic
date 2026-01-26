from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E55_Type import Type

if TYPE_CHECKING:
    from .E11_Modification import Modification
    from .E18_Physical_Thing import PhysicalThing
    from .E29_Design_or_Procedure import DesignOrProcedure

class Material(Type):
    """Material <http://www.cidoc-crm.org/cidoc-crm/E57_Material>.

    This class is a specialization of E55 Type and comprises the concepts of materials.
    Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing).
    This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E57 Material, e.g. “instances of gold”.
    It is recommended that internationally or nationally agreed codes and terminology should be used.
    """
    employed_in: list[Modification] = []
    incorporated_in: list[PhysicalThing] = []
    use_foreseen_by: list[DesignOrProcedure] = []
