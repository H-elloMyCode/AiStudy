# with open('test_write_w.txt', 'w', encoding='utf-8') as f:
#     f.write('Python文件读取教程\n')
#     f.write('第一行内容\n')
#     f.write('第二行内容\n')
#     print('覆盖写入完成')

# with open('test_write_w.txt', 'a', encoding='utf-8') as f:
#     f.write('追加的第三行内容')
#     print('追加写入完成')

# lines = ['批量写入第一行\n', '批量写入第二行\n', '批量写入第三行\n']
#
# with open('batch_write.txt', 'w', encoding='utf-8') as f:
#     f.writelines(lines)
#     print("批量写入完成!")

# user_info = {'name': '小明', 'age': 18, 'score': 95.5}
#
# with open('user_info.txt', 'w', encoding='utf-8') as f:
#     f.write(f'姓名: {user_info["name"]}\n')
#     f.write(f'年龄: {user_info["age"]}\n')
#     f.write(f'成绩: {user_info["score"]}\n')
#
#     print("格式化写入完成")

# def copy_image(src_path, dst_path):
#     # 读取原图片
#     with open(src_path, 'rb') as f_read:
#         binary_data = f_read.read()
#         with open(dst_path, 'wb') as f_write:
#             f_write.write(binary_data)
#
#     print(f'图片复制完成: {src_path} -> {dst_path}')
#
# copy_image('1.png', '1_copy.png')

import datetime


def write_log(log_path, content):
    """
    追加写入日志（包含时间戳）
    :param log_path:
    :param content:
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H时%M分%S秒')
    log_line = f'[{timestamp}] {content}\n'

    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_line)
        print(f'日志已写入: {log_line.strip()}')


write_log('operation.log', '用户小明登录系统')
write_log('operation.log', '用户小明查询了成绩')
write_log('operation.log', '用户小明退出系统')
