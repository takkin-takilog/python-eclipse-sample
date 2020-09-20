# =================================================
# Pandas DataFrame "Append/Drop" test
# =================================================
import datetime as dt
import pandas as pd

YOBI = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data_mat = [
    ["2020/09/01", "1:00", 0, 101],
    ["2020/09/01", "2:00", 0, 102],
    ["2020/09/01", "3:00", 0, 103],

    ["2020/09/02", "1:00", 1, 111],
    ["2020/09/02", "2:00", 1, 112],
    ["2020/09/02", "3:00", 1, 113],

    ["2020/09/03", "1:00", 0, 121],
    ["2020/09/03", "2:00", 0, 122],
    ["2020/09/03", "3:00", 0, 123],

    ["2020/09/04", "1:00", 0, 131],
    ["2020/09/04", "2:00", 0, 132],
    ["2020/09/04", "3:00", 0, 133],

    ["2020/09/05", "1:00", 1, 141],
    ["2020/09/05", "2:00", 1, 142],
    ["2020/09/05", "3:00", 1, 143],

    ["2020/09/06", "1:00", 1, 151],
    ["2020/09/06", "2:00", 1, 152],
    ["2020/09/06", "3:00", 1, 153],

    ["2020/09/07", "1:00", 1, 161],
    ["2020/09/07", "2:00", 1, 162],
    ["2020/09/07", "3:00", 1, 163],

    ["2020/09/08", "1:00", 0, 171],
    ["2020/09/08", "2:00", 0, 172],
    ["2020/09/08", "3:00", 0, 173],

    ["2020/09/09", "1:00", 0, 181],
    ["2020/09/09", "2:00", 0, 182],
    ["2020/09/09", "3:00", 0, 183],

    ["2020/09/10", "1:00", 0, 191],
    ["2020/09/10", "2:00", 0, 192],
    ["2020/09/10", "3:00", 0, 193],

]

df_org = pd.DataFrame(data_mat,
                      columns=["Date", "Time", "Goto", "Value"])
print("{:-^60}".format(" DataFrame初期化 "))
print(df_org)

# ==================== 曜日追加 ====================
print("{:-^60}".format(" \"Date\" 一覧取得 "))
date_list = list(df_org.groupby("Date").groups.keys())
print(date_list)

date_dict = {}
for date in date_list:
    dt_ = dt.datetime.strptime(date, "%Y/%m/%d")
    date_dict[date] = YOBI[dt_.weekday()]

print(date_dict)

yobi_list = []
for date in df_org["Date"]:
    yobi_list.append(date_dict[date])

df_org["Weekday"] = yobi_list

print("{:-^60}".format(" 曜日追加 "))
print(df_org)

# ==================== マルチインデックス ====================
df_multi = df_org.set_index(["Date", "Weekday", "Goto", "Time"]).sort_index()
print("{:-^60}".format(" Multi Index "))
print(df_multi)


df_time_mean = df_multi.mean(level=["Goto", "Time"]).sort_index()
print("{:-^60}".format(" Multi Index [Mean](Goto, Time) "))
print(df_time_mean)

df_time_mean = df_multi.mean(level=["Weekday", "Goto", "Time"]).sort_index()
print("{:-^60}".format(" Multi Index [Mean](Weekday, Goto, Time) "))
print(df_time_mean)
