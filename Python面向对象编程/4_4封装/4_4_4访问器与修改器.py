# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄修改成功，当前年龄: {self.__age}')
#         else:
#             print(f'年龄 {new_age} 不合法（必须是 0-150 的整数），修改失败！')
#
# p = Person('小明', 18)
# print(p.get_name())
# print(p.get_age())
#
# p.set_age('25')
# print(p.get_age())
#
# p.__age = 30
# print(p.get_age())

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄修改成功，当前年龄: {self.__age}')
#         else:
#             print(f'年龄 {new_age} 不合法（必须是 0-150 的整数），修改失败！')
#
# p = Person('小明', 18)
# print(p.name)
# print(p.age)
#
# p.age = 20
# print(p.age)

class Goods:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            print(f'价格 {new_price} 必须是数字!')
            return
        if new_price <= 0:
            print(f'价格 {new_price} 必须大于0!')
            return

        self.__price = new_price
        print(f'《{self.__name}》价格更新为: {self.__price}')


goods = Goods('Python入门教程', 59.9)

print(goods.name)
print(goods.price)

goods.price = '50'
print(goods.price)