student = {
    'name': '小明',
    'age': 18,
    'gender': '男',
    'scores': [90, 85, 95]
}

empty_dict = {}
print(type(student))
print(type(empty_dict))

student = {
    'name': '小明',
    'age': 18
}
print(student['name'])
# print(student['height'])

print(student.get('name'))
print(student.get('height'))
print(student.get('height', 175))

print("======================")

student = {
    'name': '小明',
    'age': 18
}
student['age'] = 19
print(student)

student['height'] = 175
student['hobby'] = ['篮球', '看书']
print(student)

print("========================")

student = {
    'name': '小明',
    'age': 18,
    'height': 175
}
print(student)
del student['height']
print(student)

age = student.pop('age')
print(age)
print(student)

print("=======================")

student = {
    'name': '小明',
    'age': 18,
    'gender': '男'
}
print(student.keys())
print(student.values())

print(student)
print(student.items())
for key, value in student.items():
    print(f'{key}: {value}')

print(student)
student.clear()
print(student)

d = {'a': 1, 'a': 2}
print(d)

print("====================")
# d = {[1,2] : 'test'}
d = {(1,2): 'test'}
print(d)