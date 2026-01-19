# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'姓名: {self.name}，年龄: {self.age}')
#
# class Learner:
#     def study(self, course):
#         print(f'{self.name} 正在学习 {course}')
#
# class Student(Person, Learner):
#
#     def exam(self):
#         print(f'{self.name} 参加考试，年龄: {self.age}')

# stu = Student('小明', 18)
# stu.exam()
# stu.show_info()
# stu.study('Python')

class A:
    def show(self):
        print('我是 A 类的 show 方法')


class B:
    def show(self):
        print('我是 B 类的 show 方法')


class C(A, B):
    def show(self):
        print('我是 C 类的 show 方法（统一逻辑）')
        A.show(self)
        B.show(self)


# c = C()
# c.show()
#
# print(C.__mro__)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Learner:
#     def __init__(self, course):
#         self.course = course
#
#
# class Student(Person, Learner):
#     def __init__(self, name, course):
#         Person.__init__(self, name)
#         Learner.__init__(self, course)

# stu = Student('小明', 'Python')
# print(stu.name)
# print(stu.course)

class Person:
    def __init__(self, name):
        self.name = name


class Learner:
    def study(self, course):
        print(f'学习 {course}')


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.learner = Learner()

    def study(self, course):
        print(f'{self.name}: ', end='')
        self.learner.study(course)

# stu = Student('小明')
# stu.study('Python')

class Car:
    def run(self):
        print('在公路上行驶')

    def fuel(self):
        print('消耗汽油')

class Airplane:
    def fly(self):
        print('在天空飞行')
    def fuel(self):
        print('消耗航空汽油')

class FlyingCar(Car, Airplane):
    def __init__(self, brand):
        self.brand = brand

    def fuel(self):
        print(f'{self.brand} 飞行汽车: ')
        print('-> 行驶时: ', end='')
        Car.fuel(self)
        print('-> 飞行时: ', end='')
        Airplane.fuel(self)

flying_car = FlyingCar('特斯拉')
flying_car.run()
flying_car.fly()
flying_car.fuel()