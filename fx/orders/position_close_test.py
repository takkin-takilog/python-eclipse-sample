# ==============================================================================
# brief        OANDA PositionClose API Test
#              OANDA ポジションクローズAPIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.positions import OpenPositions, PositionClose
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# ポジションを保有しておく
# -----------------------------

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# オープン中の全ポジション情報を取得する
print("①オープン中の全ポジション情報を取得（決済前）")
ep = OpenPositions(accountID=ya.account_number)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# ポジションをクローズする
data = {
    "longUnits": "400",
    "shortUnits": "ALL"
}

print("②ポジションをクローズ")
ep = PositionClose(accountID=ya.account_number,
                   instrument="USD_JPY", data=data)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# オープン中の全ポジション情報を取得する
print("③オープン中の全ポジション情報を取得（決済後）")
ep = OpenPositions(accountID=ya.account_number)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
