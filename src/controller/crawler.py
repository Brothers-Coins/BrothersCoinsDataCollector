from src.controller.file_manager import FileManager
from src.model.crawler_page import CrawlerPage
from src.model.singleton import Singleton
from src.model.transaction.bank_transactions import BankTransactions


class CrawlerManager:
    __metaclass__ = Singleton
    __base_url = "https://www.tibia.com/account/?subtopic=accountmanagement&page=tibiacoinshistory&currentpage="

    def __init__(self, file_transactions: BankTransactions):
        self.__bank_transactions = file_transactions
        self.__last_id = file_transactions.transactions[-1].id

    @property
    def bank_transactions(self):
        return self.__bank_transactions

    def collect(self):
        page_counter = 1
        while True:
            end_crawler = self.__make_crawler_page(page_counter)
            if end_crawler:
                break
            page_counter += 1

    def __make_crawler_page(self, page_counter: int) -> bool:
        end_crawler = False
        cookies = FileManager.get_cookies()
        crawler_page = CrawlerPage(cookies, CrawlerManager.__base_url + str(page_counter))
        for transaction in crawler_page.transactions:
            if transaction.id == self.__last_id:
                end_crawler = True
            self.__bank_transactions.add(transaction)
        return end_crawler