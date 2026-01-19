age = 18
name = '小明'
is_student = True

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

x = 100
y = x
print(y)

count = 0
count += 1
print(count)

count += 5
print(count)

num = 10
num -= 3
print(num)

price = 20
price *= 1.8
print(price)

score = 95
score /= 2
print(score)

n = 10
n //= 3
print(n)

n %= 2
print(n)

n **= 3
print(n)

total = 0
for i in range(1, 6):
    total += i
print(total)

price = 99.9
discount = 0.8
price *= discount
print(f'折扣后价格: {price}')

input_count = 0
while input_count < 3:
    user_input = input("请输入内容: ")
    input_count += 1
print(f'共输入{input_count}次')

# 10 = a