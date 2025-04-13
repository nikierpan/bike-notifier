import requests

class Notifier:
    _TOKEN: str
    _URL: str = "https://api.telegram.org/bot{token}/sendMessage"
    _chat_id: str

    def __init__(self, token: str, chat_id: str) -> None:
        self._TOKEN = token
        self._chat_id = chat_id

    def send_message(self, message: str, silent: bool = False) -> None:
        url = self._URL.format(token=self._TOKEN)

        payload = {
            "chat_id": self._chat_id,
            "text": message
        }

        if silent:
            payload["disable_notification"] = True

        response = requests.post(url, data=payload)
        # Проверка успешности запроса
        if response.status_code != 200:
            raise Exception(f"Ошибка отправки сообщения: {response.text}")
        return response.json()