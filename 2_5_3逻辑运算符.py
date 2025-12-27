print(True and True)
print(True and False)
print(10 > 5 and 8 > 3)
print(10 > 5 and 8 < 3)

print(True or False)
print(False or False)
print(10 > 5 or 8 < 3)
print(10 < 5 or 8 < 3)

print("========== not =======")
print(not True)
print(not False)
print(not (10 > 5))

print("===========实用场景===========")
age = 19
score = 65
if age >= 18 and score >= 60:
    print("成绩且成绩及格")

total = 90
is_vip = False
if total >= 100 or is_vip:
    print("可享受优惠")

if not (total >= 100 or is_vip):
    print("无法享受优惠")
else:
    print("可享受优惠")

print("========== 短路示例 ===========")
# print(False and (10 / 0))
# print(True or (10 / 0))
# print((10 / 0) and False)

print(True and False or True)
print(True and (False or True))

# print(True and '')
print(10 and 20)
print(0 or 20)