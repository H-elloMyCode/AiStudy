dict1 = {}
for x in range(1, 6):
    dict1[x] = x * x
# print(dict1)

dict2 = {x: x * x for x in range(1, 6)}
# print(dict2)

keys = ['name', 'age', 'gender']
values = ['小明', 18, '男']
user_dict = {k: v for k, v in zip(keys, values)}
# print(user_dict)

s = 'Python'
char_index = {char: index for index, char in enumerate(s)}
# print(char_index)

origin_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
filtet_dict = {k: v for k, v in origin_dict.items() if v > 10}
# print(filtet_dict)

raw_data = {'name': '小红', 'age': '', 'gender': '女', 'score': None}
clean_data = {k: v for k, v in raw_data.items() if v}
# print(clean_data)

score_dict = {'语文': 80, '数学': 90, '英语': 85}
new_score = {k: v + 10 for k, v in score_dict.items()}
# print(new_score)

dict_a = {'a': 10, 'b': 20}
dict_b = {'a': 5, 'c': 15}
merge_dict = {k: dict_a.get(k, 0) + dict_b.get(k, 0) for k in dict_a.keys() | dict_b.keys()}
# print(merge_dict)

score_dict = {'语文': 80, '数学': 90, '数英': 85, '英语': 75}
filter_score = {k: v for k, v in score_dict.items() if v > 80 and '数' in k}
# print(filter_score)

repeat_dict = {x % 3: x for x in range(1, 6)}
# print(repeat_dict)

# wrong_dict = {[1, 2]: 'test' for x in range(1)}
right_dict = {(1, 2): 'test' for x in range(1)}
# print(right_dict)

input_str = input("请输入键值对(用逗号分隔, 格式key=value): ").strip()
user_input_dict = {}

if input_str:
    user_input_dict = {
        k.strip(): v.strip()
        for item in input_str.split(',')
        if '=' in item
        for k, v in [item.split('=')]
    }

print(user_input_dict)
