count = 0
while count < 5:
    print(f'第{count + 1}次循环')
    count += 1

# correct_pwd = '123456'
# user_pwd = ''
# while user_pwd != correct_pwd:
#     user_pwd = input("请输入密码： ")
#     if user_pwd != correct_pwd:
#         print("密码错误，请重试")
#
# print("登录成功")

print("=======================")
count = 0
while True:
    count += 1
    print(count)
    if count == 5:
        break

print("=======================")

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

num = 17
i = 2
while i < num:
    if num % i == 0:
        print(f'{num}不是质数')
        break
    i += 1
else:
    print(f'{num}是质数')