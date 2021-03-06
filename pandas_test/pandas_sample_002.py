# =================================================
# Pandas DataFrame "Append/Drop" test
# =================================================
import datetime as dt
import pandas as pd

YOBI = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data_mat = [
    ["2020/09/01", "1:00", 0, 101, 110, 91, 106],
    ["2020/09/01", "2:00", 0, 102, 112, 90, 103],
    ["2020/09/01", "3:00", 0, 103, 122, 89, 110],
    ["2020/09/01", "4:00", 0, 104, 117, 88, 109],
    ["2020/09/01", "5:00", 0, 105, 123, 85, 117],

    ["2020/09/02", "1:00", 1, 111, 120, 91, 113],
    ["2020/09/02", "2:00", 1, 112, 130, 81, 110],
    ["2020/09/02", "3:00", 1, 113, 125, 61, 111],
    ["2020/09/02", "4:00", 1, 114, 126, 60, 112],
    ["2020/09/02", "5:00", 1, 115, 127, 59, 113],

    ["2020/09/03", "1:00", 0, 121, 150, 61, 110],
    ["2020/09/03", "2:00", 0, 122, 130, 71, 100],
    ["2020/09/03", "3:00", 0, 123, 140, 61, 93],
    ["2020/09/03", "4:00", 0, 124, 135, 62, 90],
    ["2020/09/03", "5:00", 0, 125, 133, 63, 85],

    ["2020/09/04", "1:00", 0, 131, 180, 101, 111],
    ["2020/09/04", "2:00", 0, 132, 170, 91, 106],
    ["2020/09/04", "3:00", 0, 133, 150, 90, 121],
    ["2020/09/04", "4:00", 0, 134, 148, 88, 111],
    ["2020/09/04", "5:00", 0, 135, 145, 85, 101],

    ["2020/09/05", "1:00", 1, 141, 170, 121, 130],
    ["2020/09/05", "2:00", 1, 142, 160, 123, 150],
    ["2020/09/05", "3:00", 1, 143, 180, 111, 125],
    ["2020/09/05", "4:00", 1, 144, 181, 121, 150],
    ["2020/09/05", "5:00", 1, 145, 185, 131, 140],

    ["2020/09/06", "1:00", 1, 151, 190, 131, 152],
    ["2020/09/06", "2:00", 1, 152, 195, 125, 140],
    ["2020/09/06", "3:00", 1, 153, 185, 111, 166],
    ["2020/09/06", "4:00", 1, 154, 187, 101, 156],
    ["2020/09/06", "5:00", 1, 155, 190, 105, 146],

    ["2020/09/07", "1:00", 1, 161, 210, 136, 181],
    ["2020/09/07", "2:00", 1, 162, 185, 142, 166],
    ["2020/09/07", "3:00", 1, 163, 175, 123, 160],
    ["2020/09/07", "4:00", 1, 164, 176, 120, 161],
    ["2020/09/07", "5:00", 1, 165, 180, 110, 150],

    ["2020/09/08", "1:00", 0, 171, 220, 152, 180],
    ["2020/09/08", "2:00", 0, 172, 230, 132, 199],
    ["2020/09/08", "3:00", 0, 173, 200, 101, 144],
    ["2020/09/08", "4:00", 0, 174, 210, 111, 174],
    ["2020/09/08", "5:00", 0, 175, 205, 121, 155],

    ["2020/09/09", "1:00", 0, 181, 250, 91, 204],
    ["2020/09/09", "2:00", 0, 182, 210, 125, 189],
    ["2020/09/09", "3:00", 0, 183, 270, 135, 155],
    ["2020/09/09", "4:00", 0, 184, 271, 133, 145],
    ["2020/09/09", "5:00", 0, 185, 273, 120, 175],

    ["2020/09/10", "1:00", 0, 191, 235, 151, 210],
    ["2020/09/10", "2:00", 0, 192, 245, 160, 202],
    ["2020/09/10", "3:00", 0, 193, 265, 120, 186],
    ["2020/09/10", "4:00", 0, 194, 275, 110, 166],
    ["2020/09/10", "5:00", 0, 195, 270, 115, 156],

]

df_org = pd.DataFrame(data_mat,
                      columns=["Date", "Time", "Goto", "o", "h", "l", "c"])
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
print("{:-^60}".format(" Multi Index 1 "))
print(df_multi)
print("{:-^60}".format(" Multi Index 2 "))
df_multi["h-o"] = df_multi["h"] - df_multi["o"]
df_multi["l-o"] = df_multi["l"] - df_multi["o"]
df_multi["c-o"] = df_multi["c"] - df_multi["o"]
print(df_multi)

print("{:-^60}".format(" Multi Index 3 "))
print(df_multi.index.get_level_values(level="Date"))

df_time_mean = df_multi.mean(level=["Goto", "Time"]).sort_index()
print("{:-^60}".format(" Multi Index [Mean](Goto, Time) "))
print(df_time_mean)

df_time_mean = df_multi.mean(level=["Weekday", "Goto", "Time"]).sort_index()
print("{:-^60}".format(" Multi Index [Mean](Weekday, Goto, Time) "))
print(df_time_mean)
