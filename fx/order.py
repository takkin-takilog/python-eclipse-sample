# ==============================================================================
# brief        OANDA Order
#              注文する
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.orders import OrderCreate
from oandapyV20.endpoints.trades import TradeDetails, TradeClose
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya


class TimeInForceConst():
    """
    # TimeInForceConst - 注文時の有効期間条件定数クラス
    """
    # キャンセルされるまで有効
    # "Good unTil Cancelled"
    GTC = "GTC"

    # 指定された日時まで有効
    # "Good unTil Date" and will be cancelled at the provided time
    GTD = "GTD"

    # 当日のニューヨーク時間17時まで有効
    # "Good For Day" and will be cancelled at 5pm New York time
    GFD = "GFD"

    # 注文数量の全部が即座に約定しない場合、注文数量の全部を即座に失効させる
    # "Filled Or Killed"
    FOK = "FOK"

    # 指定した価格かそれよりも有利な価格で、即時に一部あるいは全数量を約定させ、
    # 成立しなかった注文数量をキャンセルさせる
    # "Immediately partially filled Or Cancelled"
    IOC = "IOC"


class OrderTypeConst():
    """
    # OrderTypeConst - 注文タイプ定数クラス
    """
    # 成行注文
    # A Market Order
    MARKET = "MARKET"

    # 指値注文
    # A Limit Order
    # ※ポジション・オープンで使用
    LIMIT = "LIMIT"

    # 逆指値注文
    # A Stop Order
    # ※ポジション・オープンで使用
    STOP = "STOP"

    # MIT注文
    # A Market-if-touched Order
    # ＜指値との違い＞
    # 条件に達すると注文が実行されるが、ロットサイズが大きい場合、実行には時間がかかる。
    # 実行中に条件から外れた場合、指値注文とMIT注文で動作が異なる。
    #  指値注文：条件から外れたら注文を停止する。
    #  MIT注文：条件から外れても注文は停止しない。その場合、成行きで注文が実行される。
    MARKET_IF_TOUCHED = "MARKET_IF_TOUCHED"

    # 利益確定注文（指値注文）
    # A Take Profit Order
    # ※ポジション・クローズで使用（オープン時には使用不可）
    # Note:Cannot be used to opan a new posiition.
    TAKE_PROFIT = "TAKE_PROFIT"

    # ストップ注文（逆指値注文）
    # A Stop Loss Order
    # ※ポジション・クローズで使用（オープン時には使用不可）
    # Note:Cannot be used to opan a new posiition.
    STOP_LOSS = "STOP_LOSS"

    # トレイリング・ストップ・リミット注文
    # A Trailing Stop Loss Order
    # ※ポジション・クローズで使用（オープン時には使用不可）
    # Note:Cannot be used to opan a new posiition.
    TRAILING_STOP_LOSS = "TRAILING_STOP_LOSS"

    # A Fixed Price Order
    FIXED_PRICE = "FIXED_PRICE"


"""
# ========== ex01 ==========
# 成行注文（買）
# 注文方法：成行
# 取引通貨：USD/JPY
# 売買：買い
# 数量：10000
# ==========================
data = {
    "order": {
        "instrument": "USD_JPY",
        "units": "+10000",
        "type": "MARKET",
        "positionFill": "DEFAULT"
    }
}

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
r = OrderCreate(ya.account_number, data=data)
rsp = api.request(r)
"""

"""
# ========== ex02 ==========
# トレードの詳細を取得
# ==========================
api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
r = TradeDetails(ya.account_number, tradeID=13)
rsp = api.request(r)
"""

# ========== ex03 ==========
# トレード・クローズ
# トレードID：13
# 数量：5000
# ==========================
data = {
    "units": 5000,
}

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
r = TradeClose(ya.account_number, tradeID=13, data=data)
rsp = api.request(r)


print(json.dumps(rsp, indent=2))

