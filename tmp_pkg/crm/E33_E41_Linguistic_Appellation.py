from __future__ import annotations
from .._base import OptimizedBaseModel
from .E33_Linguistic_Object import LinguisticObject
from .E41_Appellation import Appellation

class Name(Appellation, LinguisticObject):
    """Linguistic Appellation <http://www.cidoc-crm.org/cidoc-crm/E33_E41_Linguistic_Appellation>."""
    ...
