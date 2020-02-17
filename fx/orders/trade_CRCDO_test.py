# ==============================================================================
# brief        OANDA TradeCRCDO API Test
#              OANDA トレード操作APIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.trades import TradeCRCDO
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# ポジションを保有しておく
# -----------------------------

trade_id = 110  # 作成したトレードIDを指定

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# ========== ex01 ==========
# 決済注文作成、置き換え
# ==========================
data01 = {
    "takeProfit": {
        "price": "150.000",
        "timeInForce": "GTC",
    },
    "stopLoss": {
        "price": "100.000",
        "timeInForce": "GTC",
    },
}

# ========== ex02 ==========
# 決済注文キャンセル
# ==========================
data02 = {
    "takeProfit": None,
    "stopLoss": None,
}

# トレード注文実行
ep = TradeCRCDO(accountID=ya.account_number, tradeID=trade_id, data=data02)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
