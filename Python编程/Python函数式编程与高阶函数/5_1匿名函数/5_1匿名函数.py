# def add(x, y):
#     return x + y


# lambda x, y: x + y

square = lambda x: x ** 2

# print(square(5))
# print(square(3))

add = lambda x, y: x + y
# print(add(10, 20))

multiply = lambda x, y=20: x * y
# print(multiply(5))
# print(multiply(5, 3))

# test = lambda x: x += 1; return x
# test = lambda x: for i in range(x): print(i)

max_num = lambda x, y: x if x > y else y
# print(max_num(8, 5))

# numbers = [1, 2, 3]
# result = list(map(lambda x: x * 3, numbers))
# print(result)

# numbers = [2, 7, 4, 9, 1]
# result = list(filter(lambda x: x > 5, numbers))
# print(result)

from functools import reduce

# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x * y, numbers)
# print(result)

students = [('小明', 85), ('小红', 92), ('小刚', 78)]
print(students)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)