import json

from checkers.base import BaseChecker
from bs4 import BeautifulSoup
from requests import Session



class VeloskladChecker(BaseChecker):
    URL = "https://www.velosklad.ru/velosipedy/poiskall/?text=aspect+covenant"
    _session: Session

    @staticmethod
    def _parse_html_document(document: str) -> bool:
        soup = BeautifulSoup(document, "html.parser")
        script_tag = soup.find("script", {"class": "catalogue-list__item"})
        if not script_tag:
            return False

        if "covenant" in script_tag.text:
            return True
        return False