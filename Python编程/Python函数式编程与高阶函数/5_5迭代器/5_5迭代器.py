from collections.abc import Iterator, Iterable

# lst = [1, 2, 3]
# print(isinstance(lst, Iterable))
# print(isinstance(lst, Iterator))
#
# lst_iter = iter(lst)
# print(isinstance(lst_iter, Iterator))

fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)

# print(next(fruit_iter))
# print(next(fruit_iter))
# print(next(fruit_iter))
# print(next(fruit_iter))

# nums = [1, 2, 3]
# for num in nums:
#     print(num)

lst_iter = iter([1, 2, 3])


# print(list(lst_iter))
# print(list(lst_iter))

class MyIterator(Iterator):
    def __init__(self):
        self.count = 1

    def __next__(self):
        if self.count <= 5:
            res = self.count
            self.count += 1
            return res
        else:
            raise StopIteration


# my_iter = MyIterator()
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# for num in my_iter:
#     print(num)

class BigNumberIterator(Iterator):
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __next__(self):
        if self.current <= self.max_num:
            res = self.current
            self.current += 1
            return res
        raise StopIteration


big_iter = BigNumberIterator(10000000)
# for _ in range(100):
#     print(next(big_iter))

nums = [1, 2, 3]

map_iter = map(lambda x: x * 2, nums)
print(isinstance(map_iter, Iterator))

# print(next(map_iter))
# print(next(map_iter))
# print(next(map_iter))
# print(next(map_iter))