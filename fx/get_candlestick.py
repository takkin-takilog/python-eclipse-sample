# ==============================================================================
# brief        ローソク足チャートの取得
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import datetime
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya
import oandapyV20.endpoints.instruments as instruments
import pandas as pd
from oandapyV20.exceptions import V20Error


class CandleStick(object):
    """ CandleStick - ローソク足定義クラス。"""

    def __init__(self, granularity):
        """"コンストラクタ
        引数:
            dt (str): datetime formatted by DT_FMT.
        戻り値:
            tf_dt (str): changed datetime.
        """

        self.__CANDLES = "candles"
        self.__MID = "mid"
        self.__O = "o"
        self.__H = "h"
        self.__L = "l"
        self.__C = "c"

        self.__TIME = "time"
        self.__VOLUME = "volume"
        self.__OPEN = "open"
        self.__HIGHT = "high"
        self.__LOW = "low"
        self.__CLOSE = "close"

        self.__DT_FMT = "%Y-%m-%dT%H:%M:00.000000000Z"
        self.__GRANULARITY = granularity

        self.__df = []

        self.__api = API(access_token=ya.access_token,
                         environment=oc.OandaEnv.PRACTICE)

    def getInstrumentsCandles(self, instrument, dt_from, dt_to):

        TMDLT = datetime.timedelta(hours=9)

        DT_FMT = "%Y-%m-%dT%H:%M:10.000000Z"
        dt_from_str = (dt_from - TMDLT).strftime(DT_FMT)
        dt_to_str = (dt_to - TMDLT).strftime(DT_FMT)

        print("from: {}" .format(dt_from_str))
        print("to  : {}" .format(dt_to_str))
        print("------------------------------------------")

        params = {
            "from": dt_from_str,
            "to": dt_to_str,
            "granularity": self.__GRANULARITY,
            "price": "ABM"
        }

        # APIへ過去データをリクエスト
        ic = instruments.InstrumentsCandles(instrument=instrument,
                                            params=params)

        flg = True
        while flg:
            try:
                print(datetime.datetime.now())
                res = self.__api.request(ic)
            except V20Error as err:
                print(err)
            else:
                flg = False

        self.__data = []
        for raw in res[self.__CANDLES]:
            self.__data.append([self.__changeDateTimeFmt(raw[self.__TIME]),
                                raw[self.__VOLUME],
                                raw[self.__MID][self.__O],
                                raw[self.__MID][self.__H],
                                raw[self.__MID][self.__L],
                                raw[self.__MID][self.__C]])
        # リストからデータフレームへ変換
        df = pd.DataFrame(self.__data)

        df.columns = [self.__TIME,
                      self.__VOLUME,
                      self.__OPEN,
                      self.__HIGHT,
                      self.__LOW,
                      self.__CLOSE]
        df = df.set_index(self.__TIME)
        # date型を整形する
        df.index = pd.to_datetime(df.index)

        print(df)

    def __changeDateTimeFmt(self, dt):
        """"日付フォーマットの変換メソッド
        引数:
            dt (str): DT_FMT形式でフォーマットされた日付
        戻り値:
            tf_dt (str): 変換後の日付
        """
        TMDLT = datetime.timedelta(hours=9)

        tf_dt = datetime.datetime.strptime(dt, self.__DT_FMT) + TMDLT

        return tf_dt


if __name__ == "__main__":
    cs = CandleStick(oc.OandaGrn.M1)

    instrument = oc.OandaIns.USD_JPY

    dlt = datetime.timedelta(minutes=1)
    dt_from = datetime.datetime.now()
    dt_to = dt_from + dlt

    cs.getInstrumentsCandles(instrument, dt_from, dt_to)
