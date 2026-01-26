from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E18_Physical_Thing import PhysicalThing
from .E71_Human_Made_Thing import HumanMadeThing

if TYPE_CHECKING:
    from .E12_Production import Production
    from .E1_CRM_Entity import CRMEntity
    from .E36_Visual_Item import VisualItem

class PhysicalHumanMadeThing(HumanMadeThing, PhysicalThing):
    """Physical Human-Made Thing <http://www.cidoc-crm.org/cidoc-crm/E24_Physical_Human-Made_Thing>.

    This class comprises all persistent physical items of any size that are purposely created by human activity. This class comprises, besides others, human-made objects, such as a sword, and human-made features, such as rock art. For example, a “cup and ring” carving on bedrock is regarded as instance of E24 Physical Human-Made Thing.
    Instances of E24 Physical Human-Made Thing may be the result of modifying pre-existing physical things, preserving larger parts or most of the original matter and structure, which poses the question if they are new or even human-made, the respective interventions of production made on such original material should be obvious and sufficient to regard that the product has a new, distinct identity and intended function and is human-made. Substantial continuity of the previous matter and structure in the new product can be documented by describing the production process also as an instance of E81 Transformation.
    Whereas interventions of conservation and repair are not regarded to produce a new instance of E24 Physical Human-Made Thing, the results of preparation of natural history specimens that substantially change their natural or original state should be regarded as instances of E24 Physical Human-Made Things, including the uncovering of petrified biological features from a solid piece of stone. On the other side, scribbling a museum number on a natural object should not be regarded to make it human-made. This notwithstanding, parts, sections, segments, or features of an instance of E24 Physical Human-Made Thing may continue to be non-human-made and preserved during the production process, for example natural pearls used as a part of an eardrop.
    """
    depicts: list[CRMEntity] = []
    produced_by: list[Production] = []
    shows: list[VisualItem] = []
