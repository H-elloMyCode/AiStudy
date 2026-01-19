# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.score = 0
#
#     def set_score(self, new_score):
#         self.score = new_score
#
# stu = Student('小明', 18)
# print(stu.score)
# stu.set_score(100)
# print(stu.score)

# stu1 = Student('小明', 18)
# stu2 = Student('小红', 19)
#
# stu1.gender = '男'
# print(stu1.gender)
# print(stu2.gender)

# print(stu1.name)
# print(stu2.age)
# print(stu1.score)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'姓名: {self.name}, 年龄: {self.age}')
#
# stu = Student('小明', 18)
# stu.show_info()

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self, course):
#         print(f'{self.name} 正在学习 {course}')
#
# stu = Student('小红')
# stu.study('Python')
# stu.study('数学')

class Student:
    def __init__(self, name, chinese, math):
        self.name = name
        self.chinese = chinese
        self.math = math

    def get_total_score(self):
        total = self.chinese + self.math
        return total

# stu = Student('小刚', 90, 95)
# print(f'{stu.name} 总分: {stu.get_total_score()}')

class Phone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def reduce_price(self, amount):
        self.price -= amount

phone1 = Phone('Mate 60 Pro', 6999)
phone2 = Phone('iPhone 15', 7999)

# print(phone1.price)
# print(phone2.price)
# phone1.reduce_price(500)
# print(phone1.price)
# print(phone2.price)

class Test:
    class_attr = '类属性'
    def __init__(self):
        self.instance_attr = '实例属性'

# obj1 = Test()
# obj2 = Test()
# print(obj1.class_attr)
# print(obj2.class_attr)
# print(obj1.instance_attr)
# print(obj2.instance_attr)
# Test.class_attr = '修改类属性'
# print(obj1.class_attr)
# print(obj2.class_attr)

class ShoppingCart:
    def __init__(self, username):
        self.username = username
        self.goods = []
        self.total_price = 0

    def add_goods(self, goods_name, price):
        self.goods.append(goods_name)
        self.total_price += price
        print(f'[{self.username}] 添加商品: {goods_name}, 单价: {price}')

    def show_cart(self):
        print(f'\n[{self.username}] 的购物车: ')
        print(f'商品列表: {self.goods}')
        print(f'总价: {self.total_price} 元')

cart1 = ShoppingCart('小明')
cart2 = ShoppingCart('小红')

cart1.add_goods('Python教程', 89)
cart1.add_goods('鼠标', 59)
cart2.add_goods('口红', 199)

cart1.show_cart()
cart2.show_cart()