class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'姓名: {self.name}，年龄: {self.age}')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        super().show_info()
        print(f'学号: {self.student_id}')


# stu = Student('小明', 18, '2026001')
# stu.show_info()

class Animal:
    def eat(self):
        print('通用逻辑: 先洗手/清理食物')
        # 父类核心逻辑
        print('动物开始进食...')


class Dog(Animal):
    def eat(self):
        super().eat()
        print(f'金毛犬专属: 啃骨头，吃得更香!')


# dog = Dog()
# dog.eat()

class A:
    def show(self):
        print('我是 A 类的 show 方法')


class B:
    def show(self):
        print('我是 B 类的 show 方法')


class C(A, B):
    def show(self):
        # super(A, self).show()
        # super(B, self).show()
        # super(C, self).show()
        A.show(self)
        B.show(self)


# c = C()
# c.show()

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def run(self):
        print(f'{self.color} 的 {self.brand} 开始行驶（通用行驶逻辑）')


class Car(Vehicle):
    def __init__(self, brand, color, seat_count):
        super().__init__(brand, color)
        self.seat_count = seat_count

    def run(self):
        super().run()
        print(f'这是 {self.seat_count}座{self.color}的{self.brand}汽车，最高时速 120 km/h')


car = Car('特斯拉', '白色', 5)
car.run()