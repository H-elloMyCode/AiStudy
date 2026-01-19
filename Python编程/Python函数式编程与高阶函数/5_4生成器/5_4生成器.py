# lst = [x for x in range(1000000)]
# print(type(lst))
# print(lst[:100])

# gen = (x for x in range(1000000))
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# gen1 = (x for x in range(5))
#
# for num in gen1:
#     print(num)

# print(next(gen1))

# gen2 = (x for x in range(10) if x % 2 == 0)
# print(list(gen2))
# print(list(gen2))
#
# gen3 = (x for x in range(3))
# print(list(gen3))
# print(list(gen3))

def my_generator():
    print("开始执行")
    yield 1
    print("继续执行")
    yield 2
    print("最后执行")
    yield 3

# gen = my_generator()
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def infinite_even():
    num = 0
    while True:
        yield num
        num += 2

# even_gen = infinite_even()
#
# for _ in range(150):
#     print(next(even_gen))

def counter():
    count = 0
    while True:
        res = yield count
        if res is not None:
            count = res
        else:
            count += 1

# gen = counter()
# print(next(gen))
# print(next(gen))
# print(gen.send(10))
# print(next(gen))

def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# file_gen = read_large_file('test.txt')
# count = 0
# for line in file_gen:
#     print(line)
#     if count == 10:
#         break
#     count += 1

gen = (x for x in range(10))

filterd = filter(lambda x: x % 2 == 0, gen)

mapped = map(lambda x: x * 3, filterd)

for num in mapped:
    print(num)