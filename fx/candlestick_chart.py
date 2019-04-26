# ==============================================================================
# brief        ローソク足チャートの描写
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
#     Bokehのインストール（conda install bokeh）
# ==============================================================================

import copy
import datetime
from math import pi

from bokeh.layouts import Column
from bokeh.models import RangeTool
from bokeh.plotting import figure, show, output_file
from oandapyV20 import API

from bokehlib import bokeh_common as bc
from fx import oanda_common as oc
from fx import your_account as ya
import oandapyV20.endpoints.instruments as instruments
import pandas as pd


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

        self.__WIDE = 12 * 60 * 60 * 1000  # half day in ms
        self.__WIDE_SCALE = 0.2

        self.__SMA1PRD = 5
        self.__SMA2PRD = 20
        self.__SMA3PRD = 75

        # 移動平均線
        self.__SMA1COL = "SMA-" + str(self.__SMA1PRD)
        self.__SMA2COL = "SMA-" + str(self.__SMA2PRD)
        self.__SMA3COL = "SMA-" + str(self.__SMA3PRD)

        # ボリンジャーバンド
        self.__BB_BASE = "BB-Base"
        self.__BB_U_SIGMA = "BB-Sig-up"
        self.__BB_U_SIGMA2 = "BB-Sig*2-up"
        self.__BB_U_SIGMA3 = "BB-Sig*3-up"
        self.__BB_L_SIGMA = "BB-Sig-low"
        self.__BB_L_SIGMA2 = "BB-Sig*2-low"
        self.__BB_L_SIGMA3 = "BB-Sig*3-low"

        # MACD
        self.__MACD = "MACD"
        self.__SIGN = "SIGN"

        self.__BG_COLOR = "#2e2e2e"
        self.__CND_INC_COLOR = "#e73b3a"
        self.__CND_DEC_COLOR = "#03c103"
        self.__CND_EQU_COLOR = "#ffff00"
        self.__DT_FMT = "%Y-%m-%dT%H:%M:00.000000000Z"

        self.__GRANULARITY = granularity

        self.__df = []

        self.__api = API(access_token=ya.access_token,
                         environment=oc.OandaEnv.PRACTICE)

    def getInstrumentsCandles(self, instrument, dt_from, dt_to):

        params = {
            "alignmentTimezone": "Japan",
            "from": dt_from.strftime(self.__DT_FMT),
            "to": dt_to.strftime(self.__DT_FMT),
            "granularity": self.__GRANULARITY
        }

        # APIへ過去データをリクエスト
        ic = instruments.InstrumentsCandles(instrument=instrument,
                                            params=params)
        self.__api.request(ic)

        self.__data = []
        for raw in ic.response[self.__CANDLES]:
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

        # ---------- 移動平均線 ----------
        df[self.__SMA1COL] = df[self.__CLOSE].rolling(
            window=self.__SMA1PRD).mean()
        df[self.__SMA2COL] = df[self.__CLOSE].rolling(
            window=self.__SMA2PRD).mean()
        df[self.__SMA3COL] = df[self.__CLOSE].rolling(
            window=self.__SMA3PRD).mean()

        # ---------- ボリンジャーバンド ----------
        sigma = df[self.__CLOSE].rolling(window=self.__SMA2PRD).std(ddof=0)
        base = df[self.__SMA2COL]
        df[self.__BB_BASE] = base
        df[self.__BB_U_SIGMA] = base + sigma
        df[self.__BB_U_SIGMA2] = base + sigma * 2
        df[self.__BB_U_SIGMA3] = base + sigma * 3
        df[self.__BB_L_SIGMA] = base - sigma
        df[self.__BB_L_SIGMA2] = base - sigma * 2
        df[self.__BB_L_SIGMA3] = base - sigma * 3

        # ---------- MACD ----------
        ema_s = df[self.__CLOSE].ewm(span=12).mean()
        ema_l = df[self.__CLOSE].ewm(span=26).mean()
        df[self.__MACD] = (ema_s - ema_l)
        df[self.__SIGN] = df[self.__MACD].ewm(span=9).mean()

        self.__df = copy.copy(df)

    def drawCandleStick(self, fig_width=1000):

        df = copy.copy(self.__df)

        inc = df[self.__CLOSE] > df[self.__OPEN]
        dec = df[self.__OPEN] > df[self.__CLOSE]
        equ = df[self.__CLOSE] == df[self.__OPEN]

        set_tools = bc.ToolType.gen_str(bc.ToolType.XPAN,
                                        bc.ToolType.WHEEL_ZOOM,
                                        bc.ToolType.BOX_ZOOM,
                                        bc.ToolType.RESET,
                                        bc.ToolType.SAVE)

        inc_color = self.__CND_INC_COLOR
        dec_color = self.__CND_DEC_COLOR
        equ_color = self.__CND_EQU_COLOR

        # --------------- メインfigure ---------------
        fig1_len = int(len(df) * self.__WIDE_SCALE)
        enddt = oc.OandaGrn.offset(df.index[-1], self.__GRANULARITY)

        plt_main = figure(
            plot_height=400,
            plot_width=fig_width,
            x_axis_type=bc.AxisTyp.X_DATETIME,
            x_range=(df.index[-fig1_len], enddt),
            tools=set_tools,
            background_fill_color=self.__BG_COLOR,
            title="Candlestick example"
        )
        plt_main.xaxis.major_label_orientation = pi / 4
        plt_main.grid.grid_line_alpha = 0.3

        # draw Candle Stick (increment)
        plt_main.segment(df.index[inc], df[self.__HIGHT][inc], df.index[inc],
                         df[self.__LOW][inc], color=inc_color, line_width=1)
        plt_main.vbar(df.index[inc], self.__WIDE, df[self.__OPEN][inc],
                      df[self.__CLOSE][inc], fill_color=inc_color,
                      line_width=1, line_color=inc_color)

        # draw Candle Stick (decrement)
        plt_main.segment(df.index[dec], df[self.__HIGHT][dec], df.index[dec],
                         df[self.__LOW][dec], color=dec_color, line_width=1)
        plt_main.vbar(df.index[dec], self.__WIDE, df[self.__OPEN][dec],
                      df[self.__CLOSE][dec], fill_color=dec_color,
                      line_width=1, line_color=dec_color)

        # draw Candle Stick (equal)
        plt_main.segment(df.index[equ], df[self.__HIGHT][equ], df.index[equ],
                         df[self.__LOW][equ], color=equ_color, line_width=1)
        plt_main.vbar(df.index[equ], self.__WIDE, df[self.__OPEN][equ],
                      df[self.__CLOSE][equ], fill_color=equ_color,
                      line_width=1, line_color=equ_color)

        # 移動平均線
        plt_main.line(df.index, df[self.__SMA1COL], line_width=2,
                      line_color="pink", legend=self.__SMA1COL)
        plt_main.line(df.index, df[self.__SMA2COL], line_width=2,
                      line_color="yellow", legend=self.__SMA2COL)
        plt_main.line(df.index, df[self.__SMA3COL], line_width=2,
                      line_color="orange", legend=self.__SMA3COL)

        # ボリンジャーバンド
        bb_width = 1
        plt_main.line(df.index, df[self.__BB_BASE], line_dash="dotted",
                      line_width=2, line_color="blue", legend="base")
        plt_main.line(df.index, df[self.__BB_U_SIGMA], line_dash="dotted",
                      line_width=bb_width, line_color="deepskyblue",
                      legend="±1σ")
        plt_main.line(df.index, df[self.__BB_L_SIGMA], line_dash="dotted",
                      line_width=bb_width, line_color="deepskyblue")
        plt_main.line(df.index, df[self.__BB_U_SIGMA2], line_dash="dotted",
                      line_width=bb_width, line_color="aqua",
                      legend="±2σ")
        plt_main.line(df.index, df[self.__BB_L_SIGMA2], line_dash="dotted",
                      line_width=bb_width, line_color="aqua")
        plt_main.line(df.index, df[self.__BB_U_SIGMA3], line_dash="dotted",
                      line_width=bb_width, line_color="aquamarine",
                      legend="±3σ")
        plt_main.line(df.index, df[self.__BB_L_SIGMA3], line_dash="dotted",
                      line_width=bb_width, line_color="aquamarine")
        plt_main.legend.location = "top_left"

        # --------------- レンジツールfigure ---------------
        plt_rang = figure(
            plot_height=150,
            plot_width=fig_width,
            x_range=(df.index[0], enddt),
            y_range=plt_main.y_range,
            x_axis_type=bc.AxisTyp.X_DATETIME,
            background_fill_color=self.__BG_COLOR,
            toolbar_location=None,
        )
        plt_rang.xaxis.major_label_orientation = pi / 4
        plt_rang.grid.grid_line_alpha = 0.3

        # draw Candle Stick (increment)
        plt_rang.segment(df.index[inc], df[self.__HIGHT][inc], df.index[inc],
                         df[self.__LOW][inc], color=inc_color)
        plt_rang.vbar(df.index[inc], self.__WIDE, df[self.__OPEN][inc],
                      df[self.__CLOSE][inc], fill_color=inc_color,
                      line_width=1, line_color=inc_color)

        # draw Candle Stick (decrement)
        plt_rang.segment(df.index[dec], df[self.__HIGHT][dec], df.index[dec],
                         df[self.__LOW][dec], color=dec_color)
        plt_rang.vbar(df.index[dec], self.__WIDE, df[self.__OPEN][dec],
                      df[self.__CLOSE][dec], fill_color=dec_color,
                      line_width=1, line_color=dec_color)

        # draw Candle Stick (equal)
        plt_rang.segment(df.index[equ], df[self.__HIGHT][equ], df.index[equ],
                         df[self.__LOW][equ], color=equ_color)
        plt_rang.vbar(df.index[equ], self.__WIDE, df[self.__OPEN][equ],
                      df[self.__CLOSE][equ], fill_color=equ_color,
                      line_width=1, line_color=equ_color)

        # --------------- MACD figure ---------------
        plt_macd = figure(
            plot_height=150,
            plot_width=fig_width,
            x_axis_type=bc.AxisTyp.X_DATETIME,
            x_range=plt_main.x_range,
            tools=set_tools,
            background_fill_color=self.__BG_COLOR,
        )
        plt_macd.xaxis.major_label_orientation = pi / 4
        plt_macd.grid.grid_line_alpha = 0.3

        # MACD
        plt_macd.line(df.index, df[self.__MACD],
                      legend=self.__MACD, line_color="red")
        plt_macd.line(df.index, df[self.__SIGN],
                      legend=self.__SIGN, line_color="cyan")
        plt_macd.grid.grid_line_alpha = 0.3
        plt_macd.legend.location = "top_left"

        # --------------- レンジツール ---------------
        range_tool = RangeTool(x_range=plt_main.x_range)
        plt_rang.add_tools(range_tool)
        plt_rang.toolbar.active_multi = range_tool

        output_file("candlestick_sample001.html",
                    title="candlestick.py example")

        show(Column(plt_main, plt_rang, plt_macd))    # open a browser

    def __changeDateTimeFmt(self, dt):
        """"日付フォーマットの変換メソッド
        引数:
            dt (str): DT_FMT形式でフォーマットされた日付
        戻り値:
            tf_dt (str): 変換後の日付
        """
        if self.__GRANULARITY is oc.OandaGrn.D:
            tdt = datetime.datetime.strptime(dt, self.__DT_FMT)
            tf_dt = datetime.date(tdt.year, tdt.month, tdt.day)

        return tf_dt


if __name__ == "__main__":
    cs = CandleStick(oc.OandaGrn.D)

    instrument = oc.OandaIns.USD_JPY
    dt_from = datetime.datetime(
        year=2018, month=1, day=1, hour=0, minute=0, second=0)
    dt_to = datetime.datetime(
        year=2019, month=2, day=1, hour=12, minute=0, second=0)
    cs.getInstrumentsCandles(instrument, dt_from, dt_to)
    cs.drawCandleStick()
