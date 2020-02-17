# ==============================================================================
# brief        OANDA OrderReplace API Test
#              OANDA 注文置き換えAPIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.orders import OrderDetails, OrderReplace
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# 保留中となるオーダーを作成しておくこと
# -----------------------------

order_id = 103  # 作成したオーダーIDを指定

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# 保留中の注文情報を確認
ep = OrderDetails(accountID=ya.account_number, orderID=order_id)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# 保留中の注文を置き換える
data = {
    "order": {
        "price": 105.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "type": "LIMIT",
        "units": 10000,
        "type": "LIMIT",
        "positionFill": "DEFAULT",
        "tradeID": "103",
    },
}
ep = OrderReplace(accountID=ya.account_number, orderID=order_id,
                  data=data)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

