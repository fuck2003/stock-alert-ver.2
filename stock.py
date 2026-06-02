import requests
import os
from datetime import datetime


API_KEY = os.environ["FINNHUB_KEY"]
DINGTALK_WEBHOOK = os.environ["DINGTALK_WEBHOOK"]

WATCH_LIST = {
    "TSLA": 1
}

for symbol, target in WATCH_LIST.items():

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"

    data = requests.get(url).json()

    price = data.get("c", 0)

    print(symbol, price)

    if price > target:

        msg = {
            "msgtype": "text",
            "text": {
                "content":
                f"【K股票预警】\n"
                f"股票：{symbol}\n"
                f"当前价格：{price}\n"
                f"触发条件：>{target}"
            }
        }

        

        requests.post(
            DINGTALK_WEBHOOK,
            json=msg
        )

f"时间：{datetime.now()}\n"
