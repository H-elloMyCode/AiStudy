# class Person:
#     def __init__(self, name, age, id_card):
#         self.name = name
#         self.__age = age
#         self.__id_card = id_card
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄修改为: {new_age}')
#         else:
#             print(f'年龄 {new_age} 不合法')
#
#     def show_info(self):
#         print(f'姓名: {self.name}，年龄: {self.__age}，身份证: {self.__id_card}')

# p = Person('小明', 18, '110101200601011234')

# print(p.name)
# print(p.__age)
# print(p._Person__age)

# print(p._Person__age)
# p._Person__age = -1
# print(p.get_age())

# print(p.get_age())
# p.set_age(20)
# print(p.get_age())
# p.set_age(-1)
# print(p.get_age())

# p.show_info()

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __check_amount(self, amount):
        if not isinstance(amount, (int, float)):
            return False
        return amount > 0

    def deposit(self, amount):
        if self.__check_amount(amount):
            self.__balance += amount
            print(f'存款 {amount} 元成功，当前余额: {self.__balance}')
        else:
            print('存款金额不合法')

    def withdraw(self, amount):
        if self.__check_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            print(f'取款 {amount} 元成功，当前余额: {self.__balance}')
        else:
            print('取款金额不合法或余额不足！')

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)

# account.__check_amount(2000)

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Student(Person):
    def show_parent_attr(self):
        # print(self.__name)
        print(f'父类私有属性 name: {self.get_name()}')

stu = Student('小明')
# stu.show_parent_attr()

class Order:
    def __init__(self, order_id, total_amount):
        self.__order_id = order_id
        self.__total_amount = total_amount
        self.__status = '待支付'

    def __check_status(self):
        if self.__status != '待支付':
            print(f'订单 {self.__order_id} 状态为: {self.__status}， 无法操作')
            return False
        return True

    def pay(self, amount):
        if not self.__check_status():
            return
        if amount == self.__total_amount:
            self.__status = '已支付'
            print(f'订单 {self.__order_id} 支付成功，状态更新为: {self.__status}')
        else:
            print(f'支付金额 {amount} 与订单金额 {self.__total_amount} 不符')

    def get_order_info(self):
        return {'order_id': self.__order_id, 'total_amount': self.__total_amount, 'status': self.__status}

order = Order('2026001', 199)
print(order.get_order_info())

order.pay(199)
order.pay(199)