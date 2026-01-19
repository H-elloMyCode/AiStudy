empty_list = []
nums = [1, 2, 3, 4, 5]
mix_list = [18, '小明', True, 3.14]

print(type(nums))

fruits = ['苹果', '香蕉', '橙子']
print(fruits[0])
print(fruits[-1])

nums = [10, 20, 30, 40, 50]
print(nums[1:3])
print(nums[:3])
print(nums[3:])

print("===================")

fruits = ['苹果', '香蕉', '橙子']
fruits[1] = '葡萄'
print(fruits)

print("===================")
fruits = ['苹果', '香蕉', '橙子']
fruits.append('梨')
print(fruits)

fruits.insert(1, '草莓')
print(fruits)

fruits.remove('香蕉')
print(fruits)

del fruits[0]
print(fruits)

last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

print("==================")

nums = [3, 1, 4, 2, 5]
nums.sort()
print(nums)

nums.reverse()
print(nums)

print(nums.count(3))

print(len(nums))

if 6 in nums:
    nums.remove(6)
print(nums)

print("==================")

l1 = [1, 2, 3]
l2 = l1
print(l2)
print(l2)
l1.remove(1)
print(l1)
print(l2)
