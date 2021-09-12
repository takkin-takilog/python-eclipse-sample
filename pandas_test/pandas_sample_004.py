import datetime as dt
import pandas as pd

data_mat = [
    [dt.datetime(2021, 1, 15, 13, 1), 100, 200, 300, True],
    [dt.datetime(2021, 1, 15, 13, 2), 101, 201, 301, True],
    [dt.datetime(2021, 1, 15, 13, 3), 102, 202, 302, True],
    [dt.datetime(2021, 1, 15, 13, 4), 103, 203, 303, True],
    [dt.datetime(2021, 1, 15, 13, 5), 104, 204, 304, True],
    [dt.datetime(2021, 1, 15, 13, 6), 105, 205, 305, True],
    [dt.datetime(2021, 1, 15, 13, 7), 106, 206, 306, True],
    [dt.datetime(2021, 1, 15, 13, 8), 107, 207, 307, True],
    [dt.datetime(2021, 1, 15, 13, 9), 108, 208, 308, False],
    [dt.datetime(2021, 1, 15, 13, 10), 109, 209, 309, False],
]


COL_DATETIME = "DateTime"
COL_FIRST = "First"
COL_SECOND = "Second"
COL_THARD = "Thard"
COL_BOOL = "Bool"

df_org = pd.DataFrame(data_mat,
                      columns=[COL_DATETIME, COL_FIRST, COL_SECOND, COL_THARD, COL_BOOL])
df = df_org.set_index(COL_DATETIME)

print("{:-^60}".format(" DataFrame初期化 "))
print(df)

print("{:-^60}".format(" 行指定での値一括変更① "))
target_idx = dt.datetime(2021, 1, 15, 13, 6)
df.loc[target_idx] = [406, 506, 106, True]
print(df)

print("{:-^60}".format(" 行指定での値一括変更② "))
# 指定したインデックスが存在しなければ、最終行に追加される。
target_idx = dt.datetime(2021, 1, 15, 10, 1)
df.loc[target_idx] = [406, 506, 106, True]
print(df)

print("{:-^60}".format(" インデックスを昇順にソート "))
df.sort_index(inplace=True)
print(df)


print("{:-^60}".format(" 条件で行を抽出 "))
df_cond = df[df[COL_SECOND] == 203]
print(df_cond)


print("{:-^60}".format(" 先頭から2行を削除 "))
print(df)
df_drop = df.drop(df[:2].index)
print(df_drop)

print("{:-^60}".format(" True/Falseのみ抽出 "))
df_true = df[df[COL_BOOL]]
df_false = df[~df[COL_BOOL]]
print(df)
print(df_true)
print(df_false)
