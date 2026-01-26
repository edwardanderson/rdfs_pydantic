from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .Transfer import Transfer

if TYPE_CHECKING:
    from ..crm.E39_Actor import Actor
    from ..crm.E97_Monetary_Amount import MonetaryAmount

class Payment(Transfer):
    """Payment <https://linked.art/ns/terms/Payment>.

    Payment of Money.
    """
    paid_amount: list[MonetaryAmount] = []
    paid_from: list[Actor] = []
    paid_to: list[Actor] = []
