# ==============================================================================
# brief        OANDA OpenPositions API Test
#              OANDA オープンポジション取得APIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.positions import OpenPositions
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
