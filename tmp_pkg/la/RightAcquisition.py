from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .Transfer import Transfer

if TYPE_CHECKING:
    from ..crm.E30_Right import Right

class RightAcquisition(Transfer):
    """Right Acquisition <https://linked.art/ns/terms/RightAcquisition>.

    The acquiring or establishment of a particular E30 Right over some entity.
    """
    establishes: list[Right] = []
    invalidates: list[Right] = []
