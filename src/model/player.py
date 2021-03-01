from typing import List

from src.model.transaction.type_transaction import TypeTransaction


class Player:
    def __init__(self, name: str, transactions: List = None):
        self.__transactions = [] if transactions is None else transactions
        self.__name = name

    def __get_transactions_by_type(self, type_transaction: TypeTransaction):
        return list(filter(lambda transaction: transaction.type_transaction is type_transaction,
                           self.__transactions))

    @property
    def name(self):
        return self.__name

    @property
    def buy_transactions(self):
        return self.__get_transactions_by_type(TypeTransaction.BUY_TRANSACTION)

    @property
    def sell_transactions(self):
        return self.__get_transactions_by_type(TypeTransaction.SELL_TRANSACTION)

    @property
    def max_transaction_sell(self):
        return max(self.sell_transactions)

    @property
    def max_transaction_buy(self):
        return min(self.buy_transactions)

    def __eq__(self, other: "Player"):
        return self.__name == other.name
