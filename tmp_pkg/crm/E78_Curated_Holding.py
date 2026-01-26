from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing

if TYPE_CHECKING:
    from .E39_Actor import Actor
    from .E87_Curation_Activity import CurationActivity

class CuratedHolding(PhysicalHumanMadeThing):
    """Curated Holding <http://www.cidoc-crm.org/cidoc-crm/E78_Curated_Holding>.

    This class comprises aggregations of instances of E18 Physical Thing that are assembled and maintained (“curated” and “preserved,” in museological terminology) by one or more instances of E39 Actor over time for a specific purpose and audience, and according to a particular collection development plan. Typical instances of curated holdings are museum collections, archives, library holdings and digital libraries. A digital library is regarded as an instance of E18 Physical Thing because it requires keeping physical carriers of the electronic content.
    Items may be added or removed from an E78 Curated Holding in pursuit of this plan. This class should not be confused with the E39 Actor maintaining the E78 Curated Holding who is often referred to using the name of the E78 Curated Holding (e.g. “The Wallace Collection decided…”).
    Collective objects in the general sense, like a tomb full of gifts, a folder with stamps, or a set of chessmen, should be documented as instances of E19 Physical Object, and not as instances of E78 Curated Holding. This is because they form wholes, either because they are physically bound together or because they are kept together for their functionality.
    """
    curated_by: list[CurationActivity] = []
    current_or_former_curator: list[Actor] = []
