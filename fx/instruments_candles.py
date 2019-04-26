# ==============================================================================
# brief        OANDA Instruments Candles
#              指定された日時のローソク足情報を取得する。
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import datetime
import json
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya
import oandapyV20.endpoints.instruments as instruments
import pandas as pd


api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)

fmt = "%Y-%m-%dT%H:%M:00.000000000Z"
# 2015年9月15日のローソク足情報を取得
_from = datetime.datetime(year=2015, month=9, day=15,
                          hour=12, minute=0, second=0).strftime(fmt)

params = {
    "alignmentTimezone": "Japan",
    'from': _from,
    "count": 24,  # 取得数24
    "granularity": oc.OandaGrn.H1  # 1時間足
}

# APIへ過去データをリクエスト
ic = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
api.request(ic)

# リストへ入れ替える
data = []
for raw in ic.response['candles']:
    data.append([raw['time'], raw['volume'], raw['mid']['o'],
                 raw['mid']['h'], raw['mid']['l'], raw['mid']['c']])

# リストからデータフレームへ変換
df = pd.DataFrame(data)
df.columns = ['time', 'volume', 'open', 'high', 'low', 'close']
df = df.set_index('time')

# date型を整形する
df.index = pd.to_datetime(df.index)
print(df.tail(25))

# レスポンス生データ表示
# print(json.dumps(ic.response, indent=2))
