# ==============================================================================
# brief        OANDA Orders Common
#              OANDA 注文共通
#
# author       たっきん
# ==============================================================================


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


class OrderPositionFillConst():
    """
    # OrderPositionFillConst - ポジション数変更方法定数クラス
    #
    #  Specification of how Positions in the Account are modified when the
    #  Order is filled.
    """
    # 新規ポジションを保有する用途のみで使用可。
    # 両建て可能アカウントの場合、両建てとなる。
    # 両建て不可アカウントの場合、指定不可。
    # When the Order is filled, only allow Positions to be opened or extended.
    OPEN_ONLY = "OPEN_ONLY"

    # ポジションを保有していた場合は優先して減少させる。
    # 新規ポジションを増やすことは可。
    # When the Order is filled, always fully reduce an existing Position before
    # opening a new Position.
    REDUCE_FIRST = "REDUCE_FIRST"

    # 保有ポジション数を減少させる用途のみで指定可能。
    # 但し、新規ポジションを増やすことは不可。
    # When the Order is filled, only reduce an existing Position.
    REDUCE_ONLY = "REDUCE_ONLY"

    # 両建て不可アカウントの場合、"REDUCE_FIRST"となり、
    # 両建て可能アカウントの場合、"OPEN_ONLY"となる。
    # When the Order is filled, use REDUCE_FIRST behaviour for non-client
    # hedging Accounts, and OPEN_ONLY behaviour for client hedging Accounts.
    DEFAULT = "DEFAULT"
