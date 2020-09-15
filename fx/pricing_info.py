# ==============================================================================
# brief        OANDA Pricing Stream
#              リアルタイムで為替レート値を取得する。
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import time
import json
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingInfo
from oandapyV20.exceptions import V20Error
from fx import oanda_common as oc
from fx import your_account as ya

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

params = {"instruments": "USD_JPY,EUR_JPY,EUR_USD"}
pi = PricingInfo(ya.account_number, params)

try:
    while True:
        rsp = api.request(pi)
        print("■リストの取得")
        print(json.dumps(rsp, indent=2))
        time.sleep(1)

except V20Error as e:
    print("Error: {}".format(e))
