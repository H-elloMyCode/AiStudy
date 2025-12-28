# print(1)
# print(2)
# print(3)

s = 'Python'
for char in s:
    print(char)

nums = [1, 2, 3, 4, 5]
total = 0
for num in nums:
    total += num
print(f'列表总和: {total}')

for i in range(5):
    print(f'第{i + 1}次循环')

for i in range(1, 10):
    print(i, end=' ')

print()

for i in range(2, 11, 2):
    print(i, end=' ')

print()

student = {'name': '小明', 'age': 18, 'score': 90}
for i in student.keys():
    print(i)

for key, value in student.items():
    print(f'{key}: {value}')

print("==========================")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("=====================")
lst = [1, 2, 3, 4]
for num in lst:
    if num == 2:
        lst.remove(num)
    print(num)

for num in lst.copy():
    if num == 2:
        lst.remove(num)

print(lst)