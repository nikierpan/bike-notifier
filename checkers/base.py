import requests

from requests import Session



class BaseChecker:
    _session: Session

    def __init__(self):
        self._session = requests.Session()


    def _load_html_document(self,) -> str:
        headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/115.0.0.0 Safari/537.36"),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        res = self._session.get(self.URL, headers=headers)
        res.raise_for_status()
        return res.text

    @staticmethod
    def _parse_html_document(document: str) -> bool:
        pass

    def check_availability(self) -> bool:
        document = self._load_html_document()
        return self._parse_html_document(document)