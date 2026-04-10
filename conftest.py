# -*- coding: utf-8 -*-
import pytest

from public.config import BASE_URL
from public.headers import get_headers
from public.request import ApiClient


@pytest.fixture(scope="session")
def base_url():
    """接口根地址，整个测试会话共享"""
    return BASE_URL


@pytest.fixture(scope="session")
def headers():
    """公共请求头，携带 Bearer token"""
    return get_headers()


@pytest.fixture(scope="session")
def client(base_url, headers):
    """会话级 ApiClient，自动打印请求/响应"""
    return ApiClient(base_url, headers)
