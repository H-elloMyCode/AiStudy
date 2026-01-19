# class Dog:
#     def __init__(self):
#         self.name = '无名小狗'
#         self.age = 1
#
#     def show_info(self):
#         print(f'名字: {self.name}, 年龄: {self.age} 岁')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'名字: {self.name}, 年龄: {self.age} 岁')

# dog1 = Dog()
# dog1.show_info()
# dog2 = Dog('旺财', 3)
# dog3 = Dog('小白', 2)
# dog2.show_info()
# dog3.show_info()

# class Dog:
#     def __init__(self, name='无名小狗', age=1):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'名字: {self.name}, 年龄: {self.age} 岁')

# dog4 = Dog()
# dog4.show_info()

# dog5 = Dog('来福')
# dog6 = Dog(age=4)
# dog7 = Dog('大黄', 5)
#
# dog5.show_info()
# dog6.show_info()
# dog7.show_info()

# class Dog:
#     def __init__(self, name='无名小狗', age=1):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'名字: {self.name}, 年龄: {self.age} 岁')

# dog_a = Dog('旺财', 3)
# dog_b = Dog('小白', 2)
#
# dog_a.age = 4
#
# print(dog_a.age)
# print(dog_b.age)


# class Dog:
#     def __init__(self, name='无名小狗', age=1):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'名字: {self.name}, 年龄: {self.age} 岁')
#
# dog = Dog('旺财', 3)
#
# dog.color = '黄色'
# print(f'{dog.name} 的颜色: {dog.color}')
#
# def bark(self):
#     print(f'{self.name} 在叫: 汪汪汪!')
#
# Dog.bark = bark
# dog.bark()

class Dog:
    def __init__(self, name='无名小狗', age=1):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'名字: {self.name}, 年龄: {self.age} 岁')

# Dog()

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_pass(self):
        return self.score >= 60

students = [
    Student('小明', 85),
    Student('小红', 59),
    Student('小刚', 92),
    Student('小丽', 78)
]

for stu in students:
    result = '及格' if stu.is_pass() else '不及格'
    print(f'姓名：{stu.name}，分数：{stu.score}，结果：{result}')