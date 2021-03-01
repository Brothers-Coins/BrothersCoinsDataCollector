from typing import List

import requests
from bs4 import BeautifulSoup

from src.model.transaction.transaction import Transaction


class CrawlerPage:
    def __init__(self, cookies: dict, url: str):
        html = requests.get(url=url, cookies=cookies)
        self._soup = BeautifulSoup(html.content, 'html.parser')

    @property
    def transactions(self) -> List["Transaction"]:
        # TODO: SCRAPPER DA TABLEA DA PÁGINA
        return []