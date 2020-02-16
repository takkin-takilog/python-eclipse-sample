# ==============================================================================
# brief        OANDA OrderCancel API Test
#              OANDA 注文キャンセルAPIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.orders import OrderDetails, OrderCancel
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ----------事前準備 ----------
# 保留中となるオーダーを作成しておくこと
# -----------------------------

order_id = 10  # 作成したオーダーIDを指定

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

# 保留中の注文情報を確認
ep = OrderDetails(accountID=ya.account_number, orderID=order_id)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# 保留中の注文をキャンセルする
ep = OrderCancel(accountID=ya.account_number, orderID=order_id)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))

# 保留中の注文情報を再度確認
ep = OrderDetails(accountID=ya.account_number, orderID=order_id)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
