# ==============================================================================
# brief        閏年判定
#
# author       たっきん
# ==============================================================================


def judge_leap_yaer():

    while True:

        try:

            # 西暦の入力
            print("西暦を入力してください = ")
            year = int(input())
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(" {0}年は閏年です。"      .format(year))
                    else:
                        print(" {0}年は閏年ではありません。" .format(year))
                else:
                    print(" {0}年は閏年です。"                .format(year))
            else:
                print(" {0}年は閏年ではありません。"                .format(year))

        except ValueError:
            print("Error:数字以外が入力されました。")


if __name__ == '__main__':
    judge_leap_yaer()
