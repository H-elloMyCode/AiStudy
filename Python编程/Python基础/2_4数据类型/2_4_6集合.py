nums = {1, 2, 2, 3, 3, 3}
print(nums)

empty_set = set()
wrong_empty_set = {}

list1 = [1, 2, 2, 3]
s = set(list1)
print(s)

print(type(nums))
print(type(empty_set))
print(type(wrong_empty_set))
print(type(s))

print("===========================")

fruits = {'苹果', '香蕉', '橙子'}
print('香蕉' in fruits)
print('葡萄' in fruits)

print("============================")
fruits = {'苹果', '香蕉', '橙子'}
fruits.add('葡萄')
print(fruits)

fruits.update(['梨', '芒果'])
print(fruits)

fruits.remove('香蕉')
print(fruits)

# fruits.remove('菠萝')
fruits.discard('西瓜')
print(fruits)

fruit = fruits.pop()
print(fruit)

fruits.clear()
print(fruits)

print("=======================")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a - b)
print(a.difference(b))
print(b - a)
print(b.difference(a))

print("=====================")

aa = {1, 2, 3}
# print(a[0])

# bb = {[1,2], 3}
bb = {(1,2), 3}
print(bb)