# =================================================
# Pandas DataFrame "Append/Drop" test
# =================================================

import pandas as pd

df = pd.DataFrame({"numbers": ["001", "002", "003", "004", "005"],
                   "colors": ["red", "white", "blue", "black", "pink"]},
                  columns=["numbers", "colors"])
df.set_index("numbers", inplace = True)

df_add = pd.DataFrame({"numbers": ["006", "007"],
                   "colors": ["yellow", "cyan"]},
                  columns=["numbers", "colors"])
df_add.set_index("numbers", inplace = True)

print("----- df -----")
print(df)

df = df.append(df_add)

print("----- df(append) -----")
print(df)

print("----- df(drop) -----")
droplist = range(0, len(df_add))
df.drop(df.index[droplist], inplace = True)
print(df)
