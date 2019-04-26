# ==============================================================================
# brief        Plotサンプルコード 002
#
# author       たっきん
# ==============================================================================
import pandas as pd
import matplotlib.pyplot as plt


data = {"value": [120, 100, 90, 110, 150, 200, 300, 1000, 900, 800,
                  500, 300, 250, 200, 190, 150, 100, 50, 60, 80,
                  100, 150, 200, 400, 800, 1600]}

df = pd.DataFrame(data)


# --------------- n期間の移動平均線 ---------------
n1 = 3   # 期間の設定
n2 = 5   # 期間の設定
n3 = 10   # 期間の設定

SMAn1 = df["value"].rolling(window=n1).mean()
SMAn2 = df["value"].rolling(window=n2).mean()
SMAn3 = df["value"].rolling(window=n3).mean()

# ********** 描写 **********
fig1 = plt.figure("移動平均線")

plt.plot(df, label="Sample")
plt.legend()
plt.scatter(range(df.size), df)
plt.plot(SMAn1, linestyle="dashed", label="SMA-" + str(n1))
plt.plot(SMAn2, linestyle="dashed", label="SMA-" + str(n2))
plt.plot(SMAn3, linestyle="dashed", label="SMA-" + str(n3))
plt.legend()
plt.scatter(range(df.size), SMAn1, marker="*")
plt.scatter(range(df.size), SMAn2, marker="*")
plt.scatter(range(df.size), SMAn3, marker="*")

plt.title("Simple Moving Average(SMA)")
plt.grid(linestyle="dashed")


# --------------- MACD ---------------
sn = 3   # 移動平均（短期）期間の設定
ln = 7   # 移動平均（長期）期間の設定
mn = 5   # MACD期間の設定

EMAsn = df["value"].ewm(span=sn).mean()
EMAln = df["value"].ewm(span=ln).mean()
MACD = (EMAsn - EMAln)
SIGNAL = MACD.ewm(span=mn).mean()

# ********** 描写 **********
fig2 = plt.figure("MACD")

plt.plot(df, label="Sample")
plt.plot(MACD, linestyle="dashed", label="MACD")
plt.plot(SIGNAL, linestyle="dashed", label="Signal")
plt.legend()
plt.scatter(range(df.size), df)
plt.scatter(range(df.size), MACD, marker="*")
plt.scatter(range(df.size), SIGNAL, marker="*")

plt.title("MACD")
plt.grid(linestyle="dashed")


# --------------- ボリンジャーバンド ---------------
n = 5   # 期間の設定

# ===== 中心線の計算 =====
SMA_BB_n = df["value"].rolling(window=n).mean()


# ===== 上下バンド線の計算 =====
# 標準偏差の計算
sigma_n = df["value"].rolling(window=n).std(ddof=0)

# ±1σの計算
p1_sigma = SMA_BB_n + sigma_n
m1_sigma = SMA_BB_n - sigma_n
# ±2σの計算
p2_sigma = SMA_BB_n + sigma_n * 2
m2_sigma = SMA_BB_n - sigma_n * 2
# ±3σの計算
p3_sigma = SMA_BB_n + sigma_n * 3
m3_sigma = SMA_BB_n - sigma_n * 3

# ********** 描写 **********
fig3 = plt.figure("ボリンジャーバンド")

plt.plot(df, label="Sample")
plt.plot(SMA_BB_n, linestyle="dashed", label="SMA-" + str(n))
plt.plot(p1_sigma, c="hotpink", linestyle="dashed", label="+1σ")
plt.plot(m1_sigma, c="hotpink", linestyle="dashed", label="-1σ")
plt.plot(p2_sigma, c="aqua", linestyle="dashed", label="+2σ")
plt.plot(m2_sigma, c="aqua", linestyle="dashed", label="-2σ")
plt.plot(p3_sigma, c="lime", linestyle="dashed", label="+3σ")
plt.plot(m3_sigma, c="lime", linestyle="dashed", label="-3σ")
plt.legend()
plt.scatter(range(df.size), df)
plt.scatter(range(df.size), SMA_BB_n, marker="*")
plt.scatter(range(df.size), p1_sigma, marker="*", c="hotpink")
plt.scatter(range(df.size), m1_sigma, marker="*", c="hotpink")
plt.scatter(range(df.size), p2_sigma, marker="*", c="aqua")
plt.scatter(range(df.size), m2_sigma, marker="*", c="aqua")
plt.scatter(range(df.size), p3_sigma, marker="*", c="lime")
plt.scatter(range(df.size), m3_sigma, marker="*", c="lime")

plt.title("Bollinger Bands")
plt.grid(linestyle="dashed")

plt.show()
