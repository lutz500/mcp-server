import httpx
from utils.logger import logger


class APIClient:
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.client = httpx.Client(timeout=self.timeout)

    def get(
        self, endpoint: str, params: dict = None, headers: dict = None
    ) -> dict | list | None:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.client.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            logger.info(f"GET {url} -> {data}")
            return data
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error for GET {url}: {e.response.status_code} - {e.response.text}"
            )
        except httpx.RequestError as e:
            logger.error(f"Request error for GET {url}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error for GET {url}: {e}")
        return None
