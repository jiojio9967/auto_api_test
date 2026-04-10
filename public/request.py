# -*- coding: utf-8 -*-
import requests

from public.config import BASE_URL
from public.headers import get_headers


class ApiClient:
    """轻量 HTTP 客户端，基于 requests.Session 封装，自动打印请求/响应"""

    def __init__(self, base_url: str = BASE_URL, headers: dict = None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or get_headers())

    def _log(self, res: requests.Response) -> requests.Response:
        print(f"\n请求URL  : {res.request.url}")
        print(f"HTTP状态 : {res.status_code}")
        print(f"响应内容 : {res.text}")
        return res

    def get(self, path: str, **kwargs) -> requests.Response:
        res = self.session.get(f"{self.base_url}{path}", **kwargs)
        return self._log(res)

    def post(self, path: str, **kwargs) -> requests.Response:
        res = self.session.post(f"{self.base_url}{path}", **kwargs)
        return self._log(res)

    def put(self, path: str, **kwargs) -> requests.Response:
        res = self.session.put(f"{self.base_url}{path}", **kwargs)
        return self._log(res)

    def delete(self, path: str, **kwargs) -> requests.Response:
        res = self.session.delete(f"{self.base_url}{path}", **kwargs)
        return self._log(res)
