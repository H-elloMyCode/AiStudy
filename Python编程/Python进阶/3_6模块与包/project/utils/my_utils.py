"""
    自定义工具模块：包含常用的数学计算函数和工具类
    功能：
        1. 提供PI、MAX_NUM等常量；
        2. 提供add、mul、is_positive等工具函数；
        3. 提供Calculator计算器类。
"""

PI = 3.1415926
MAX_NUM = 1000


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def is_positive(num):
    return num > 0


class Calculator:
    def __init__(self, base=0):
        self.base = base

    def add_base(self, num):
        return self.base + num

if __name__ == '__main__':
    # 测试
    print(f'测试 add 函数: ', add(1, 2))
    print(f'测试 mul 函数: ', add(2, 2))

    calc = Calculator(base=5)
    print(calc.add_base(105))