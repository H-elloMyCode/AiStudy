# try:
#     num_input = input("请输入一个数字: ")
#     num = int(num_input)
#     result = 10 / num
#
#     print(f'10 / {num} = {result}')
# except ZeroDivisionError:
#     print("错误：不能除以0!")
# except ValueError:
#     print("错误：请输入有效的数字!")

# try:
#     num_input = input("请输入一个数字: ")
#     num = int(num_input)
#     result = 10 / num
#
#     # print(10 + '20')
#
#     print(f'10 / {num} = {result}')
# except ZeroDivisionError:
#     print("错误：不能除以0!")
# except ValueError:
#     print("错误：请输入有效的数字!")
# except:
#     print("错误：发生了未知错误，请重试!")

# try:
#     num_input = input("请输入一个数字: ")
#     num = int(num_input)
#     result = 10 / num
# except ZeroDivisionError:
#     print("错误：不能除以0!")
# except ValueError:
#     print("错误：请输入有效的数字!")
# else:
#     print(f'10 / {num} = {result}')
# finally:
#     print("=====操作结束=====")

# try:
#     lst = [1, 2, 3]
#     print(lst[10])
# except IndexError as e:
#     print(f'异常类型: {type(e).__name__}')
#     print(f'异常描述: {e}')

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

    except FileNotFoundError:
        print(f'错误：文件[{file_path}] 不存在!')
        return None
    except PermissionError:
        print(f'错误：没有权限读取文件[{file_path}]!')
        return None
    else:
        print(f'成功读取文件[{file_path}], 内容长度: {len(content)}')
        return content
    finally:
        print(f'文件读取操作完成（路径{file_path}）')
        # f.close()

content = read_file('text.txt')
if content:
    print('文件内容: ', content[:100])