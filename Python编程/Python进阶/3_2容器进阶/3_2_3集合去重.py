# lst = [1, 2, 3, 5, 3, 3, 4, 5, 2]

# unique_lst = list(set(lst))
# print(unique_lst)

# lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
#
# unique_lst = list(dict.fromkeys(lst))
# print(unique_lst)

lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
seen = set()
unique_lst = []

for item in lst:
    if item not in seen:
        seen.add(item)
        unique_lst.append(item)
# print(unique_lst)

dict_lst = [
    {'name': '小明', 'age': 18},
    {'name': '小红', 'age': 19},
    {'name': '小明', 'age': 20}
]

seen = set()
unique_dict_lst = []

for dict in dict_lst:
    key = dict["name"]
    if key not in seen:
        seen.add(key)
        unique_dict_lst.append(dict)

# print(unique_dict_lst)
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
lst3 = [5, 6, 7]

unique_all = list(set(lst1 + lst2 + lst3))
# print(unique_all)

# s = {[1, 2], 3}
lst = [0, '', 1, 2, 2, False, 3]
unique_lst = [x for x in list(set(lst)) if x]
# print(unique_lst)

input_tags = input('请输入标签（用逗号分隔）：').strip()
raw_tags = [tag.strip() for tag in input_tags.split(',') if tag.strip()]

unique_tags = list(dict.fromkeys(raw_tags))
print(unique_tags)