import time
import random
import pandas as pd

SMA_SPAN_L = 100000
SMA_SPAN_S = int(SMA_SPAN_L / 2)
COL_SMA_L = "sma_l"
COL_SMA_S = "sma_s"

float_list = [random.uniform(100.0, 200.0) for i in range(SMA_SPAN_L)]
indexs = range(1, SMA_SPAN_L + 1)
s = pd.Series(float_list, index=indexs, name="float_list")

time_sta = time.perf_counter()

df = pd.DataFrame(s)
df[COL_SMA_L] = s.rolling(window=SMA_SPAN_L).mean()
df[COL_SMA_S] = s.rolling(window=SMA_SPAN_S).mean()

counter = time.perf_counter() - time_sta

print(df)

print("---------- Result ----------")
print(counter)
