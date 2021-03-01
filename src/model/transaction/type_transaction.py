from enum import Enum


class TypeTransaction(Enum):
    """
    BUY and SELL are in perspective of player
    """
    BUY_TRANSACTION = 1
    SELL_TRANSACTION = -1
