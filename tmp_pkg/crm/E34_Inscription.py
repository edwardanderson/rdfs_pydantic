from __future__ import annotations
from .._base import OptimizedBaseModel
from .E33_Linguistic_Object import LinguisticObject
from .E37_Mark import Mark

class Inscription(Mark, LinguisticObject):
    """Inscription <http://www.cidoc-crm.org/cidoc-crm/E34_Inscription>.

    This class comprises recognisable texts that can be attached to instances of E24 Physical Human-Made Thing.
    The transcription of the text can be documented in a note by P3 has note: E62 String. The alphabet used can be documented by P2 has type: E55 Type. This class is not intended to describe the idiosyncratic characteristics of an individual physical embodiment of an inscription, but the underlying prototype. The physical embodiment is modelled in the CIDOC CRM as instances of E24 Physical Human-Made Thing.
    The relationship of a physical copy of a book to the text it contains is modelled using E18 Physical Thing. P128 carries (is carried by): E33 Linguistic Object.
    """
    ...
