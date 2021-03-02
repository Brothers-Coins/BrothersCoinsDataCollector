from src.controller.crawler_manager import CrawlerManager
from src.controller.file_manager import FileManager
from src.controller.singleton import Singleton
from src.model.date.date import Date
from src.model.transaction.bank_transactions import BankTransactions
from src.model.transaction.transaction import Transaction


class Manager:
    __metaclass__ = Singleton

    def __init__(self):
        self.__crawler_manager = CrawlerManager(self.__convert_file_transctions_to_transactions())

    @staticmethod
    def __convert_file_transctions_to_transactions() -> BankTransactions:
        list_json_transactions = FileManager.get_transactions()
        return BankTransactions([
            Transaction(transaction["id"], transaction["value"], transaction["player"], Date(date_dict=transaction["date"]))
            for transaction in list_json_transactions
        ])

    def get_transactions(self):
        self.__crawler_manager.collect()
        transactions = self.__crawler_manager.bank_transactions.transactions
        FileManager.save_transactions(transactions)
        return transactions

