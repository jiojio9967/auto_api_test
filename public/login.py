# -*- coding: utf-8 -*-
import requests

from public.config import BASE_URL, LOGIN_MOBILE, LOGIN_PASSWORD, LOGIN_TYPE

_token_cache: str = ""


def get_token() -> str:
    """调用登录接口动态获取 token，同一进程内只请求一次（会话级缓存）"""
    global _token_cache
    if _token_cache:
        return _token_cache

    url = f"{BASE_URL}/xh-gather-app/open/member/login"
    body = {
        "mobile": LOGIN_MOBILE,
        "password": LOGIN_PASSWORD,
        "type": LOGIN_TYPE,
    }
    print(f"\n[login] 请求URL : {url}")
    print(f"[login] 请求体  : {body}")

    res = requests.post(url, json=body, headers={"Content-Type": "application/json"})
    print(f"[login] HTTP状态: {res.status_code}")
    print(f"[login] 响应内容: {res.text}")

    data = res.json()
    _token_cache = data["data"]["token"]
    return _token_cache
