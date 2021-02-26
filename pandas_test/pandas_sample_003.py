import datetime as dt
import pandas as pd

data_mat = [
    [dt.datetime(2021, 1, 15, 13, 1), 1],
    [dt.datetime(2021, 1, 15, 13, 2), 2],
    [dt.datetime(2021, 1, 15, 13, 3), 3],
    [dt.datetime(2021, 1, 15, 13, 4), 4],
    [dt.datetime(2021, 1, 15, 13, 5), 5],
    [dt.datetime(2021, 1, 15, 13, 6), 6],
    [dt.datetime(2021, 1, 15, 13, 7), 7],
    [dt.datetime(2021, 1, 15, 13, 8), 8],
    [dt.datetime(2021, 1, 15, 13, 9), 9],
    [dt.datetime(2021, 1, 15, 13, 10), 10],

    [dt.datetime(2021, 1, 16, 13, 1), 11],
    [dt.datetime(2021, 1, 16, 13, 2), 12],
    [dt.datetime(2021, 1, 16, 13, 3), 13],
    [dt.datetime(2021, 1, 16, 13, 4), 14],
    [dt.datetime(2021, 1, 16, 13, 5), 15],
    [dt.datetime(2021, 1, 16, 13, 6), 16],
    [dt.datetime(2021, 1, 16, 13, 7), 17],
    [dt.datetime(2021, 1, 16, 13, 8), 18],
    [dt.datetime(2021, 1, 16, 13, 9), 19],
    [dt.datetime(2021, 1, 16, 13, 10), 20],

    [dt.datetime(2021, 1, 17, 13, 1), 21],
    [dt.datetime(2021, 1, 17, 13, 2), 22],
    [dt.datetime(2021, 1, 17, 13, 3), 23],
    [dt.datetime(2021, 1, 17, 13, 4), 24],
    [dt.datetime(2021, 1, 17, 13, 5), 25],
    [dt.datetime(2021, 1, 17, 13, 6), 26],
    [dt.datetime(2021, 1, 17, 13, 7), 27],
    [dt.datetime(2021, 1, 17, 13, 8), 28],
    [dt.datetime(2021, 1, 17, 13, 9), 29],
    [dt.datetime(2021, 1, 17, 13, 10), 30],
]

df_org = pd.DataFrame(data_mat,
                      columns=["DateTime", "no"])
df = df_org.set_index("DateTime")

print("{:-^60}".format(" DataFrame初期化 "))
print(df)

print("{:-^60}".format(" 指定された時刻範囲を抽出 "))
start_time = dt.time(13, 2)
end_time = dt.time(13, 4)
df_time = df.loc[start_time:end_time]
print(df_time)

print("{:-^60}".format(" 指定された日付時間範囲を抽出 "))
start_dt = dt.datetime(2021, 1, 15, 13, 5)
end_dt = dt.datetime(2021, 1, 17, 13, 3)
df_dt = df.loc[start_dt:end_dt]
print(df_dt)
