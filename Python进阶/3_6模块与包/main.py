# import calculator as calc

# from calculator import *

# print(f'圆周率: {calc.PI}')
# print(f'10 + 20 = {calc.add(10, 20)}')
# print(f'10 * 20 = {calc.mul(10, 20)}')

# print(f'圆周率: {PI}')

# import my_tools.calculator as calc
# import my_tools.logger as log

# from my_tools.calculator import mul
# from my_tools.logger import write_log
#
# print(mul(10, 20))
# write_log('计算完成')

import math
import random
import datetime

# print(f'10 的平方根, {math.sqrt(10)}')
# print(f'1-100 的随机数: {random.randint(1, 100)}')
# print(f'当前时间: {datetime.datetime.now()}')

import requests

res = requests.get('https://www.baidu.com')
print(f'请求状态码: {res.status_code}')
