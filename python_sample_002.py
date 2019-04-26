# ==============================================================================
# brief        pythonサンプルコード 002
#
# author       たっきん
# ==============================================================================


class ClassTest(object):
    """テスト用Class 002"""

    def my_test_print_func(self):
        print("this is TEST PRINT")


class ClassAddSub(object):
    """加算減算Class 002"""

    my_ct_instance = ClassTest()  # ClassTestのインスタンス

    def __init__(self, init=0):
        """コンストラクタ"""
        self.__mTest = init     # 初期化

    def my_add_func(self, val=10):
        """加算"""
        self.__mTest = self.__mTest + val

        return self.__mTest

    def my_sub_func(self, val):
        """減算"""
        self.__mTest = self.__mTest - val

        return self.__mTest

    def my_print_val(self):
        """表示"""
        print("value = {0}"   .format(self.__mTest))


def func_sample_002():

    clsAddSub02 = ClassAddSub()  # ClassAddSubのインスタンス

    clsAddSub02.my_add_func(10)

    print("func_sample_002")
