from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E55_Type import Type

if TYPE_CHECKING:
    from .E54_Dimension import Dimension

class MeasurementUnit(Type):
    """Measurement Unit <http://www.cidoc-crm.org/cidoc-crm/E58_Measurement_Unit>.

    This class is a specialization of E55 Type and comprises the types of measurement units: feet, inches, centimetres, litres, lumens, etc.
    This type is used categorically in the model without reference to instances of it, i.e. the model does not foresee the description of instances of instances of E58 Measurement Unit, e.g. “instances of cm”.
    Système International (SI) units or internationally recognized non-SI terms should be used whenever possible, such as those defined by ISO80000:2009. Archaic Measurement Units used in historical records should be preserved.
    """
    unit_of: list[Dimension] = []
