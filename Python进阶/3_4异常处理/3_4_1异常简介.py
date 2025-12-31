# a = 10 / 0

a = 10
b = 0
# print(a / 0)

# print(undefined_var)

# print(10 + '20')

# num = int('abc')
s = 'Python'
# print(s[10])

# print("前置")

user = {'name': '小明'}
# print(user['age'])

# print("后续代码")

# num_input = input("请输入一个数字: ")
# num = int(num_input)

# print(f'10 / {num} = {10 / num}')

num_input = input("请输入一个非零数字: ")
if num_input.strip().isdigit():
    num = int(num_input)
    if num != 0:
        print(f'10 / {num} = {10 / num}')
    else:
        print("错误！不能输入0!")
else:
    print("错误! 请输入数字")