# path = "D:\\Projects\\AiStudy\\Python进阶\\3_5文件操作\\3_5_3路径处理.py"

from pathlib import Path

p1 = Path('test_pathlib.txt')
p2 = Path('data/logs')

p3 = Path('D:/Projects/AiStudy/Python进阶/3_5文件操作/test_pathlib.txt')

p4 = Path('data') / 'logs' / 'app.log'
# with open(p4, 'r', encoding='utf-8') as f:
#     print(f.read())

# with open(p3, 'r', encoding='utf-8') as f:
#     print(f.read())

# print(p4)

p = Path('D:/Projects/AiStudy/Python进阶/3_5文件操作/data/logs/app.log')

# print(p.resolve())
#
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.parent)
# print(p.parents[0])
# print(p.parents[1])
#
# print(p.drive)

p = Path('data/logs/app.log')

# print(p.exists())
# print(p.is_file())
# print(p.is_dir())

# dir_path = Path('data/logs/2025')
# dir_path.mkdir(parents=True, exist_ok=True)

# print(Path.cwd())
# print(Path.home())

path = Path('test.txt')
# path.write_text('Python路径处理教程\nHello Pathlib!', encoding='utf-8')

content = path.read_text(encoding='utf-8')
# print(content)

dir_path = Path('data/logs')

# for log_file in dir_path.glob('*.log'):
#     print(f'日志文件: {log_file}')

# for log_file in dir_path.rglob('*.log'):
#     print(f'日志文件: {log_file}')

import os

path = os.path.join('data', 'logs', 'app.log')
# print(path)
#
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.splitext(path))

# print(os.path.exists(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))

# print(os.getcwd())

current_dir = Path(__file__).parent
file_path = current_dir / '3_5_3路径处理.py'
# print(file_path)

from pathlib import Path
import datetime


def rename_log_files(dir_path):
    """
    重命名日志文件
    :param dir_path:
    :return:
    """
    dir_path = Path(dir_path)
    date_str = datetime.datetime.now().strftime('%Y%m%d')

    for log_file in dir_path.glob('*.log'):
        new_name = f'{log_file.stem}_{date_str}{log_file.suffix}'
        new_path = log_file.parent / new_name

        log_file.rename(new_path)
        print(f'重命名完成: {log_file} -> {new_path}')

rename_log_files('data/logs/2026')