import requests
import json
from utils.config_reader import get_config

class BaseApi:
    def __init__(self):
        self.base_url = get_config('env', 'base_url')
        self.session = requests.Session()
        self.default_timeout = float(get_config('timeout', 'default'))
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def send_request(self, method, endpoint, **kwargs):
        """
        統一發送請求的核心方法
        """
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.default_timeout)
        try:
            response = self.session.request(method, url, **kwargs)
            print(f"\n{'=' * 50}")
            print(f"[Request] {method} {url}")
            if 'json' in kwargs:
                print(f"[Payload] {json.dumps(kwargs['json'], indent=2)}")
            print(f"[Status] {response.status_code}")
            if response.status_code != 200 and response.status_code != 201:
                print(f"[Error Response] {response.text[:200]}...")

            print(f"{'=' * 50}")

            return response
        except Exception as e:
            print(f"!!! Network Error: {e}")
            raise e

    def get(self, endpoint, **kwargs):
        return self.send_request("GET", endpoint, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.send_request("POST", endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self.send_request("PUT", endpoint, data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.send_request("DELETE", endpoint, **kwargs)