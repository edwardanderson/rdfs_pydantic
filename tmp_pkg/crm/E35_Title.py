from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E33_Linguistic_Object import LinguisticObject
from .E41_Appellation import Appellation

if TYPE_CHECKING:
    from .E71_Human_Made_Thing import HumanMadeThing

class Title(Appellation, LinguisticObject):
    """Title <http://www.cidoc-crm.org/cidoc-crm/E35_Title>.

    This class comprises the textual strings that within a cultural context can be clearly identified as titles due to their form. Being a subclass of E41 Appellation, E35 Title can only be used when such a string is actually used as a title of a work, such as a text, an artwork, or a piece of music.
    Titles are proper noun phrases or verbal phrases, and should not be confused with generic object names such as “chair”, “painting”, or “book” (the latter are common nouns that stand for instances of E55 Type). Titles may be assigned by the creator of the work itself, or by a social group.
    This class also comprises the translations of titles that are used as surrogates for the original titles in different social contexts.
    """
    title_of: list[HumanMadeThing] = []
