from datetime import datetime, timedelta, timezone

DT_FMT = "%Y-%m-%dT%H:%M:%S"

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

tdjp = datetime(year=2019, month=5, day=21, hour=13, minute=0, second=0)
print("タイムゾーン：東京指定")
print("{}   {}" .format(tdjp, tdjp.timestamp()))

td = datetime(year=2019, month=5, day=21, hour=13, minute=0, second=0)
print("タイムゾーン：指定なし")
print("{}   {}" .format(td, td.timestamp()))
bb = td




