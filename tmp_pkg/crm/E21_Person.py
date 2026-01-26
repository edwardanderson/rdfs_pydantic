from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E20_Biological_Object import BiologicalObject
from .E39_Actor import Actor

if TYPE_CHECKING:
    from .E67_Birth import Birth
    from .E69_Death import Death

class Person(Actor, BiologicalObject):
    """Person <http://www.cidoc-crm.org/cidoc-crm/E21_Person>.

    This class comprises real persons who live or are assumed to have lived.
    Legendary figures that may have existed, such as Ulysses and King Arthur, fall into this class if the documentation refers to them as historical figures. In cases where doubt exists as to whether several persons are in fact identical, multiple instances can be created and linked to indicate their relationship. The CIDOC CRM does not propose a specific form to support reasoning about possible identity.
    In a bibliographic context, a name presented following the conventions usually employed for personal names will be assumed to correspond to an actual real person (an instance of E21 Person), unless evidence is available to indicate that this is not the case. The fact that a persona may erroneously be classified as an instance of E21 Person does not imply that the concept comprises personae.
    """
    born: list[Birth] = []
    died: list[Death] = []
    father_for: list[Birth] = []
    gave_birth: list[Birth] = []
    parent: list[Person] = []
    parent_of: list[Person] = []
