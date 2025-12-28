from queue import PriorityQueue

age = 18
if age >= 18:
    print("你已成年，可以进入")
print("程序结束")

score = 58
if score >= 60:
    print("成绩及格，继续加油")
else:
    print("成绩不及格，补考")

score = 100
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
# else:
#     print("不及格")

print("=========================")
age = 20
has_license = True
if age >= 18:
    print("你已成年")
    if has_license:
        print("你有驾照，可以开车")
    else:
        print("你没有驾照，要先考取")
else:
    print("未成年，不能考驾照，不能开车")

print("===============================")
# if age >= 18:
# print("成年")

num = int(input("请输入一个整数: "))
if num % 2 == 0:
    print(f'{num}是偶数')
else:
    print(f'{num}是奇数')

correct_pwd = '123456'
user_pwd = input("请输入密码：")
if user_pwd == correct_pwd:
    print("登陆成功")
else:
    print("密码错误")