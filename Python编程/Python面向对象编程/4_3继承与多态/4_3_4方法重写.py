class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} 在吃东西（父类通用逻辑）')

    def sleep(self):
        print(f'{self.name} 在睡觉')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # def eat(self):
    #     print(f'{self.name}（狗）在啃骨头')
    #
    # def eat(self, food):
    #     print(f'{self.name} 吃 {food}')
    # def eat(self):
    #     super().eat()
    #     print(f'-> {self.name}（狗）专属: 啃骨头更香!')
    def eat(self):
        print(f'{self.breed}犬{self.name} 在啃骨头')


class Cat(Animal):
    def eat(self):
        print(f'{self.name}（猫）在吃鱼')


# dog = Dog('旺财', '金毛')
# dog.eat()
# cat = Cat('小白')

# dog.eat('骨头')
# dog.eat()
# cat.eat()

# dog.sleep()
# cat.sleep()

def feed_animal(animal):
    animal.eat()


dog = Dog('旺财', '金毛')
cat = Cat('小白')
bird = Animal('麻雀')


# feed_animal(dog)
# feed_animal(cat)
# feed_animal(bird)

class Bird(Animal):
    def eat(self):
        print(f'{self.name}（鸟）在吃虫子')


# feed_animal(Bird('小燕子'))

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