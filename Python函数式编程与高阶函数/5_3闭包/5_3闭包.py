# def outer():
#     a = 10
#     def inner():
#         print(a)
#     inner()
#
# outer()

# def outer():
#     a = 10
#     def inner():
#         print(a)
#     return inner
#
# f = outer()
# f()

# def counter(initial):
#     count = initial
#
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# counter1 = counter(0)
# print(counter1())
# print(counter1())
# print(counter1())
#
# counter2 = counter(10)
# print(counter2())
# print(counter2())
# print(counter1())

def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

# chinese_greet = make_greeter('你好')
# print(chinese_greet("小明"))
#
# englist_greet = make_greeter("Hello")
# print(englist_greet("Tom"))

class Counter:
    def __init__(self, initial):
        self.count = initial

    def increment(self):
        self.count += 1
        return self.count

def counter(initial):
    count = initial
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# counter1 = Counter(0)
# counter1.increment()
# print(counter1.count)
# counter1.increment()
# print(counter1.count)
# counter1.increment()
# print(counter1.count)
#
# print("===============================")
#
# counter2 = counter(0)
# print(counter2())
# print(counter2())
# print(counter2())

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行耗时：{end - start:.4f} 秒")
        return result
    return wrapper

@timer_decorator
def show_function():
    time.sleep(1)

# show_function()

def outer():
    lst = [1, 2]
    def inner():
        lst.append(3)
        print(lst)
    return inner

f = outer()
f()
f()
f()

f = None
