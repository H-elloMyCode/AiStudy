def print_info(name, age):
    print(f'姓名: {name}, 年龄: {age}')


# print_info('小明', 18)


# print_info(18, '小明')
# print_info('小红')
# print_info('小红', 20, '女')

def print_info(name, age=18):
    print(f'姓名: {name}, 年龄: {age}')


# def print_info(age=18, name):
#     print(f'姓名: {name}, 年龄: {age}')

# print_info('小明')
# print_info('小红', 20)

def print_info(name, age, gender):
    print(f'姓名: {name}, 年龄: {age}, 性别: {gender}')


# print_info(gender='男', name='小明', age=50)
# print_info(gender='女', age=20, '小红')

def calc_sum(*args):
    """计算任意数量数字的和"""
    total = 0
    for num in args:
        total += num
    return total


# print(calc_sum(1, 2))
# print(calc_sum(1, 2, 3, 4))
# print(calc_sum())

nums = [10, 20, 30]


# print(calc_sum(*nums))

def print_user(**kwargs):
    """打印用户任意属性"""
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# print_user(name='小明', age=18)
# print_user(name='小红', age=20, score=99)

user = {'name': '小刚', 'age': 21, 'city': '北京'}


# print_user(**user)


def test(name, age=18, *args, **kwargs):
    pass


def add_item(item, lst=[]):
    lst.append(item)
    return lst


# print(add_item(1))
# print(add_item(2))

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# print(add_item(1))
# print(add_item(2))

def create_user(username, password, age=18, **kwargs):
    """
    创建用户信息
    :param username:
    :param password:
    :param age:
    :param kwargs:
    :return:
    """
    user_info = {'username': username, 'password': password, 'age': age}
    user_info.update(kwargs)
    return user_info


print(create_user('小明', '123456'))
print(create_user('小明', '123456', 21))
print(create_user('小红', 'aaaaaa', 20, gender='女', city='上海'))
