import time

def get_headers():
    return {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "*/*",

        # 👉 直接用你抓到的
        "authorization": "vlSnpS/XrYjrWZVApxLyHb9MJD5Yw1rV8RHF2SUlu86PYUMDqKVbGLnC4Y6LUkNYO5Rfq0PgjV7uP1MpSaQB5Eri0pVLOEzrYAgKmq1LSLDxNK5jyIt8AQnX77FrkVah",

        "deviceid": "7C519352-1132-40C3-B9B2-2750D8EFAD11",
        "source": "IOS",
        "version": "150",
        "language": "cn",
        "rateunit": "USD",

        # 👉 动态时间
        "timestamp": str(int(time.time() * 1000)),

        "User-Agent": "chain/150 CFNetwork/1335.0.3.4 Darwin/21.6.0",

        # 👉 先写死（后面再讲算法）
        "sign": "0d6f25aee0179f30befa51951114de8d"
    }