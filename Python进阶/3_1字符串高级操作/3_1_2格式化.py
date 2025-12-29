num1 = 123
num2 = 3.1415926
num3 = 0.85

# print(f'学号补零到6位: {num1:006d}')
#
# print(f'圆周率保留2位: {num2:.2f}')
# print(f'圆周率保留4位: {num2:.4f}')
#
# print(f'通过率: {num3:.2%}')
#
# print(f'科学计数法: {num2:.2e}')
#
# print(f'带正号: {num1:+d}')
# print(f'负数带符号: {-num1:+d}')

name1 = '小明'
name2 = '张三四'
score1 = 95
score2 = 8.5

# print(f'{"姓名:":<8}{"成绩":>6}')
# print(f'{name1:<8}{score1:>6d}')
# print(f'{name2:<8}{score2:>6.1f}')

# print(f'{name1:-^10}')
# print(f'{score1:*^8}')

text = 'Python教程很实用'
# print(f'{text:.5}')

user = {'id': 8, 'name': '李五', 'salary': 12500.875, 'rate': 0.92}
info = f'''
用户ID: {user["id"]:04d}
用户姓名: {user["name"]:>10}
月薪资: {user["salary"]:>12.2f}
通过率: {user["rate"]:.1%}
'''
# print(info)

print('学号: {:06d}, 成绩: {:.2f}'.format(123, 89.567))
print('通过率: %.1f%% ' % (0.85 * 100))