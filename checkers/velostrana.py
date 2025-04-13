import json

from checkers.base import BaseChecker
from bs4 import BeautifulSoup
from requests import Session



class VelostranaChecker(BaseChecker):
    URL = "https://www.velostrana.ru/aspect/covenant/"
    _session: Session

    @staticmethod
    def _parse_html_document(document: str) -> bool:
        soup = BeautifulSoup(document, "html.parser")
        script_tag = soup.find_all("script", {"type": "application/ld+json"})
        if not script_tag:
            return False

        avail = False
        for script in script_tag:
            # Пытаемся загрузить JSON из содержимого тега
            try:
                data = json.loads(script.string)
            except json.JSONDecodeError as e:
                raise ValueError("Ошибка декодирования JSON.") from e

            # Извлекаем данные о предложениях
            offers = data.get("offers", {})
            availability = offers.get("availability", "")
            avail = availability == "https://schema.org/InStock"
        return avail