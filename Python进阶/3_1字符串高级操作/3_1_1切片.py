s = 'Python教程123'

# print(s[-11])
# print(s[0:6])
# print(s[:6])
# print(s[6:])
#
# print(s[-3:])
# print(s[:-3])
#
# print(s[0:10:2])
# print(s[::3])

# print(s[::-1])
# print(s[8:2:-1])

phone = '13812345678'
# print(phone[-4:])

s = '2026Python教程2026'


# print(s[4:-4])

def is_palindrome(text):
    return text == text[::-1]


# print(is_palindrome('abcba'))
# print(is_palindrome('python'))

s = 'abcdefgh'
result = [
    s[i:i + 2]
    for i in range(0, len(s), 2)
]

# print(result)

str = 'abcdefg'
# print(s[3:1:-1])

s = 'Python'
new_s = s[:3]
print(s)
print(new_s)