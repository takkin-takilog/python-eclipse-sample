# ==============================================================================
# brief        ローソク足チャートの描写
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
#     Bokehのインストール（conda install bokeh）
# ==============================================================================

import datetime
from math import pi

from bokeh.plotting import figure, show, output_file
from oandapyV20 import API

from fx import oanda_common as oc
from fx import your_account as ya
import oandapyV20.endpoints.instruments as instruments
import pandas as pd


class CandleStick(object):
    """ CandleStick - ローソク足定義クラス。"""

    def __init__(self):
        """"コンストラクタ
        引数：
            なし
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

        self.__api = API(access_token=ya.access_token,
                         environment=oc.OANDA_ENV.PRACTICE)

    def drawCandleStick(self, instrument, datetime_from, datetime_to,
                        granularity):

        params = {
            "alignmentTimezone": "Japan",
            "from": datetime_from,
            "to": datetime_to,
            "granularity": granularity
        }

        # APIへ過去データをリクエスト
        ic = instruments.InstrumentsCandles(instrument=instrument,
                                            params=params)
        self.__api.request(ic)

        self.__data = []
        for raw in ic.response[self.__CANDLES]:
            self.__data.append([raw[self.__TIME],
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

        inc = df[self.__CLOSE] > df[self.__OPEN]
        dec = df[self.__OPEN] > df[self.__CLOSE]
        equ = df[self.__CLOSE] == df[self.__OPEN]
        w = 12 * 60 * 60 * 1000  # half day in ms

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

        p = figure(x_axis_type="datetime", tools=TOOLS,
                   plot_width=1000, title="MSFT Candlestick")
        p.xaxis.major_label_orientation = pi / 4
        p.grid.grid_line_alpha = 0.3

        p.segment(df.index, df[self.__HIGHT], df.index,
                  df[self.__LOW], color="black")
        p.vbar(df.index[inc], w, df[self.__OPEN][inc], df[self.__CLOSE][inc],
               fill_color="#CD360D", line_color="black")
        p.vbar(df.index[dec], w, df[self.__OPEN][dec], df[self.__CLOSE][dec],
               fill_color="#296FBC", line_color="black")
        p.vbar(df.index[equ], w, df[self.__OPEN][equ], df[self.__CLOSE][equ],
               fill_color="#FFEE77", line_color="black")

        output_file("candlestick.html", title="candlestick.py example")

        show(p)  # open a browser


if __name__ == "__main__":
    cs = CandleStick()

    fmt = '%Y-%m-%dT%H:%M:00.000000Z'

    instrument = oc.OANDA_INS.USD_JPY
    datetime_from = datetime.datetime(year=2018, month=9, day=12, hour=12,
                                      minute=0, second=0).strftime(fmt)
    datetime_to = datetime.datetime(year=2018, month=12, day=15, hour=12,
                                    minute=0, second=0).strftime(fmt)
    granularity = oc.OANDA_GRN.D
    cs.drawCandleStick(instrument, datetime_from, datetime_to,
                       granularity)
