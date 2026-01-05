numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num

# print(total)

numbers = [1, 2, 3, 4]
total = sum(filter(lambda x: x % 2 == 0, numbers))


# print(total)

def add(x, y):
    return x + y


f = add


# print(f(1, 2))

def calculate(func, a, b):
    return func(a, b)


# print(calculate(add, 3, 4))

def make_adder(n):
    def adder(x):
        return x + n

    return adder


add5 = make_adder(5)


# print(add5(10))

def pure_add(x, y):
    return x + y


lst = [1, 2]


def impure_append(x):
    lst.append(x)
    return lst


# print(impure_append(3))
# print(lst)

nums = [1, 2, 3]
nums[0] = 10
# print(nums)

nums = [1, 2, 3]
new_nums = [10] + nums[1:]
# print(nums)
# print(new_nums)

nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))


# print(squares)

def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1)


# print(sum_recursive(4))

def add_one(x):
    return x + 1


def multiply_two(x):
    return x * 2


def square(x):
    return x ** 2


def compose(f1, f2, f3):
    def wrapper(x):
        return f3(f2(f1(x)))

    return wrapper


my_func = compose(add_one, multiply_two, square)
# print(my_func(3))

from functools import reduce, lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(10))

numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y, map(lambda x : x * 3, filter(lambda x: x % 2 == 1, numbers)))

print(result)