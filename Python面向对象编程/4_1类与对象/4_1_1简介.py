class Calculator:
    def __init__(self, num1, num2):
        print("__init__ 调用了")
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

calc = Calculator(10, 5)
print(f'10 + 5 = {calc.add()}')
print(f'10 - 5 = {calc.sub()}')
print(f'10 * 5 = {calc.mul()}')

class Student:
    # 初始化方法
    school = '第一中学'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show_info(self):
        print(f'姓名: {self.name}, 年龄: {self.__age}')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self.__age = new_age
        else:
            print('年龄不合法')

    def study(self, course):
        print(f'{self.name} 正在学习 {course}')


stu1 = Student('小明', 18)
stu2 = Student('小红', 19)

# print(Student.school)
#
# print(stu1.school)
# print(stu2.school)
#
# Student.school = '第五中学'
# print(Student.school)
# print(stu1.school)
# print(stu2.school)

# print(stu2.get_age())
# stu1.set_age(149)
# print(stu1.get_age())

# print(stu1.name)
# print(stu2.age)

# stu1.show_info()
# stu2.study('Python')
