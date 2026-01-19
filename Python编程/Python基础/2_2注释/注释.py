print("Hello world") # 单行注释

# print("你好") # 临时屏蔽代码

"""
多行注释
第一行
第二行
第三行
"""

def add(a, b):
    """
    功能：计算两个数的和
    :param a: 第一个加数
    :param b: 第二个加数
    :return: a + b 的结果
    """
    return a + b

help(add)