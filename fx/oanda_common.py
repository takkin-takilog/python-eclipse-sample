# ==============================================================================
# brief        python OANDA 共通モジュール
#
# author       たっきん
# ==============================================================================


class OANDA_ENV(object):
    """ OANDA_ENV - OANDA環境の定義クラス。"""

    PRACTICE = "practice"   # デモ口座
    LIVE = "live"   # 本講座


class OANDA_GRN(object):
    """ OANDA_GRN - ローソク足の時間足定義クラス。"""

    S5 = "S5"  # 5 seconds
    S10 = "S10"  # 10 seconds
    S15 = "S15"  # 15 seconds
    S30 = "S30"  # 30 seconds
    M1 = "M1"  # 1 minute
    M2 = "M2"  # 2 minutes
    M3 = "M3"  # 3 minutes
    M4 = "M4"  # 4 minutes
    M5 = "M5"  # 5 minutes
    M10 = "M10"  # 10 minutes
    M15 = "M15"  # 15 minutes
    M30 = "M30"  # 30 minutes
    H1 = "H1"  # 1 hour
    H2 = "H2"  # 2 hours
    H3 = "H3"  # 3 hours
    H4 = "H4"  # 4 hours
    H6 = "H6"  # 6 hours
    H8 = "H8"  # 8 hours
    H12 = "H12"  # 12 hours
    D = "D"  # 1 Day
    W = "W"  # 1 Week
    M = "M"  # 1 Month
