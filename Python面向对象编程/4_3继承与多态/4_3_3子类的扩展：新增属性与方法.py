class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} 在吃东西')

    def sleep(self):
        print(f'{self.name} 在睡觉')
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f'{self.breed}犬{self.name}（{self.age}岁）汪汪叫!')

    def play(self):
        super().eat()
        print(f'{self.breed}犬{self.name} 吃完东西后, 开心玩球! ')

class Cat(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def catch_mouse(self):
        print(f'{self.fur_color} 的 {self.name}（{self.age}岁）在抓老鼠!')

# dog = Dog('旺财', 3)
dog = Dog('旺财', 3, '金毛')
# print(f'姓名: {dog.name}，年龄: {dog.age}，品种: {dog.breed}')
# dog.eat()
# dog.sleep()
# dog.bark()
# dog.play()

cat = Cat('小白', 2, '纯白色')
# cat.eat()
# cat.sleep()
# cat.catch_mouse()

class ElectronicProduct:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def power_on(self):
        print(f'{self.brand} 产品开机中 ... ')

class Phone(ElectronicProduct):
    def __init__(self, brand, price, screen_size, ram):
        super().__init__(brand, price)
        self.screen_size = screen_size
        self.ram = ram

    def make_call(self, number):
        print(f'{self.brand} 手机（{self.screen_size}英寸/{self.ram}G）拨打{number}...')

    def show_config(self):
        print(f'品牌: {self.brand}，价格: {self.price} 元, 屏幕: {self.screen_size} 英寸，内存: {self.ram} G')

phone = Phone('小米', 2999, 6.7, 12)
print(phone.price)
print(phone.screen_size)

phone.power_on()
phone.make_call('10086')
phone.show_config()