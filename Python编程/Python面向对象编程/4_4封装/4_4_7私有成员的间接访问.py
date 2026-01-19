# class Person:
#     def __init__(self, name, age, id_card):
#         self.__name = name
#         self.__age = age
#         self.__id_card = id_card
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_card(self):
#         return f'{self.__id_card[:6]}********{self.__id_card[-4:]}'
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄已更新为: {self.__age}')
#         else:
#             print(f'年龄 {new_age} 不合法，修改失败！')
#
# p = Person('小明', 18, '110101200601011234')
#
# print(p.get_name())
# print(p.get_id_card())
#
# print(p.get_age())
# p.set_age(21)
# print(p.get_age())


# class Person:
#     def __init__(self, name, age, id_card):
#         self.__name = name
#         self.__age = age
#         self.__id_card = id_card
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def id_card(self):
#         return f'{self.__id_card[:6]}********{self.__id_card[-4:]}'
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄已更新为: {self.__age}')
#         else:
#             print(f'年龄 {new_age} 不合法，修改失败！')
#
# p = Person('小明', 18, '110101200601011234')
#
# print(p.name)
# print(p.id_card)
#
# print(p.age)
# p.age = 21
# print(p.age)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __check_amount(self, amount):
        if not isinstance(amount, (int, float)):
            return False, '金额必须是数字'
        if amount <= 0:
            return False, '金额必须大于 0'
        return True, '校验通过'

    def deposit(self, amount):
        is_valid, msg = self.__check_amount(amount)
        if not is_valid:
            print(f'存款失败')
            return
        self.__balance += amount
        print(f'存款 {amount} 元成功，当前余额: {self.__balance}')

    def withdraw(self, amount):
        is_valid, msg = self.__check_amount(amount)
        if not is_valid:
            print(f'取款失败: {msg}')
            return
        if amount > self.__balance:
            print('取款失败: 余额不足')
            return
        self.__balance -= amount
        print(f'取款 {amount} 元成功，当前余额: {self.__balance}')

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)
#
# account.withdraw(-200)
# account.__check_amount(1000)

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.__student_id = student_id

    def show_info(self):
        parent_name = self.get_name()
        print(f'姓名: {parent_name}，学号: {self.__student_id}')

# stu = Student('小明', '2026001')
# stu.show_info()

class Order:
    def __init__(self, order_id, total_amount):
        self.__order_id = order_id
        self.__total_amount = total_amount
        self.__status = '待支付'

    def __check_status(self, targe_status):
        allowed_status = ['待支付', '已支付', '已取消', '已发货']
        if targe_status not in allowed_status:
            return False, f'状态 {targe_status} 不合法'
        if self.__status == '已取消' and targe_status != '待支付':
            return False, '已取消的订单无法修改为其他状态'
        return True, '校验通过'

    @property
    def order_id(self):
        return self.__order_id

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        is_valid, msg = self.__check_status(new_status)
        if not is_valid:
            print(f'修改状态失败: {msg}')
            return
        self.__status = new_status
        print(f'订单 {self.__order_id} 状态更新为: {new_status}')

    def pay(self):
        is_valid, msg = self.__check_status('已支付')
        if not is_valid:
            print(f'支付失败: {msg}')
            return
        if self.__status != '待支付':
            print(f'支付失败：当前订单状态为: {self.__status}')
            return

        self.__status = '已支付'
        print(f'订单 {self.__order_id} 支付成功！')

order = Order('2026001', 199.9)
print(order.order_id)
print(order.total_amount)
print(order.status)

# order.status = '已取消'
# order.status = '已发货'
order.pay()
print(order.status)