import os
import time


# 默认值从 Charles 抓包得到，仅作为本地兜底；正式使用请通过环境变量覆盖。
_DEFAULT_AUTH_TOKEN = (
    "vlSnpS/XrYjrWZVApxLyHb9MJD5Yw1rV8RHF2SUlu86PYUMDqKVbGLnC4Y6LUkNYO5Rfq0PgjV7"
    "uP1MpSaQB5Eri0pVLOEzrYAgKmq1LSLDxNK5jyIt8AQnX77FrkVah"
)
_DEFAULT_SIGN = "0d6f25aee0179f30befa51951114de8d"


def _get_token() -> str:
    """优先读取环境变量 API_TOKEN，找不到再回退到本地默认值。"""
    return os.getenv("API_TOKEN") or _DEFAULT_AUTH_TOKEN


def _get_sign() -> str:
    """优先读取环境变量 API_SIGN，找不到再回退到本地默认值。"""
    return os.getenv("API_SIGN") or _DEFAULT_SIGN


def get_headers():
    return {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "*/*",

        # 优先来自 API_TOKEN 环境变量；没有则使用默认抓包 token
        "authorization": _get_token(),

        "deviceid": "7C519352-1132-40C3-B9B2-2750D8EFAD11",
        "source": "IOS",
        "version": "150",
        "language": "cn",
        "rateunit": "USD",

        # 动态时间戳
        "timestamp": str(int(time.time() * 1000)),

        "User-Agent": "chain/150 CFNetwork/1335.0.3.4 Darwin/21.6.0",

        # 优先来自 API_SIGN 环境变量；没有则使用默认抓包 sign
        "sign": _get_sign(),
    }
