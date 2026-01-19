lst1 = []
for x in range(1, 6):
    lst1.append(x)
# print(lst1)

lst2 = [x for x in range(1, 6)]
# print(lst2)

lst3 = [x * x for x in range(1, 6)]
# print(lst3)

nums = [1, 2, 3]
str_nums = [str(x) for x in nums]
# print(str_nums)

even_lst1 = []
for x in range(1, 11):
    if x % 2 == 0:
        even_lst1.append(x)
# print(even_lst1)
even_lst2 = [x for x in range(1, 11) if x % 2 == 0]
# print(even_lst2)

nums = [-2, -1, 0, 1, 2, 3]
positive_nums = [x for x in nums if x > 0]
# print(positive_nums)

str_list = ['Python', '', '教程', ' ', '2025']
clean_list = [s.strip() for s in str_list if s.strip()]
# print(clean_list)

list1 = [1, 2, 3]
list2 = [10, 20]
result = [x + y for x in list1 for y in list2]
# print(result)

nums = [x for x in range(1, 21) if x % 2 == 0 and x % 3 ==0]
# print(nums)

gen = (x for x in range(100))
# print(type(gen))
# for e in gen:
#     print(e)

# lst = [x if x % 2 ==0 for x in range(10)]

input_str = input('请输入多个数字(用逗号分隔): ').strip()
nums_list = [int(x) for x in input_str.split(',') if x.strip().isdigit()]
even_list = [x for x in nums_list if x % 2 == 0]
print(even_list)