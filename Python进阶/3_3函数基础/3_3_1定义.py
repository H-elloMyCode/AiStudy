def print_welcome():
    """打印欢迎语"""
    print("欢迎学习Python函数")


# print_welcome()
# print_welcome()

# help(print_welcome)

def print_user_welcome(username):
    """
    打印指定用户的欢迎语
    :param username: 字符串，用户名
    """
    print(f'你好，{username}！欢迎使用本程序')


# print_user_welcome("小明")
# print_user_welcome("小红")

# help(print_user_welcome)

def calc_sum(a, b):
    """
    计算两个数的和
    :param a: 数字，第一个数
    :param b: 数字，第二个数
    :return: 两个数的和
    """
    return a + b


# print(calc_sum(a))
# print(f'10 + 20 = {calc_sum(10, 20)}')
# print(f'3.5 + 4.5 = {calc_sum(3.5, 4.5)}')

def calc_average(a, b, c):
    """计算三个数的平均值"""
    avg = (a + b + c) / 3
    return avg


# print(f'平均值: {calc_average(10, 20, 30)}')

def power(num, n=2):
    """
    计算数字的 n 次方，n 默认为 2
    :param num:
    :param n:
    :return:
    """
    return num ** n


# print(power(5))
# print(power(5, 3))

def test_return():
    print("第一步")
    return
    print("第二步")


# test_return()

def test_scope():
    num = 10


# print(num)

def is_leap_year(year):
    """
    判断指定年份是否为闰年
    :param year: 整数，年份
    :return: bool，True=闰年，False=平年
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2000))
print(is_leap_year(2001))