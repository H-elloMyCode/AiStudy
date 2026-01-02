# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f'{self.name} 在吃饭')
#
#     def sleep(self):
#         print(f'{self.name} 在睡觉')
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def eat(self):
#         print(f'学生 {self.name} 在食堂吃饭, 学号: {self.student_id}')
#
#     def study(self, course):
#         print(f'学号 {self.student_id} 的 {self.name} 正在学习 {course}')
#
#
#
# stu = Student('小明', 18, '2026001')
# stu.study('Python')

# stu.eat()
# stu.sleep()

# print(f'姓名：{stu.name}，年龄：{stu.age}，学号：{stu.student_id}')
# stu.eat()

# stu = Student('小明', 18)
# print(stu.name)
# stu.eat()
# stu.sleep()


class Animal:
    def move(self):
        print(f'动物在移动')

class Dog(Animal):
    def bark(self):
        print('狗在叫')

# dog = Dog()
# dog.move()
# dog.bark()

class Person:
    def __init__(self, name):
        self.__id_card = '123456'
        self.name = name

    def __private_method(self):
        print('父类私有方法')

class Student(Person):
    def get_info(self):
        # print(self.__id_card)
        # self.__private_method()
        print(f'姓名: {self.name}')

# stu = Student('小明')
# stu.get_info()

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def run(self):
        print(f'{self.color} 的 {self.brand} 在行驶')

class Car(Vehicle):
    def __init__(self, brand, color, seat_count):
        super().__init__(brand, color)
        self.seat_count = seat_count

    def run(self):
        print(f'{self.color} 的 {self.brand} 汽车（{self.seat_count}座）在公路上行驶')

    def honk(self):
        print(f'{self.brand} 汽车鸣笛: 滴滴!!')

class Bicycle(Vehicle):
    def __init__(self, brand, color, type_):
        super().__init__(brand, color)
        self.type_ = type_

    def run(self):
        print(f'{self.color} 的 {self.brand}{self.type_} 自行车在非机动车道行驶')

car = Car('特斯拉', '白色', 5)
car.run()
car.honk()

bicycle = Bicycle('捷安特', '黑色', '山地')
bicycle.run()