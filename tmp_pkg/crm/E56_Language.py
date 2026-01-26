from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E55_Type import Type

if TYPE_CHECKING:
    from .E33_Linguistic_Object import LinguisticObject

class Language(Type):
    """Language <http://www.cidoc-crm.org/cidoc-crm/E56_Language>.

    This class is a specialization of E55 Type and comprises the natural languages in the sense of concepts.
    This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E56 Language, e.g. “instances of Mandarin Chinese”.
    It is recommended that internationally or nationally agreed codes and terminology should be used to denote instances of E56 Language, such as those defined in ISO 639-3:2007 and later versions.
    """
    language_of: list[LinguisticObject] = []
