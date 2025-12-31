# with open('test.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print('文件全部内容: ')
#     print(content)
#     print(f'内容长度: {len(content)}')
#
# with open('test.txt', 'r', encoding='utf-8') as f:
#     print("逐行读取: ")
#     line = f.readline()
#     while line:
#         print(line.strip())
#         line = f.readline()

# with open('test.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     print('所有行列表: ', lines)
#     print("遍历处理: ")
#     for index, line in enumerate(lines):
#         print(f'第{index + 1}行: {line.strip()}')

# with open('test.txt', 'r', encoding='utf-8') as f:
#     print("直接遍历文件对象: ")
#     for index, line in enumerate(f):
#         print(f'第{index + 1}行: {line.strip()}')

# with open('test.txt', 'r') as f:
#     print("直接遍历文件对象: ")
#     for index, line in enumerate(f):
#         print(f'第{index + 1}行: {line.strip()}')

# with open('D:\\Projects\\AiStudy\\Python进阶\\3_5文件操作\\test.txt', 'r', encoding='utf-8') as f:
#     print("直接遍历文件对象: ")
#     for index, line in enumerate(f):
#         print(f'第{index + 1}行: {line.strip()}')

# with open('1.png', 'rb') as f:
#     binary_data = f.read()
# print(binary_data)

def filter_error_log(log_path, output_path):
    """
    筛选日志文件中的错误行
    :param log_path:
    :param output_path:
    :return: 筛选后的文件路径
    """
    error_lines = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '错误' in line or 'ERROR' in line:
                error_lines.append(line)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.writelines(error_lines)

    print(f'筛选完成！共找到{len(error_lines)}行错误日志，已保存到{output_path}')

filter_error_log('log.txt', 'error_log.txt')