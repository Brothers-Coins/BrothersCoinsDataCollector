from typing import List
from src.controller.singleton import Singleton
from src.model.transaction.transaction import Transaction


class BankTransactions:
    __metaclass__ = Singleton

    def __init__(self, transactions: "List[Transaction]"):
        self.__transactions = transactions

    def add(self, transaction: Transaction):
        self.__transactions.append(transaction)

    @property
    def transactions(self) -> List["Transaction"]:
        return self.__transactions
