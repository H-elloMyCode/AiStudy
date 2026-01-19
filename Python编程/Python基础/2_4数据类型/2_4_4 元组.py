fruits = ('苹果', '香蕉', '橙子')

empty_tuple = ()

single_tuple = (18,)
wrong_tuple = (18)

print(type(fruits))
print(type(empty_tuple))
print(type(single_tuple))
print(type(wrong_tuple))

print("=========================")

nums = (10, 20, 30, 40, 50)
print(nums[0])
print(nums[-1])

print(nums[1:3])
print(nums[:3])

print("==========================")

fruits = ('苹果', '香蕉', '橙子')
# fruits[1] = '葡萄'
# del fruits[0]

a = (1, 2, 3)
b = (4, 5, 6)
print(a)
print(b)

print(a + b)
print(a * 2)
print(len(a))

print(a.count(2))

print(a.index(3))

info = ('小明', 18, '男')
name, age, gender = info
print(name)
print(age)
print(gender)

tuple_list = (1, 2, 3, [4, 5, 6])
print(tuple_list)
tuple_list[3][0] = 999
print(tuple_list)