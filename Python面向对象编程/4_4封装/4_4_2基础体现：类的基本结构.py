# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'姓名: {self.name}，年龄: {self.age}')
#
#     def grow_up(self):
#         self.age += 1
#         print(f'{self.name} 长大了 1 岁，现在 {self.age} 岁')
#
# p1 = Person('小明', 18)
# p2 = Person('小红', 17)
#
# p1.show_info()
# p1.grow_up()
#
# p2.show_info()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and 0 < new_age < 150:
#             self.__age = new_age
#             print(f'年龄修改成功，当前年龄: {self.__age}')
#         else:
#             print(f'年龄 {new_age} 不合法，修改失败！')
#
#     def show_info(self):
#         print(f'姓名: {self.__name}，年龄: {self.__age}')
#
# p = Person('小明', 18)
#
# print(p.get_name())
# print(p.get_age())
#
# p.set_age(19)
# print(p.get_age())
#
# p.show_info()

# print(p._Person__name)

class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, (int, float)) and new_price > 0:
            self.__price = new_price
            print(f'《{self.__title}》价格修改为 {new_price} 元')
        else:
            print(f'价格 {new_price} 不合法，修改失败！')

    def show_book_info(self):
        print(f'书名: 《{self.__title}》')
        print(f'作者: {self.__author}')
        print(f'价格: {self.__price} 元')

book = Book('Python入门', '张三', 59.9)
book.show_book_info()
print(book.title)
book.price = 49.9
book.price = -10