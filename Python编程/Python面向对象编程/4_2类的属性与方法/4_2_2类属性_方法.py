class Student:
    school = '第一中学'
    def __init__(self, name, age):
        self.name = name
        self.age = age



# print(Student.school)
#
stu1 = Student('小明', 18)
stu2 = Student('小红', 19)

stu1.school = '新学校'
# print(Student.school)
# print(stu2.school)
# print(stu1.school)

# stu1.school = '第二中学'
# print(stu1.school)
# print(stu2.school)
# print(Student.school)

# print(stu1.school)
# print(stu2.school)
#
# Student.school = '第十中学'
# print(stu1.school)
# print(stu2.school)

# class Student:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
# stu1 = Student('小明')
# stu2 = Student('小红')
# stu3 = Student('小刚')
# print(f'创建了 {Student.count} 个学生对象')

# class Student:
#     school = '第一中学'
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
#     @classmethod
#     def set_school(cls, new_school):
#         cls.school = new_school
#
#     @classmethod
#     def get_student_count(cls):
#         return cls.count
#
# Student.set_school('第五十中学')
# print(Student.school)
#
# stu = Student('小明')
# stu.set_school('第三中学')
# print(Student.school)
#
# print(f'学生数量: {Student.get_student_count()}')

class Phone:
    brand = '未知品牌'
    def __init__(self, model, price):
        self.model = model
        self.price = price

    @classmethod
    def create_cheap_phones(cls, count):
        phones = []
        for i in range(count):
            model = f'低价机型{i + 1}'
            price = 999
            phones.append(cls(model, price))

        return phones

# cheap_phones = Phone.create_cheap_phones(50)
# for phone in cheap_phones:
#     print(f'型号: {phone.model}, 价格: {phone.price}')
#


class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# print(MathUtils.add(10, 20))
# print(MathUtils.is_even(9))
#
# obj = MathUtils()
# print(obj.add(100, 200))
# print(obj.is_even(10))

class Book:
    total_books = 0
    default_category = '未分类'

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.category = Book.default_category

        Book.total_books += 1

    def show_info(self):
        print(f'书名: {self.title}, 作者: {self.author}, 分类: {self.category}, 价格: {self.price}')

    @classmethod
    def set_default_category(cls, new_category):
        cls.default_category = new_category

    @classmethod
    def get_total_books(cls):
        return f'当前图书总数: {cls.total_books} 本'

    @staticmethod
    def is_expensive(price):
        return price > 100

Book.set_default_category('文学类')

book1 = Book('红楼梦', '曹雪芹', 59)
book2 = Book('三体', '刘慈欣', 89)
book3 = Book('Python编程', '埃里克', 129)

book1.show_info()
book3.show_info()

print(Book.get_total_books())

print(f'《Python编程》是否是高价书: {Book.is_expensive(book3.price)}')