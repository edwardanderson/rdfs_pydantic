from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E55_Type import Type

if TYPE_CHECKING:
    from .E12_Production import Production
    from .E19_Physical_Object import PhysicalObject
    from .E29_Design_or_Procedure import DesignOrProcedure

class ProductType(Type):
    """Product Type <http://www.cidoc-crm.org/cidoc-crm/E99_Product_Type>.

    This class comprises types that stand as the models for instances of E22 Human-Made Object that are produced as the result of production activities using plans exact enough to result in one or more series of uniform, functionally and aesthetically identical and interchangeable items. The product type is the intended ideal form of the manufacture process. It is typical of instances of E22 Human-Made Object that conform to an instance of E99 Product Type that its component parts are interchangeable with component parts of other instances of E22 Human-Made Object made after the model of the same instance of E99 Product Type. Frequently, the uniform production according to a given instance of E99 Product Type is achieved by creating individual tools, such as moulds or print plates that are themselves carriers of the design of the product type. Modern tools may use the flexibility of electronically controlled devices to achieve such uniformity. The product type itself, i.e. the potentially unlimited series of aesthetically equivalent items, may be the target of artistic design, rather than the individual object. In extreme cases, only one instance of a product type may have been produced, such as in a “print on demand” process which was only triggered once. However, this should not be confused with industrial prototypes, such as car prototypes, which are produced prior to the production line being set up, or test the production line itself.
    """
    production_plan: list[DesignOrProcedure] = []
    requires_production_tool: list[PhysicalObject] = []
    type_produced_by: list[Production] = []
