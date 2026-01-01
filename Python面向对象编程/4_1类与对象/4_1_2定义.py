class EmptyClass:
    pass

class Phone:
    """
    手机类：描述手机的属性和行为
    """
    brand = '未知品牌'
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def show_info(self):
        print(f'品牌: {self.brand}, 型号: {self.model}, 价格： {self.price}')

    def call(self, number):
        print(f'{self.model} 正在拨打 {number} ...')

phone1 = Phone('Mate 60 Pro', 6999)
phone2 = Phone('iPhone 15', 7999)

# print(phone1.model)
# print(phone1.price)
#
# print(Phone.brand)
# print(phone1.brand)

Phone.brand = '华为'
# print(phone1.brand)
# print(phone2.brand)

phone2.brand = '苹果'
# print(phone2.brand)
# print(phone1.brand)

# phone1.show_info()
# phone2.show_info()

# phone1.call('10086')

class TestSelf:
    def __init__(self, name):
        self.name = name

    def print_self(self):
        print(f'self的地址: {id(self)}, 对象名称: {self.name}')

obj1 = TestSelf('对象1')
obj2 = TestSelf('对象2')

# print(f'obj1 的地址: {id(obj1)}')
# obj1.print_self()
#
# print(f'obj2 的地址: {id(obj2)}')
# obj2.print_self()

class PhoneWithDefault:
    def __init__(self, model='默认型号', price=0):
        self.model = model
        self.price = price

phone3 = PhoneWithDefault()
# print(phone3.model)
# print(phone3.price)

class TestPrivate:
    def __init__(self):
        self.__private_attr = '私有属性'

obj = TestPrivate()
# print(obj.private_attr)

class Book:
    """
    图书类: 所有图书的默认分类
    """
    category = '未分类'
    def __init__(self, title, author, price = 0):
        self.title = title
        self.author = author
        self.price = price

    def show_book_info(self):
        info = f'书名: {self.title}, 作者: {self.author}, 价格: {self.price}, 分类: {self.category}'
        print(info)
        return info

    def get_discount_price(self, discount):
        if 0 < discount <= 1:
            return self.price * discount
        else:
            print('折扣率必须在 0-1 之间!')
        return self.price

book1 = Book('Python编程：从入门到实践', '埃里克·马瑟斯', 89)
book2 = Book('红楼梦', '曹雪芹', 59)

Book.category = '文学&编程'

book1.show_book_info()
print(f'book1 8 折价格: {book1.get_discount_price(0.8)} 元')

book2.show_book_info()
print(f'book2 9 折价格: {book2.get_discount_price(0.9)} 元')