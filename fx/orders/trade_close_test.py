# ==============================================================================
# brief        OANDA TradeClose API Test
#              OANDA トレード決済APIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.trades import TradeDetails, TradeClose
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# ポジションを保有しておく
# -----------------------------

trade_id = 143  # 作成したトレードIDを指定

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# トレード詳細を取得
ep = TradeDetails(accountID=ya.account_number, tradeID=trade_id)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# ========== ex01 ==========
# トレード全決済
# ==========================
data01 = None

# ========== ex02 ==========
# トレード一部決済
# ==========================
data02 = {
    "units": "30"
}

data = data01
# data = data02

# トレード注文実行
ep = TradeClose(accountID=ya.account_number, tradeID=trade_id, data=data)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
