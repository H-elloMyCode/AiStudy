# class Student:
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
#     def study(self):
#         print(f'{self.name} 在学习')
#
# class Teacher:
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
#     def teach(self):
#         print(f'{self.name} 在讲课')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} 在吃饭')

    def sleep(self):
        print(f'{self.name} 在睡觉')


class Student(Person):

    def eat(self):
        print(f'{self.name} 在吃大餐')

    def study(self):
        print(f'{self.name} 在学习')


class Teacher(Person):
    def teach(self):
        print(f'{self.name} 在讲课')


class GraduateStudent(Student):
    pass
    # 编写毕业生的特有属性和方法


# stu = Student('小明', 18)
# print(stu.name)
# stu.eat()
# stu.sleep()
# stu.study()
#
# teacher = Teacher('李老师', 35)
# teacher.eat()
# teacher.sleep()
# teacher.teach()

class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.__id = '私有属性'

    def show_price(self):
        print(f'{self.name} 的价格: {self.price * 0.8} 元（打 8 折）')


class Book(Goods):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def show_book_info(self):
        self.show_price()
        # print(self.__id)
        print(f'作者: {self.author}')


class Clothes(Goods):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def show_clothes_info(self):
        self.show_price()
        print(f'尺码: {self.size}')

book = Book('Python 入门', 59, '张三')
book.show_book_info()

clothes = Clothes('T恤', 99, 'XL')
clothes.show_clothes_info()

