# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if 0 < new_age < 150:
#             self.__age = new_age
#         else:
#             print('年龄不合法!')
#
# p = Person(18)
# print(p.get_age())
# p.set_age(20)
# print(p.get_age())

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
# p = Person('小明')
# print(p.name)
# # p.name = '小红'

class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 150:
            self.__age = new_age
            print(f'年龄修改成功，当前年龄: {self.__age}')
        else:
            print(f'年龄 {new_age} 不合法（必须是 0-150 的整数），修改失败！')

# p = Person(18)
# print(p.age)
#
# p.age = -1
# print(p.age)

class Goods:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return f'￥{self.__price:.2f}'

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, str):
            new_price = float(new_price.replace('元', ''))

        if new_price > 0:
            self.__price = new_price
            print(f'价格更新为: {self.price}')
        else:
            print(f'价格 {new_price} 不合法！')


# goods = Goods(59.9)
# print(goods.price)
# # print(goods.price)
#
# goods.price = '49.9元'
# print(goods.price)
#
# goods.price = -10

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return f'账户余额: ￥{self.__balance:.2f}'

    @property
    def can_withdraw(self):
        return self.__balance > 100

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'存款 {amount} 元成功，{self.balance}')
        else:
            print(f'存款金额必须大于 0!')

account = BankAccount(1000)
print(account.balance)
print(account.can_withdraw)


account.balance = 50
account.balance = -200