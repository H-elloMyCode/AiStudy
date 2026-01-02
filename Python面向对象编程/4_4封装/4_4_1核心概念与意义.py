# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p = Person('小明', 18)
#
# p.age = -20
# # print(p.age)

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
#         else:
#             print(f'年龄 {new_age} 不合法，修改失败！')
#
#     def show_info(self):
#         print(f'姓名：{self.__name}，年龄：{self.__age}')
#
# p = Person('小明', 18)
# print(p.get_name())
# print(p.get_age())

# p.set_age(20)
# print(p.get_age())
# p.show_info()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 150:
            self.__age = new_age
        else:
            print(f'年龄 {new_age} 不合法，修改失败！')

    def show_info(self):
        print(f'姓名：{self.__name}，年龄：{self.__age}')

# p = Person('小明', 18)
# print(p.name)
# print(p.age)
#
# p.age = 20
# print(p.age)

class BankAccount:
    def __init__(self, account_num, balance):
        self.__account_num = account_num
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'存款 {amount} 元成功，当前余额: {self.__balance}')
        else:
            print('存款金额必须大于 0')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'取款 {amount} 元成功，当前余额: {self.__balance}')
        else:
            print('取款金额不合法或余额不足！')

account = BankAccount('6228480402564890', 1000)
print(account.balance)

account.deposit(500)
account.withdraw(300)
account.withdraw(1199)

# account.__balance = 1000000
# print(account.__balance)
# print(account.__balance
print(account.balance)
print(account._BankAccount__balance)

account._BankAccount__balance = 1000000
# print(account.balance)