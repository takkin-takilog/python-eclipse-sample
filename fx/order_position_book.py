# ==============================================================================
# brief        オープンオーダー、オープンポジションの描写
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
#     Bokehのインストール（conda install bokeh）
# ==============================================================================

import copy
import datetime
from bokeh.plotting import figure, show
from oandapyV20 import API
from bokeh.layouts import gridplot
from datetime import timedelta

from bokehlib import bokeh_common as bc
from fx import oanda_common as oc
from fx import your_account as ya
import oandapyV20.endpoints.instruments as instruments
import pandas as pd


class OrderBook(object):
    """ OrderBook - オーダーブック定義クラス。"""

    def __init__(self, granularity):
        """"コンストラクタ"""

        self.__BUCKETS = "buckets"

        self.__ORD_BOOK = "orderBook"
        self.__PSI_BOOK = "positionBook"
        self.__PRICE = "price"
        self.__LONG = "longCountPercent"
        self.__SHORT = "shortCountPercent"

        self.__TIME = "time"
        self.__CUR_PRICE = "price"
        self.__BUCKET_WIDTH = "bucketWidth"

        self.__WIDE = 12 * 60 * 60 * 1000  # half day in ms
        self.__WIDE_SCALE = 0.2

        self.__DT_FMT = "%Y-%m-%dT%H:%M:00Z"
        self.__GRANULARITY = granularity

        self.__CUT_TH = 50  # 現レートから上下何本残すか
        self.__X_AXIS_MAX = 2.5  # X軸レンジ

        self.__BG_COLOR = "#2e2e2e"
        self.__BAR_R_COLOR = "#00A4BD"
        self.__BAR_L_COLOR = "#FF8400"
        self.__CURPRI_COLOR = "#7DA900"

        self.__ord_df = []
        self.__ord_curpri = 0

        self.__psi_df = []
        self.__psi_curpri = 0

        self.__api = API(access_token=ya.access_token,
                         environment=oc.OandaEnv.PRACTICE)

    def getInstrumentsOrderBook(self, instrument, dt):

        params = {
            "time": dt.strftime(self.__DT_FMT),
        }

        # APIへ過去データをリクエスト
        ic = instruments.InstrumentsOrderBook(instrument=instrument,
                                              params=params)
        self.__api.request(ic)

        self.__data = []
        for raw in ic.response[self.__ORD_BOOK][self.__BUCKETS]:
            self.__data.append([float(raw[self.__PRICE]),
                                float(raw[self.__LONG]),
                                float(raw[self.__SHORT])])

        # リストからデータフレームへ変換
        df = pd.DataFrame(self.__data)
        df.columns = [self.__PRICE,
                      self.__LONG,
                      self.__SHORT]
        df = df.set_index(self.__PRICE).sort_index(ascending=False)
        # date型を整形する
        time = pd.to_datetime(self.__changeDateTimeFmt(
            ic.response[self.__ORD_BOOK][self.__TIME]))
        cur_price = float(ic.response[self.__ORD_BOOK][self.__CUR_PRICE])
        bucket_width = float(ic.response[self.__ORD_BOOK][self.__BUCKET_WIDTH])

        print(df)
        print(bucket_width)

        print(time)
        print(cur_price)
        idx_th = bucket_width * self.__CUT_TH
        self.__ord_df = df[(df.index > cur_price - idx_th)
                           & (df.index < cur_price + idx_th)]
        self.__ord_curpri = cur_price

    def getInstrumentsPositionBook(self, instrument, dt):

        params = {
            "time": dt.strftime(self.__DT_FMT),
        }

        # APIへ過去データをリクエスト
        ic = instruments.InstrumentsPositionBook(instrument=instrument,
                                                 params=params)
        self.__api.request(ic)

        self.__data = []
        for raw in ic.response[self.__PSI_BOOK][self.__BUCKETS]:
            self.__data.append([float(raw[self.__PRICE]),
                                float(raw[self.__LONG]),
                                float(raw[self.__SHORT])])

        # リストからデータフレームへ変換
        df = pd.DataFrame(self.__data)
        df.columns = [self.__PRICE,
                      self.__LONG,
                      self.__SHORT]
        df = df.set_index(self.__PRICE).sort_index(ascending=False)
        # date型を整形する
        time = pd.to_datetime(self.__changeDateTimeFmt(
            ic.response[self.__PSI_BOOK][self.__TIME]))
        cur_price = float(ic.response[self.__PSI_BOOK][self.__CUR_PRICE])
        bucket_width = float(ic.response[self.__PSI_BOOK][self.__BUCKET_WIDTH])

        print(df)
        print(bucket_width)

        print(time)
        print(cur_price)
        idx_th = bucket_width * self.__CUT_TH
        self.__psi_df = df[(df.index > cur_price - idx_th)
                           & (df.index < cur_price + idx_th)]
        self.__psi_curpri = cur_price

    def drawPositionOrderBook(self, fig_width=500):

        set_tools = bc.ToolType.gen_str(bc.ToolType.XPAN,
                                        bc.ToolType.WHEEL_ZOOM,
                                        bc.ToolType.BOX_ZOOM,
                                        bc.ToolType.RESET,
                                        bc.ToolType.SAVE)

        df = copy.copy(self.__ord_df)
        # --------------- メインfigure ---------------
        plt1 = figure(
            plot_height=fig_width,
            plot_width=fig_width,
            x_range=(-self.__X_AXIS_MAX, self.__X_AXIS_MAX),
            tools=set_tools,
            title="Order Book example",
            background_fill_color=self.__BG_COLOR
        )
        plt1.grid.grid_line_alpha = 0.3

        df_up = df[self.__LONG][(df.index > self.__ord_curpri)]
        df_lo = -df[self.__SHORT][(df.index < self.__ord_curpri)]
        df_right = pd.concat([df_up, df_lo])

        df_up = -df[self.__SHORT][(df.index > self.__ord_curpri)]
        df_lo = df[self.__LONG][(df.index < self.__ord_curpri)]
        df_left = pd.concat([df_up, df_lo])

        plt1.hbar(y=df.index, height=0.03, left=df_right,
                  right=0, color=self.__BAR_R_COLOR)
        plt1.hbar(y=df.index, height=0.03, left=df_left,
                  right=0, color=self.__BAR_L_COLOR)
        plt1.line(x=[-self.__X_AXIS_MAX, self.__X_AXIS_MAX],
                  y=[self.__ord_curpri, self.__ord_curpri],
                  color=self.__CURPRI_COLOR, line_width=3)

        plt1.xaxis.axis_label = "Count Percent[%]"
        plt1.yaxis.axis_label = "Price"

        df = copy.copy(self.__psi_df)
        # --------------- メインfigure ---------------
        plt2 = figure(
            plot_height=fig_width,
            plot_width=fig_width,
            x_range=(-self.__X_AXIS_MAX, self.__X_AXIS_MAX),
            tools=set_tools,
            title="Position Book example",
            background_fill_color=self.__BG_COLOR
        )
        plt2.grid.grid_line_alpha = 0.3

        df_up = df[self.__LONG][(df.index > self.__psi_curpri)]
        df_lo = -df[self.__SHORT][(df.index < self.__psi_curpri)]
        df_right = pd.concat([df_up, df_lo])

        df_up = -df[self.__SHORT][(df.index > self.__psi_curpri)]
        df_lo = df[self.__LONG][(df.index < self.__psi_curpri)]
        df_left = pd.concat([df_up, df_lo])

        plt2.hbar(y=df.index, height=0.03, left=df_right,
                  right=0, color=self.__BAR_R_COLOR)
        plt2.hbar(y=df.index, height=0.03, left=df_left,
                  right=0, color=self.__BAR_L_COLOR)
        plt2.line(x=[-self.__X_AXIS_MAX, self.__X_AXIS_MAX],
                  y=[self.__psi_curpri, self.__psi_curpri],
                  color=self.__CURPRI_COLOR, line_width=3)

        plt2.xaxis.axis_label = "Count Percent[%]"
        plt2.yaxis.axis_label = "Price"

        # make a grid
        grid = gridplot([[plt1, plt2]])

        show(grid)

    def __changeDateTimeFmt(self, dt):
        """"日付フォーマットの変換メソッド
        引数:
            dt (str): DT_FMT形式でフォーマットされた日付
        戻り値:
            tf_dt (str): 変換後の日付
        """
        tdt = datetime.datetime.strptime(dt, self.__DT_FMT)

        return tdt


if __name__ == "__main__":
    cs = OrderBook(oc.OandaGrn.D)

    instrument = oc.OandaIns.USD_JPY

    dt = datetime.datetime(year=2019, month=5, day=18,
                           hour=21, minute=40, second=0)
    dttk = dt - timedelta(hours=9)

    cs.getInstrumentsOrderBook(instrument, dttk)
    cs.getInstrumentsPositionBook(instrument, dttk)
    cs.drawPositionOrderBook(500)
