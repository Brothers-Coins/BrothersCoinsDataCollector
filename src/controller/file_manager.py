import json
from abc import ABC
from typing import List

from src.model.transaction.transaction import Transaction


class FileManager:
    __metaclass__ = ABC
    __transactions_path = '../data/transactions_a.json'

    @staticmethod
    def get_cookies() -> dict:
        with open('../data/secure_session_id.txt') as arq:
            return {
                'SecureSessionID': arq.readline()
            }

    @staticmethod
    def get_transactions():
        with open(FileManager.__transactions_path, encoding='utf8') as arq:
            return json.load(arq)["transactions"]

    @staticmethod
    def save_transactions(transactions: List["Transaction"]):
        with open(FileManager.__transactions_path, 'w', encoding='utf8') as arq:
            json.dump({"transactions": list(map(FileManager.serialize, transactions))}, arq)

    @staticmethod
    def serialize(transaction: "Transaction") -> dict:
        return transaction.broken()
