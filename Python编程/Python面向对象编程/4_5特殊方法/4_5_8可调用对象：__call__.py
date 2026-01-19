class Calculator:
    def __init__(self, op):
        self.op = op

    def __call__(self, a, b):
        if self.op == 'add':
            return a + b
        elif self.op == 'sub':
            return a - b
        elif self.op == 'mul':
            return a * b
        raise ValueError(f'不支持的运算: {self.op}')

    # def run(self, a, b):
    #     if self.op == 'add':
    #         return a + b
    #     elif self.op == 'sub':
    #         return a - b

# add_calc = Calculator('add')
# print(add_calc(1, 2))
#
# mul_calc = Calculator('mul')
# print(mul_calc(100, 100))
#
# print(callable(add_calc))
# print(callable(123))

# add_calc = Calculator('sub')
# print(add_calc.run(1, 2))

# add_calc(1, 2)

class CountDecorator:
    def __init__(self):
        self.count = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.count += 1
            print(f'函数 {func.__name__} 已调用 {self.count} 次')
            return func(*args, **kwargs)

        return wrapper

# counter = CountDecorator()
#
# @counter
# def add(a, b):
#     return a + b
#
# add(1, 2)
# add(3, 4)
# add(5, 6)
#
# print(f'add 函数总调用次数: {counter.count}')

class CartChecker:
    def __init__(self):
        self.goods = []

    def add_goods(self, name, price, num):
        self.goods.append((name, price, num))

    def __call__(self):
        if not self.goods:
            return 0.0
        total = sum(price * num for _,price, num in self.goods)
        print(f'购物车商品: {[name for name,_,_ in self.goods]}')
        return total

cart = CartChecker()

cart.add_goods('苹果', 5.99, 3)
cart.add_goods('香蕉', 3.99, 2)

total_price = cart()
print(total_price)

print(type(cart))