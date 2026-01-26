from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E64_End_of_Existence import EndOfExistence

if TYPE_CHECKING:
    from .E21_Person import Person

class Death(EndOfExistence):
    """Death <http://www.cidoc-crm.org/cidoc-crm/E69_Death>.

    This class comprises the deaths of human beings.
    If a person is killed, their death should be instantiated as E69 Death and as E7 Activity. The death or perishing of other living beings should be documented as instances of E64 End of Existence.
    """
    death_of: list[Person] = []
