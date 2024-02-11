import logging
import re

import requests
from bs4 import BeautifulSoup as bs


class CurrencyScraper:
    """Класс для получения и обработки данных о курсах валют с сайта Центробанка России."""

    def __init__(self) -> None:
        self.url = "https://www.cbr.ru/currency_base/daily/"
        try:
            self.requests = requests.get(self.url)
            self.soup = bs(self.requests.text, "lxml")
        except requests.exceptions.ConnectionError:
            logging.error("Не удалось установить соединение.")

    def _get_exchange_rate(self, index: int) -> str:
        """Внутренний метод для получения значения валюты по индексу."""
        currency = list(self.soup.find_all("tr")[index])[9].text
        return currency if currency else None

    def get_usd_rate(self) -> str:
        """Получение курса доллара США."""
        return self._get_exchange_rate(14)

    def get_eur_rate(self) -> str:
        """Получение курса евро."""
        return self._get_exchange_rate(15)

    def get_kzt_rate(self) -> str:
        """Получение курса казахстанского тенге."""
        return self._get_exchange_rate(19)

    def get_cny_rate(self) -> str:
        """Получение курса китайского юаня."""
        return self._get_exchange_rate(23)

    def get_uah_rate(self) -> str:
        """Получение курса украинской гривны."""
        return self._get_exchange_rate(37)

    @staticmethod
    def _format_currency(currency: str) -> float:
        """Внутренний метод для форматирования строки с курсом валюты."""
        return float(currency.replace(",", "."))

    @staticmethod
    def _format_number(num: float) -> str:
        """Внутренний метод для форматирования числа с разделителем тысяч."""
        result = "{0:,.1f}".format(round(num, 1))
        formatted_result = re.sub(
            r"[,\.]", lambda m: "," if m.group() == "." else " ", result
        )
        return formatted_result

    def convert(
        self, currency_1: str, currency_2: str, multiplication: bool = True
    ) -> str:
        """Выполнение расчета между двумя валютами."""
        currency_1 = self._format_currency(currency_1)
        currency_2 = self._format_currency(currency_2)

        if multiplication:
            total = currency_1 * currency_2
        else:
            if currency_2 != 0:
                total = currency_1 / currency_2
            else:
                raise ValueError("Деление на ноль недопустимо.")

        result = self._format_number(total)
        return result
