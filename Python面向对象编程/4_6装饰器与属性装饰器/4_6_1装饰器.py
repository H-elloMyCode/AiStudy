# import time

# def add(a, b):
#     start = time.time()
#     res = a + b
#     time.sleep(1)
#     end = time.time()
#     print(f'add 执行耗时: {end - start:.6f} 秒')
#     return res
#
# def mul(a, b):
#     start = time.time()
#     res = a * b
#     time.sleep(1.5)
#     end = time.time()
#     print(f'mul 执行耗时: {end - start:.6f} 秒')
#     return res

# print(add(1, 2))
# print(mul(3, 4))

# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} 执行耗时: {end - start:.6f} 秒')
#         return res
#     return wrapper
#
# @time_decorator # add = time_decorator(add)
# def add(a, b):
#     time.sleep(1.5)
#     return a + b
#
# @time_decorator
# def mul(a, b):
#     time.sleep(1.6)
#     return a * b

# print(add(1123123,523412))
# print(mul(1231, 2356))

# def time_decorator_with_param(decimal = 6):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             res = func(*args, **kwargs)
#             end = time.time()
#             print(f'{func.__name__} 执行耗时: {end - start:.{decimal}f} 秒')
#             return res
#         return wrapper
#     return decorator
#
# @time_decorator_with_param(decimal=3)
# def add(a, b):
#     time.sleep(1.5)
#     return a + b
#
# @time_decorator_with_param()
# def mul(a, b):
#     time.sleep(1.6)
#     return a * b
#
# # print(add(1123123,523412))
# # print(mul(1231, 2356))

# from functools import wraps
#
# def time_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} 执行耗时: {end - start:.6f} 秒')
#         return res
#     return wrapper
#
# @time_decorator
# def add(a, b):
#     """加法函数"""
#     time.sleep(1.5)
#     return a + b
#
# print(add.__name__)
# print(add.__doc__)

# import time
# from functools import wraps

# def log_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         call_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#         func_name = func.__name__
#
#         args_str = ', '.join([str(arg) for arg in args])
#         kwargs_str = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
#         all_args = ', '.join([s for s in [args_str, kwargs_str] if s])
#
#         print(f'[{call_time}] 调用函数：{func_name}({all_args})')
#         res = func(*args, **kwargs)
#         print(f'[{call_time}] 函数{func_name}返回值：{res}')
#         return res
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# @log_decorator
# def say_hello(name, msg='hello'):
#     return f'{msg}, {name}!'

# add(1, 2)
#
# say_hello('小明', msg='你好')

from functools import wraps

def permission_decorator(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role in allowed_roles:
                return func(user_role, *args, **kwargs)
            else:
                raise PermissionError(f'用户角色 {user_role} 无权限调用 {func.__name__}')
        return wrapper
    return decorator

@permission_decorator(allowed_roles=['admin', 'manager'])
def delete_user(user_role, user_id):
    return f'已删除用户 {user_id}'

print(delete_user('guest', 1001))