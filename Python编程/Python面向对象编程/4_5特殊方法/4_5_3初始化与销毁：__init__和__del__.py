# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#         print(f' __init__ 被调用: {self.name} 对象已初始化')
#         # return None

# p1 = Person('小明', 25)
# p2 = Person('小红')

# print(p1.name)
# print(p2.age)

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
# stu = Student('小丽', 20, '2026001')
# print(stu.name, stu.student_id)

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        print(f' __init__: 打开文件 {filename}')

    def __del__(self):
        self.file.close()
        print(f' __del__: 关闭文件 {self.filename}，对象已销毁')

# fh = FileHandler('test.txt')
# del fh

class Person:
    def __del__(self):
        print(' __del__ 被调用: 对象销毁')

# p = Person()
# # del p
#
# p1 = Person()
# p2 = p1


# p1 = Person()
# p2 = p1
#
# del p1
# del p2
#
# while True:
#     pass

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print(f'✅ 连接数据库 {host}:{port} 成功')

    def query(self, sql):
        print(f'执行 SQL: {sql}')

    def __del__(self):
        print(f'❌ 断开数据库 {self.host}:{self.port} 连接')

conn = DatabaseConnection('127.0.0.1', 3306)

conn.query('SELECT * FROM person')

del conn

# while True:
#     pass