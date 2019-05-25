from datetime import datetime, timedelta, timezone
import pandas as pd
from comtypes.npsupport import numpy as np

DT_FMT = "%Y-%m-%dT%H:%M:%S"

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

tdjp = datetime(year=2019, month=5, day=21, hour=13, minute=0, second=0)
print("タイムゾーン：東京指定")
print("{}   {}" .format(tdjp, tdjp.timestamp()))
print(tdjp.tzinfo)

td = datetime(year=2019, month=5, day=21, hour=13, minute=0, second=0)
print("タイムゾーン：指定なし")
print("{}   {}" .format(td, td.timestamp()))
print(td.tzinfo)


print("========== タイムスタンプ ==========")

tsjp = pd.Timestamp('2018-01-01 12:00:00', tz='Asia/Tokyo')
tsjpts = tsjp.timestamp()
tsjpdt = tsjp.to_pydatetime()
print("タイムゾーン：東京指定")
print("{} / {} / {}" .format(tsjp, tsjpts, datetime.fromtimestamp(tsjpts)))
print("{} / {}" .format(tsjpdt, datetime.fromtimestamp(tsjpts)))
print("{} / {}" .format(tsjpdt, datetime.utcfromtimestamp(tsjpts)))

ts = pd.Timestamp('2018-01-01 12:00:00')
tsts = ts.timestamp()
print("タイムゾーン：指定なし")
print("{} / {} / {}" .format(ts, tsts, datetime.fromtimestamp(tsts)))


print("========== pandas ==========")
# dti = pd.date_range(start='1/1/2018', periods=5, tz='Asia/Tokyo')
dti = pd.date_range(start='1/1/2018', periods=5)
print(dti)
uti = dti.tz_localize('Asia/Tokyo').astype(np.int64) // 10**9
print(uti)
print("========== pandas2 ==========")

df = pd.DataFrame({"ts": dti, "uti":uti})
print(df)


