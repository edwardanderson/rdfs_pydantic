from __future__ import annotations
from .._base import OptimizedBaseModel
from .E36_Visual_Item import VisualItem

class Mark(VisualItem):
    """Mark <http://www.cidoc-crm.org/cidoc-crm/E37_Mark>.

    This class comprises symbols, signs, signatures, or short texts applied to instances of E24 Physical Human-Made Thing by arbitrary techniques, often in order to indicate such things as creator, owner, dedications, purpose, or to communicate information generally. Instances of E37 Mark do not represent the actual image of a mark, but the abstract ideal (or archetype) as used for codification in reference documents forming cultural documentation.
    This class specifically excludes features that have no semantic significance, such as scratches or tool marks. These should be documented as instances of E25 Human-Made Feature.
    """
    ...
