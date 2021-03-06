from time import sleep

from src.controller.file_manager import FileManager
from src.controller.crawler_page import CrawlerPage
from src.controller.singleton import Singleton
from src.model.transaction.bank_transactions import BankTransactions


class CrawlerManager:
    __metaclass__ = Singleton
    __base_url = "https://www.tibia.com/account/?subtopic=accountmanagement&page=tibiacoinshistory&currentpage="
    __cookies = FileManager.get_cookies()
    __wait_time = 5

    def __init__(self, file_transactions: BankTransactions):
        self.__bank_transactions = file_transactions
        self.__last_transaction_id = file_transactions.transactions[0].id

    @property
    def bank_transactions(self):
        return self.__bank_transactions

    @property
    def last_id(self):
        return self.__last_transaction_id

    def collect(self):
        page_counter = 1
        while True:
            try:
                end_crawler = self.__make_crawler_page(page_counter)
            except ValueError:  # Error to read page
                print(f'Error to read page, wait {CrawlerManager.__wait_time} seconds...')
                sleep(CrawlerManager.__wait_time)  # Wait for a new requisition
            else:
                if end_crawler:
                    break
                page_counter += 1

    def __make_crawler_page(self, page_counter: int) -> bool:
        crawler_page = CrawlerPage(CrawlerManager.__cookies, CrawlerManager.__base_url + str(page_counter),
                                   page_counter)
        transactions_page = crawler_page.page_transactions
        if not transactions_page:
            raise ValueError("A page's transaction list can never be empty")
        print(transactions_page)
        for transaction in transactions_page:
            if transaction.id == self.__last_transaction_id:
                return True
            self.__bank_transactions.add(transaction)
        return False
