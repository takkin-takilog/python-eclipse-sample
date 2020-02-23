# ==============================================================================
# brief        OANDA PositionDetails API Test
#              OANDA ポジション詳細取得APIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.positions import PositionDetails
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# ポジションを保有しておく
# -----------------------------

instrument = "USD_JPY"

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
ep = PositionDetails(accountID=ya.account_number, instrument=instrument)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
