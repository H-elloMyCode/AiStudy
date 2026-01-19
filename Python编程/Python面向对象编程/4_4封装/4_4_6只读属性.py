# class Person:
#     def __init__(self, name, id_card):
#         self.__name = name
#         self.__id_card = id_card
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_card(self):
#         return self.__id_card

class Person:
    def __init__(self, name, id_card):
        self.__name = name
        self.__id_card = id_card

    @property
    def name(self):
        return self.__name

    @property
    def id_card(self):
        return self.__id_card

p = Person('小明', '110101200601011234')

# print(p.name)
# p.name = '小红'

# print(p.id_card)

#
# print(p.get_name())
# print(p.get_id_card())

class Order:
    def __init__(self, order_id, create_time, total_amount):
        self.__order_id = order_id
        self.__create_time = create_time
        self.__total_amount = total_amount
        self.__status = '待支付'

    @property
    def order_id(self):
        return self.__order_id

    @property
    def create_time(self):
        return self.__create_time

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        allowed_status = ['待支付', '已支付', '已取消', '已发货']
        if new_status in allowed_status:
            self.__status = new_status
            print(f'订单 {self.__order_id} 状态更新为: {new_status}')
        else:
            print(f'状态 {new_status} 不存在！')

order = Order('2026001', '2026-01-01 10:00:00', 199.9)

# print(order.order_id)
# print(order.create_time)
# print(order.total_amount)
# print(order.status)
#
# order.status = '已支付'
# print(order.status)

class Student:
    def __init__(self, scores):
        self.__scores = scores

    @property
    def scores(self):
        return self.__scores.copy()

stu = Student([90, 80, 70])
print(stu.scores)

stu.scores[0] = 100
print(stu.scores)