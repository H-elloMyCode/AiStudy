# class Person:
#     def __init__(self, age):
#         self._age = age
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, value):
#         if value < 0:
#             raise ValueError('年龄不能为负数')
#         self._age = value

# p = Person(18)
# print(p.get_age())
# p.set_age(20)
# print(p.get_age())

# p = Person(18)
# print(p.age)
# p.age = -20
# print(p.age)

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('年龄必须是整数')
        if value <0 or value > 150:
            raise ValueError('年龄必须在 0 - 150 之间')

        self.__age = value

    @age.deleter
    def age(self):
        print('执行删除 age 的逻辑: 清理年龄数据')
        del self.__age

# p = Person(18)
# print(p.age)
# del p.age
# print(p.age)

# p = Person(18)
# print(p.age)
# p.age = 20
# print(p.age)
# p.age = -10
# print(p.age)

# p = Person(18)
# print(p.age)
# p.age = 20

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

# rect = Rectangle(5, 3)
# print(rect.area)
#
# rect.width = 6
# print(rect.area)

class Product:
    def __init__(self, price):
        self.__price = price
        self.__discount = 0

    @property
    def price(self):
        return self.__price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('折扣必须是数字')
        if value < 0 or value > self.__price:
            raise ValueError(f'折扣不能为负, 且不能超过原价 {self.__price}')

        self.__discount = value

    @property
    def pay_price(self):
        return max(0, self.__price - self.__discount)

p = Product(99.9)
print(f'原价: {p.price}')
print(f'实付金额: {p.pay_price}')

print(p.discount)
p.discount = 20
print(f'折扣后实付: {p.pay_price}')

# p.price = 80
