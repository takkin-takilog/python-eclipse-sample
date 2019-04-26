# ==============================================================================
# brief        python OANDA サンプルコード
#
# author       たっきん
#
# pip install oandapyV20
# ==============================================================================

# ライブラリのインポート
import json

from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20.exceptions import V20Error

from fx import your_account as ya


class OANDA_ENV(object):
    """ OANDA_ENV - OANDA環境の定義クラス。
    パラメータ
    ----------
    PRACTICE : デモ口座
    LIVE     : 本講座
    """
    PRACTICE = "practice"
    LIVE = "live"


api = API(access_token=ya.access_token, environment=OANDA_ENV.PRACTICE)

instruments = "USD_JPY"

params = {"instruments": instruments}
ps = PricingStream(ya.account_number, params)

try:
    for rsp in api.request(ps):
        print("=================")
        print(json.dumps(rsp, indent=2))

        if "bids" in rsp.keys():
            print(rsp["bids"][0]["price"])


except V20Error as e:
    print("Error: {}".format(e))
