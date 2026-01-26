from __future__ import annotations
from .._base import OptimizedBaseModel
from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing
from .E26_Physical_Feature import PhysicalFeature

class HumanMadeFeature(PhysicalFeature, PhysicalHumanMadeThing):
    """Human-Made Feature <http://www.cidoc-crm.org/cidoc-crm/E25_Human-Made_Feature>.

    This class comprises physical features that are purposely created by human activity, such as scratches, artificial caves, artificial water channels, etc. In particular, it includes the information encoding features on mechanical or digital carriers.
    """
    ...
