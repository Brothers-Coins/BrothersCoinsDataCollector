from abc import ABCMeta

from src.model.date import Date
from src.model.transaction.type_transaction import TypeTransaction


class Transaction:
    __metaclass__ = ABCMeta  # define transaction abstract

    def __init__(self, id: int, value: int, player_name: str, date: Date):
        self.__id = id
        self.__value = value
        self.__player_name = player_name
        self.__date = date

    @property
    def transaction_object(self) -> dict:
        return {
            'id': self.__id,
            'value': self.__value,
            'player': self.__player_name,
            'date': self.__date.broken()
        }

    @property
    def id(self):
        return self.__id

    @property
    def type_transaction(self):
        return TypeTransaction.BUY_TRANSACTION if self.__value > 0 else TypeTransaction.SELL_TRANSACTION

    @property
    def value(self):
        return self.__value

    @property
    def abs_value(self):
        return abs(self.__value)

    @property
    def player_name(self):
        return self.__player_name

    def __gt__(self, other: "Transaction"):
        return self.abs_value > other.abs_value

    def __eq__(self, other):
        return self.abs_value == other.abs_value

    def __lt__(self, other):
        return self.abs_value < other.abs_value
