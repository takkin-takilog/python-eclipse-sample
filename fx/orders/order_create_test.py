# ==============================================================================
# brief        OANDA OrderCreate API Test
#              OANDA 注文作成APIテスト
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
# ==============================================================================

import json
from oandapyV20.endpoints.orders import OrderCreate
from oandapyV20 import API
from fx import oanda_common as oc
from fx import your_account as ya

# ========== ex_maket01 ==========
# 注文方法：成行
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# ================================
data_ma01 = {
    "order": {
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "MARKET",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_maket02 ==========
# 注文方法：成行
# 取引通貨：USD/JPY
# 売買：売
# 数量：10000
# ================================
data_ma02 = {
    "order": {
        "instrument": "USD_JPY",
        "units": -10000,
        "type": "MARKET",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_maket03 ==========
# 注文方法：成行(OCO注文)
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# 利確指値：150.00円(GTC)
# 損切逆指値：100.00円(GTC)
# ================================
data_ma03 = {
    "order": {
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "MARKET",
        "positionFill": "DEFAULT",
        "takeProfitOnFill": {
            "timeInForce": "GTC",
            "price": 150.000
        },
        "stopLossOnFill": {
            "timeInForce": "GTC",
            "price": 80.000
        },
    }
}

# ========== ex_limit01 ==========
# 注文方法：指値
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# ================================
data_li01 = {
    "order": {
        "price": 100.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "LIMIT",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_limit02 ==========
# 注文方法：指値
# 価格指定：100.000円
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：売
# 数量：10000
# ================================
data_li02 = {
    "order": {
        "price": 100.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": -10000,
        "type": "LIMIT",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_limit03 ==========
# 注文方法：指値(OCO)
# 価格指定：100.000円
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# 利確指値：150.00円(GTC)
# 損切逆指値：100.00円(GTC)
# ================================
data_li03 = {
    "order": {
        "price": 100.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "LIMIT",
        "positionFill": "DEFAULT",
        "takeProfitOnFill": {
            "timeInForce": "GTC",
            "price": 150.000
        },
        "stopLossOnFill": {
            "timeInForce": "GTC",
            "price": 80.000
        },
    }
}

# ========== ex_stop01 ==========
# 注文方法：逆指値
# 価格指定：130.000円
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# ===============================
data_st01 = {
    "order": {
        "price": 130.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "STOP",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_stop02 ==========
# 注文方法：逆指値
# 価格指定：130.000円
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：売
# 数量：10000
# ================================
data_st02 = {
    "order": {
        "price": 130.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": -10000,
        "type": "STOP",
        "positionFill": "DEFAULT"
    }
}

# ========== ex_stop03 ==========
# 注文方法：逆指値(OCO)
# 価格指定：130.000円
# 有効期間：キャンセルされるまで有効(GTC)
# 取引通貨：USD/JPY
# 売買：買
# 数量：10000
# 利確指値：150.00円(GTC)
# 損切逆指値：100.00円(GTC)
# ================================
data_st03 = {
    "order": {
        "price": 130.000,
        "timeInForce": "GTC",
        "instrument": "USD_JPY",
        "units": 10000,
        "type": "STOP",
        "positionFill": "DEFAULT",
        "takeProfitOnFill": {
            "timeInForce": "GTC",
            "price": 150.000
        },
        "stopLossOnFill": {
            "timeInForce": "GTC",
            "price": 100.000
        },
    }
}


# ========== ex_takeprofit01 ==========
# 注文方法：決済注文（利益確定）
# 価格指定：130.000円
# 有効期間：キャンセルされるまで有効(GTC)
#
# ※決済注文するならOrderCreateよりTradeCRCDOをっ使ったほうが良い
# =====================================
data_tp01 = {
    "order": {
        "timeInForce": "GTC",
        "price": 130.000,
        "type": "TAKE_PROFIT",
        "tradeID": "85",
    },
}

# ========== ex_stoploss01 ==========
# 注文方法：決済注文（ストップ）
# 価格指定：100.000円
# 有効期間：キャンセルされるまで有効(GTC)
#
# ※決済注文するならOrderCreateよりTradeCRCDOをっ使ったほうが良い
# ===================================
data_sl01 = {
    "order": {
        "timeInForce": "GTC",
        "price": 100.000,
        "type": "STOP_LOSS",
        "tradeID": "85",
    },
}


# ---------- 成行 ----------
data = data_ma01
# data = data_ma02
# data = data_ma03
# ---------- 指値 ----------
# data = data_li01
# data = data_li02
# data = data_li03
# ---------- 逆指値 ----------
# data = data_st01
# data = data_st02
# data = data_st03
# ---------- 決済注文（利益確定） ----------
# data = data_tp01
# ---------- 決済注文（ストップ） ----------
# data = data_sl01

api = API(access_token=ya.access_token, environment=oc.OandaEnv.PRACTICE)
ep = OrderCreate(accountID=ya.account_number, data=data)
rsp = api.request(ep)
print(json.dumps(rsp, indent=2))
