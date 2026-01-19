a = 10
b = 5
c = 10

print(a == b)
print(a == c)
print(a != b)

print(a > b)
print(a < b)
print(a >= c)
print(b <= c)

print("===============")

print(0.1 + 0.2 == 0.3)
print(abs(0.1 + 0.2 - 0.3) < 1e-9)

print("================")
print('a' < 'b')
print('abc' < 'abd')

print("================")

print([1, 2] < [1, 3])
print((10, 2) > (5, 99))

if a == 10:
    print('a 等于 10')

# print(10 > '5')
print(10 > 5.0)

print("=================")
age = 18
if age >= 18:
    print("你已成年")
else:
    print("你未成年")

score = 60
if score >= 60:
    print("及格")
else:
    print("不及格")

num = 19
if num % 2 == 0:
    print(f'{num}是偶数')
else:
    print(f'{num}是奇数')