# ==============================================================================
# brief        OANDA Accounts
#              口座情報を取得する。
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
from oandapyV20.exceptions import V20Error
from fx import oanda_common as oc
from fx import your_account as ya


api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
r = accounts.AccountSummary(ya.account_number)

try:
    rsp = api.request(r)
    print(json.dumps(rsp, indent=2))
except V20Error as e:
    print("Error: {}".format(e))
