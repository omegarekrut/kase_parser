import requests
import re
from typing import Dict, Any

class KaseClient:
    BASE_URL: str = "https://kase.kz"
    CURRENCY_HISTORY_ENDPOINT: str = "/charts/currency/history"
    CURRENCY_PAGE: str = "/ru/currency/"

    def __init__(self) -> None:
        self.session: requests.Session = requests.Session()
        self.csrf_token: str = self._get_csrf_token()

    def _get_csrf_token(self) -> str:
        response: requests.Response = self.session.get(f"{self.BASE_URL}{self.CURRENCY_PAGE}")
        response.raise_for_status()

        csrf_token: str = response.cookies.get('__Host-csrftoken', '')

        if csrf_token:
            return csrf_token

        match: re.Match | None = re.search(r'name="csrf-token" content="(.*?)"', response.text)
        if match:
            return match.group(1)

        raise ValueError("CSRF token not found")

    def fetch_currency_data(
        self, 
        symbol: str, 
        resolution: str, 
        start_timestamp: int, 
        end_timestamp: int
    ) -> Dict[str, Any]:
        url: str = f"{self.BASE_URL}{self.CURRENCY_HISTORY_ENDPOINT}"
        headers: Dict[str, str] = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": self.csrf_token,
            "Origin": self.BASE_URL,
            "Referer": f"{self.BASE_URL}/ru/currency/"
        }
        payload: Dict[str, str] = {
            "symbol": symbol,
            "resolution": resolution,
            "from": str(start_timestamp),
            "to": str(end_timestamp),
            "chart_language_code": "ru"
        }

        response: requests.Response = self.session.post(url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()
