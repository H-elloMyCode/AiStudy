class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        raise NotImplementedError('子类必须重写 eat 方法')


class Dog(Animal):
    def eat(self):
        print(f'{self.name}（狗）吃骨头')


class Cat(Animal):
    def eat(self):
        print(f'{self.name}（猫）吃鱼')


class Bird(Animal):
    def eat(self):
        print(f'{self.name}（鸟）吃虫子')


def feed_animal(animal):
    animal.eat()


# feed_animal(Dog('旺财'))
# feed_animal(Cat('十一'))
# feed_animal(Bird('麻雀'))

animal1: Animal = Dog('旺财')
animal2: Animal = Cat('小白')


# animal1.eat()
# animal2.eat()

class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        raise NotImplementedError('子类必须重写 calculate_area 方法')


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


def print_area(shape):
    area = shape.calculate_area()
    print(f'{shape.name} 的面积是: {area}')


circle = Circle('圆形', 5)
rectangle = Rectangle('矩形', 4, 6)

print_area(circle)
print_area(rectangle)

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

print_area(Triangle('三角形', 6, 8))
