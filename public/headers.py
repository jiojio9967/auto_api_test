import time

def get_headers():
    return {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "*/*",

        # 👉 直接用你抓到的
        "authorization": "vlSnpS/XrYjrWZVApxLyHUaLHyjyEg1c1yRWACIsP0iHRTtcqDMqNNECF4c71sbkkVSwa58PW1bwcxFPDDr3FNzeJTNdejqH8cFYMrxId1b7oI3Ec2GDsv/eEWACjuBb",

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