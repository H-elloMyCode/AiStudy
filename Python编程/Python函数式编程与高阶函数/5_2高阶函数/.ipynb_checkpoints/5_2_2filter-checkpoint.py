def is_even(x):
    return x % 2 == 0


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# result_filter = filter(is_even, numbers)
# print(result_filter)
# print(type(result_filter))
# print(list(result_filter))

# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)

mixed_data = [0, 1, "", "hello", [], [1, 2], None, 3.14]
# result = list(filter(None, mixed_data))

# print(result)

words = ["a", "ab", "abc", "abcd", "abcde"]

# result = list(filter(lambda s: len(s) > 3, words))
# print(result)

numbers = [1, 2, 3, 4]

# print(list(map(lambda x: x % 2 == 0, numbers)))
# print(list(filter(lambda x: x % 2 == 0, numbers)))

result1 = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))
result2 = [x for x in [1, 2, 3, 4, 5] if x > 3]

print(result1)
print(result2)