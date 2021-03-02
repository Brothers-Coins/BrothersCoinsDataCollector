from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup

from src.model.date.date import Date
from src.model.date.months import Months
from src.model.transaction.transaction import Transaction


class CrawlerPage:
    def __init__(self, cookies: dict, url: str, index_page: int):
        html = requests.get(url=url, cookies=cookies)
        print(f'Url requested for page {index_page}')
        self.__soup = BeautifulSoup(html.content, 'html.parser')

    @property
    def page_transactions(self) -> List["Transaction"]:
        all_tables = self.__soup.find_all("table")
        table = all_tables[6]
        table_rows = table.find_all("tr")[1:-1]
        return list(map(self.__html_to_object, table_rows))

    def __html_to_object(self, row: "BeautifulSoup") -> "Transaction":
        datas_of_row = row.find_all("td")
        id_transaction = self.__find_id(datas_of_row[0])
        date = self.__find_date(datas_of_row[1])
        value = self.__find_value_transaction(datas_of_row[-2])
        player_name = self.__find_player_name(datas_of_row[2], value)
        return Transaction(id_transaction, value, player_name, date)

    @staticmethod
    def __find_id(row_id: "BeautifulSoup") -> int:
        return int(row_id.next)

    @staticmethod
    def __find_date(row_date: "BeautifulSoup") -> "Date":
        navigable_string: str = row_date.next
        info_date = navigable_string.split()
        day = int(info_date[1])
        month = Months.months[info_date[0]]
        year = int(info_date[2][:-1])
        time = info_date[3]
        hours, minutes, seconds = map(int, time.split(':'))
        return Date(date=datetime(
            year=year,
            month=month,
            day=day,
            hour=hours,
            minute=minutes,
            second=seconds
        ))

    @staticmethod
    def __find_player_name(row_player: "BeautifulSoup", value: int) -> str:
        navigable_string: str = row_player.next
        infos_list = navigable_string.split()
        player_name = ' '.join(infos_list[infos_list.index('gifted') + 2:]) if value < 0 else ' '.join(
            infos_list[:infos_list.index('gifted')])
        return ' '.join(list(map(lambda name: name.capitalize(), player_name.split())))

    @staticmethod
    def __find_value_transaction(row_value: "BeautifulSoup") -> int:
        span_value = row_value.select_one('.ColorRed')
        if span_value is None:
            span_value = row_value.select_one('.ColorGreen')
        return int(span_value.next.replace(',', ''))
