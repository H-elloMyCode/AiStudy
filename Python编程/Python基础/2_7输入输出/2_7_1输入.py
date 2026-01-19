# a = input()

# name = input("请输入你的姓名: ")
# print(f'你好，{name}')

# info = input("请输入任意内容: ")
# print(f'你输入的是: {info}, 类型是: {type(info)}')

# age_input = input("请输入你的年龄: ")
# age = int(age_input)
# print(f'明年的你的年龄是: {age + 1}')

# height_input = input("请输入你的身高(米): ")
# height = float(height_input)
# print(f'身高厘米数: {height * 100}')

# score = int(input("请输入你的成绩: "))
# print(f'成绩加 5 分: {score + 5}')

# info = input("请输入你的姓名和年龄(用空格分隔): ").split()
# name, age = info
# age = int(age)
# print(f'姓名: {name}, 年龄{age}')

# nums = input("请输入3个数字(用逗号分隔): ").split(',')
# num1 = int(nums[0])
# num2 = int(nums[1])
# num3 = int(nums[2])
# print(f'数字总和: {num1 + num2 + num3}')

while True:
    age_input = input("请输入你的年龄(数字): ")
    if age_input.isdigit():
        age = int(age_input)
        print(f'你的年龄是: {age}')
        break
    else:
        print("输入错误!请输入数字")
