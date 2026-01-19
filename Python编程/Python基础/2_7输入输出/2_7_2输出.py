print("Hello world")

print(3.1415926)

name = '小明'
age = 18
print(name)
print(name, age)

print(10 + 5)
print("10 + 5 =", 10 + 5)

print("=======================")
print("姓名", "年龄", "性别", sep=',')

print("第一行内容", end=';')
print("第二行内容")

for i in range(1, 6):
    print(i, end=' ')

print("=======================")
name = '小红'
score = 98.58
print(f'{name}的数学成绩是{score}分')
print(f'{name}的数学成绩是{score + 5}分')

print(f'成绩保留至1位小数: {score:.1f}')
print(f'学号补零到6位: {123:06d}')
print(f'百分比格式: {0.85:.2%}')

print("========================")
name = '小明'
age = 19
print('%s今年%d岁' % (name, age))

name = '小刚'
score = 88
print('{}语文成绩是{}分'.format(name, score))

# with open('test.txt', 'w', encoding='utf-8') as f:
#     print('Hello python', file=f)
#     print('姓名：小明，年龄：18', file=f)

print(f'他说: "{name}考得很好"')