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
from oandapyV20.endpoints.positions import OpenPositions, PositionList
from oandapyV20.endpoints.positions import PositionClose
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# ポジションを保有しておく
# -----------------------------

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# オープン中の全ポジションリストを取得する
ep = OpenPositions(accountID=ya.account_number)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# ポジションをクローズする
data = {
    "longUnits": "ALL",
    "shortUnits": "ALL"
    }
ep = PositionClose(accountID=ya.account_number,
                   instrument="USD_JPY", data=data)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# オープン中の全ポジションリストを取得する
ep = OpenPositions(accountID=ya.account_number)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# ポジションリストを取得する
ep = PositionList(accountID=ya.account_number)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
