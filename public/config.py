import time

# 基础地址
BASE_URL = "https://api-test.528btc.com.cn"

# 🔥 你抓包的token（先写死，后面再优化）
TOKEN = "vlSnpS/XrYjrWZVApxLyHUaLHyjyEg1c1yRWACIsP0iHRTtcqDMqNNECF4c71sbkkVSwa58PW1bwcxFPDDr3FNzeJTNdejqH8cFYMrxId1b7oI3Ec2GDsv/eEWACjuBb"

# 🔥 sign先写死（后面可以做自动生成）
SIGN = "0d6f25aee0179f30befa51951114de8d"

def get_timestamp():
    return str(int(time.time() * 1000))

def get_token():
    return TOKEN