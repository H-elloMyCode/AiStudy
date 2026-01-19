class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # def __str__(self):
    #     return f'商品: {self.name}, 价格: ￥{self.price:.2f}'
    #     # return 1

    # def __repr__(self):
    #     return f'Product(name="{self.name}", price={self.price})'

# p = Product('保温杯', 99.9)
# print(p)
# print(str(p))
# print(repr(p))

# p2 = eval(repr(p))
# print(p)

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f'学生：{self.name}（学号：{self.student_id}），年龄：{self.age}岁'

    # def __repr__(self):
    #     return f'Student(name="{self.name}", age={self.age}, student_id="{self.student_id}")'
    def __repr__(self):
        return self.__str__()

stu = Student('小明', 18, '2026001')

print(stu)
print(repr(stu))

# stu2 = eval(repr(stu))
# print(stu2)