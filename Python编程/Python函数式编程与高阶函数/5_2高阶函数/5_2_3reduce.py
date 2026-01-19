from functools import reduce

# def add(x, y):
#     return x + y


# numbers = [1, 2, 3, 4, 5]

# print(reduce(add, numbers))
# print(reduce(lambda x, y: x + y, numbers))
# print(reduce(lambda x, y: x + y, numbers, 10))

# numbers = [1, 2, 3, 4]
# print(reduce(lambda x, y: x * y, numbers))

# numbers = [5, 2, 9, 1, 7]
# max_num = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_num)

numbers = [1, 2, 3, 4]

# print(list(map(lambda x: x * 2, numbers)))
# print(list(filter(lambda x: x > 2, numbers)))
# print(reduce(lambda x, y: x + y, numbers))

print(reduce(lambda x, y: x + y, [], 0))