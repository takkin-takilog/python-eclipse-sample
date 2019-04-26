# ==============================================================================
# brief        OANDA Pricing Stream
#              リアルタイムで為替レート値を取得する。
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20.exceptions import V20Error
from fx import oanda_common as oc
from fx import your_account as ya


api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

params = {"instruments": "USD_JPY"}
ps = PricingStream(ya.account_number, params)

try:
    for rsp in api.request(ps):
        print("■リストの取得")
        print(json.dumps(rsp, indent=2))

        print("■bidsのみ抽出：")
        if "bids" in rsp.keys():
            print(rsp["bids"][0]["price"])


except V20Error as e:
    print("Error: {}".format(e))
