# ==============================================================================
# brief        pythonサンプルコード 001
#
# author       たっきん
# ==============================================================================

import python_sample_002 as ps002
import python_sample_003 as ps003


def func_sample_001():

    ps003.func_sample_003()

    print("func_sample_001")


if __name__ == '__main__':
    func_sample_001()

    ps002.func_sample_002()

    clsAddSub01 = ps002.ClassAddSub()

    clsAddSub01.my_add_func(2)     # 加算処理

    clsAddSub01.my_sub_func(1)     # 減算処理

    clsAddSub01.my_ct_instance.my_test_print_func()
