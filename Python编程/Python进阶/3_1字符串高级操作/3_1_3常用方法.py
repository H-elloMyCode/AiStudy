username = '  ZhangSan  '
clean_name = username.strip().lower()
# print(clean_name)

# phone = input("请输入手机号: ").strip()
# if phone.isdigit() and len(phone) == 11:
#     print("手机号格式合法")
# else:
#     print("手机号格式有误")


s = ' Python教程-2026-01 '
s_clean = s.strip()
# print(s_clean.replace('-', '/'))
# print(s_clean.replace('-', '/', 1))

# print(s_clean.split('-'))
# print(s_clean.split('-', 1))
multi_text = '第一行\n第二行\n第三行'
# print(multi_text)
# print(multi_text.splitlines())

lst = ['Python教程', '2026', '01']
# print('-'.join(lst))
words = ['Hello', 'Python']
# print(''.join(words))

# text = 'Python教程很实用，Python很强大'
# if text.find('Python') != -1:
#     print(f'关键词出现次数: {text.count("Python")}')

s = '   abc  '
s.strip()
# print(s)
s_clean = s.strip()
# print(s_clean)

sss = 'a b\nc'.split()
# print(sss)

mylist = [1, 2, 3]
# print('-'.join(mylist))

address = '  广东省-深圳市-南山区  '
clean_addr = address.strip().upper()
addr_list = clean_addr.split('-')
show_addr = ' '.join(addr_list)

# print(show_addr)
if len(addr_list) == 3:
    print(f'解析后的地址：{show_addr}')  # 输出：解析后的地址：广东省 深圳市 南山区
else:
    print('地址格式错误（需按"省-市-区"输入）')