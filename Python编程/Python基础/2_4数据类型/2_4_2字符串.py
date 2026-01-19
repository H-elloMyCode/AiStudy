name = '小明'
print(type(name))

info = "小明说了一句话"
print(type(info))

content = '''
第一行
第二行
第三行
'''
print(type(content))

first = 'Hello'
second = 'Python'
print(first + second)
# print(first + 2)
print(first + str(2))

print("==========================")

s = 'Python'
print(s[0])
print(s[3])
print(s[-1])

print("==========================")

ss = 'Python教程'
print(ss[0:6])
print(ss[:6])
print(ss[6:])

print("==========================")

sss = '    Hello Python   '
print(sss)

print(sss.strip())
print(sss.lower())
print(sss.upper())

print(sss.replace('Python', 'Java'))

print(sss.count('o'))

sss = sss.strip()
print(sss.startswith('Hello'))
print(sss.endswith('Python'))

print("====================")

name = '小红'
score = 98.54
print(f'{name} 的数学成绩是 {score} 分')
print(f'成绩保留 1 位小数: {score:.1f}')

# name[0] = '大'
# print(name[0])

print("==========================")
# content = '我的家在东北，\'松花江\'上'
content = '我的家在东北，"松花江"上'
print(content)

ssss = '012345'
print(ssss[5])