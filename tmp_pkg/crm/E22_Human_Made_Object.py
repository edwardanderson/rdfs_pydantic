from __future__ import annotations
from .._base import OptimizedBaseModel
from .E19_Physical_Object import PhysicalObject
from .E24_Physical_Human_Made_Thing import PhysicalHumanMadeThing

class HumanMadeObject(PhysicalHumanMadeThing, PhysicalObject):
    """Human-Made Object <http://www.cidoc-crm.org/cidoc-crm/E22_Human-Made_Object>.

    This class comprises all persistent physical objects of any size that are purposely created by human activity and have physical boundaries that separate them completely in an objective way from other objects.
    The class also includes all aggregates of objects made for functional purposes of whatever kind, independent of physical coherence, such as a set of chessmen.
    """
    ...
