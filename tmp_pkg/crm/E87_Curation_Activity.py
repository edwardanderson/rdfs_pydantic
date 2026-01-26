from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E7_Activity import Activity

if TYPE_CHECKING:
    from .E78_Curated_Holding import CuratedHolding

class CurationActivity(Activity):
    """Curation Activity <http://www.cidoc-crm.org/cidoc-crm/E87_Curation_Activity>.

    This class comprises the activities that contribute to the management and the preservation and evolution of instances of E78 Curated Holding, following an implicit or explicit curation plan.
    It specializes the notion of activity into the curation of a collection and allows the history of curation to be recorded.
    Items are accumulated and organized following criteria such as subject, chronological period, material type, style of art, etc., and can be added or removed from an instance of E78 Curated Holding for a specific purpose and/or audience. The initial aggregation of items to form a collection is regarded as an instance of E12 Production Event, while the activities of evolving, preserving, and promoting a collection are regarded as instances of E87 Curation Activity.
    """
    curated: list[CuratedHolding] = []
