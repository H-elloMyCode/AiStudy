def calc_sum(a, b):
    total = a + b
    return total


result = calc_sum(10, 20)


# print(f'10 + 20 = {result}')

# print(f'10 + 20 = {calc_sum(10, 20)}')

def print_hello():
    print("Hello")


# res = print_hello()
# print(res)

def calc_sum_diff(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val


sum_res, diff_res = calc_sum_diff(20, 10)
# print(f'和: {sum_res}, 差: {diff_res}')

res_tuple = calc_sum_diff(20, 10)


# print(res_tuple)
# print(f'和: {res_tuple[0]}, 差: {res_tuple[1]}')

def is_positive(num):
    if num > 0:
        return True
    return False


# print(is_positive(5))
# print(is_positive(-3))

def check_age(age):
    if age < 18:
        print('未成年，禁止访问')
        return
    print('已成年，可以访问')


# check_age(18)
# check_age(16)

def filter_even(nums):
    even_lst = [x for x in nums if x % 2 == 0]
    return even_lst


lst = [1, 2, 3, 4, 5]


# print(f'偶数列表: {filter_even(lst)}')

def get_calc_func(type):
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    if type == 'add':
        return add
    else:
        return mul


add_func = get_calc_func(',')


# print(add_func(5, 7))

def get_list():
    lst = [1, 2, 3]
    return lst.copy()


res_lst = get_list()
res_lst.append(4)


# print(res_lst)

def parse_num_range(input_str):
    """
    解析用户输入的数字范围
    :param input_str:
    :return:
    """
    if '-' not in input_str:
        print('格式错误')
        return None, None
    parts = input_str.split('-')
    try:
        min_num = int(parts[0].strip())
        max_num = int(parts[1].strip())
    except ValueError:
        print("输入的不是数字")
        return None, None

    if min_num > max_num:
        min_num, max_num = max_num, min_num
    return min_num, max_num


input_str = input("请输入数字范围：(格式：min-max)").strip()
min_val, max_val = parse_num_range(input_str)
if min_val is not None:
    print(f'解析结果：最小值={min_val}，最大值={max_val}')
else:
    print('解析失败')
