from __future__ import annotations
from typing import TYPE_CHECKING
from .._base import OptimizedBaseModel
from .E54_Dimension import Dimension

if TYPE_CHECKING:
    from .E96_Purchase import Purchase
    from .E98_Currency import Currency

class MonetaryAmount(Dimension):
    """Monetary Amount <http://www.cidoc-crm.org/cidoc-crm/E97_Monetary_Amount>.

    This class comprises quantities of monetary possessions or obligations in terms of their nominal value with respect to a particular currency. These quantities may be abstract accounting units, the nominal value of a heap of coins or bank notes at the time of validity of the respective currency, the nominal value of a bill of exchange or other documents expressing monetary claims or obligations. It specifically excludes amounts expressed in terms of weights of valuable items, like gold and diamonds, and quantities of other non-currency items, like goats or stocks and bonds.
    """
    currency: list[Currency] = []
    sales_price_of: list[Purchase] = []
