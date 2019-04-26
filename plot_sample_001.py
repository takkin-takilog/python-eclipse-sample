# ==============================================================================
# brief        指数関数描写アニメーション
#
# author       たっきん
# ==============================================================================
import math
from matplotlib import animation
import matplotlib.pyplot as plt


x_ax = []
y_ax = []


def myfunc(x): return math.e ** x


def init_anim():
    x = 0
    x_ax.append(x)
    y_ax.append(myfunc(x))
    print("init")


def update_anim(i, interval):

    x = x_ax[-1] + interval / 1000
    x_ax.append(x)
    y_ax.append(myfunc(x))
    print("[{0}]:x = {1:.3f}, y = {2:.3f}" .format(i, x_ax[-1], y_ax[-1]))

    plt.cla()   # プロットクリア
    plt.plot(x_ax, y_ax, marker="o")    # プロット
    plt.grid()  # グリッド表示
    plt.title(r"$y = e^x$ (count = %s)" % (i))  # グラフタイトル
    plt.xlabel("x [sec]")  # グラフ横軸タイトル
    plt.ylabel("y")  # グラフ縦軸タイトル


if __name__ == '__main__':

    disp_time = 5000  # 表示時間[msec]
    disp_hz = 10  # 更新周期

    # 描画
    fig = plt.figure()

    interval = int(1000 / disp_hz)  # グラフ更新間隔[msec]
    frames = int(disp_time / interval)  # グラフ更新回数
    ani = animation.FuncAnimation(fig,
                                  func=update_anim,
                                  frames=frames,
                                  init_func=init_anim,
                                  fargs=(interval,),
                                  interval=interval,
                                  repeat=False,
                                  blit=False)

    plt.show()
