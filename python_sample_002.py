# ==============================================================================
# brief        pythonサンプルコード 002
#
# author       たっきん
# ==============================================================================


def func_sample_002():

    print("func_sample_002")


class Class002(object):
    """サンプル用Class 002"""

    def __init__(self, init=0):
        """コンストラクタ"""
        self.__mVal = init     # 初期化

    def my_add_func(self, val):
        """加算"""
        self.__mVal = self.__mVal + val

        return self.__mVal

    def my_sub_func(self, val):
        """減算"""
        self.__mVal = self.__mVal - val

        return self.__mVal

    def my_print_val(self):
        """表示"""
        print("value = {0}".format(self.__mVal))
