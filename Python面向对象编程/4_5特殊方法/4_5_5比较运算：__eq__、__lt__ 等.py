import functools

@functools.total_ordering
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price == other.price) and (self.name == other.name)

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        if self.price != other.price:
            return self.price < other.price
        return self.name < other.name

# p1 = Product('保温杯', 99.9)
# p2 = Product('水杯', 99.9)
# p3 = Product('水壶', 199.9)

# p1 = Product('保温杯A', 99.9)
# p2 = Product('保温杯B', 99.9)
#
# print(p1 < p2)

# print(p1 == p2)

# print(p1 <= p2)
# print(p3 >= p2)

# print(p1 < p2)
# print(p2 < p1)
#
# print(p2 < p3)
#
# print(p3 > p1)

# print(p1 <= p2)
# print(p1 >= p2)

#
# print(p1 == p2)
# print(p2 == p3)
#
# print(p1 != p3)

# print(p1 > p2)

@functools.total_ordering
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name}（分数: {self.score}）'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score == other.score

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score < other.score

stu1 = Student('小明', 85)
stu2 = Student('小红', 90)
stu3 = Student('小刚', 85)

# print(f'{stu1} == {stu3}：{stu1 == stu3}')
# print(f'{stu1} == {stu2}：{stu1 == stu2}')
# print(f'{stu1} < {stu2}：{stu1 < stu2}')
# print(f'{stu2} > {stu1}：{stu2 > stu1}')
# print(f'{stu1} <= {stu3}：{stu1 <= stu3}')

students = [stu2, stu1, stu3]
print('排序前：', [str(s) for s in students])
sorted_students = sorted(students)
print('排序后：', [str(s) for s in sorted_students])