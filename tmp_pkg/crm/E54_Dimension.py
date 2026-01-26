from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E1_CRM_Entity import CRMEntity

if TYPE_CHECKING:
    from .E16_Measurement import Measurement
    from .E52_Time_Span import TimeSpan
    from .E58_Measurement_Unit import MeasurementUnit
    from .E70_Thing import Thing

class Dimension(CRMEntity):
    """Dimension <http://www.cidoc-crm.org/cidoc-crm/E54_Dimension>.

    This class comprises quantifiable properties that can be measured by some calibrated means and can be approximated by values, i.e. points or regions in a mathematical or conceptual space, such as natural or real numbers, RGB values, etc.
    An instance of E54 Dimension represents the empirical or theoretically derived quantity, including the precision tolerances resulting from the particular method or calculation. The identity of an instance of E54 Dimension depends on the method of its determination because each method may produce different values even when determining comparable qualities. For instance, the wingspan of a bird alive or dead is a different dimension. Thermoluminescence dating and Rehydroxylation [RHX] dating are different dimensions of temporal distance from now, even if they aim at dating the same object. The method of determination should be expressed using the property P2 has type (is type of). Note that simple terms such as “diameter” or “length” are normally insufficient to unambiguously describe a respective dimension. In contrast, “maximum linear extent” may be sufficient.
    The properties of the class E54 Dimension allow for expressing the numerical approximation of the values of instances of E54 Dimension adequate to the precision of the applied method of determination. If the respective quantity belongs to a non-discrete space according to the laws of physics, such as spatial distances, it is recommended to record them as approximations by intervals or regions of indeterminacy enclosing the assumed true values. For instance, a length of 5 cm may be recorded as 4.5-5.5 cm, according to the precision of the respective observation. Note, that comparability of values described in different units depends critically on the representation as value regions.
    Numerical approximations in archaic instances of E58 Measurement Unit used in historical records should be preserved. Equivalents corresponding to current knowledge should be recorded as additional instances of E54 Dimension, as appropriate.
    """
    dimension_of: list[Thing] = []
    duration_of: list[TimeSpan] = []
    lower_value_limit: str | None = None
    observed_in: list[Measurement] = []
    unit: list[MeasurementUnit] = []
    upper_value_limit: str | None = None
    value: str | None = None
