# numbers = [1, 2, 3, 4, 5]

# def multiply_by_two(x):
#     return x * 2

# result_map = map(multiply_by_two, numbers)
# print(result_map)
# print(type(result_map))

# result_list = list(result_map)
# result_list = list(map(lambda x: x * 2, numbers))
# print(result_list)

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
#
# result = list(map(lambda x, y: x + y, list1, list2))
# print(result)

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30]
#
# result = list(map(lambda x, y: x + y, list1, list2))
# print(result)

str_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
int_numbers = list(map(int, str_numbers))

# print(int_numbers)

words = ["apple", "banana", "cherry"]
upper_words = list(map(str.upper, words))
# print(upper_words)

result1 = list(map(lambda x: x * 2, [1, 2, 3]))
print(result1)

result2 = [x * 2 for x in [1, 2, 3] if x > 1]
print(result2)
