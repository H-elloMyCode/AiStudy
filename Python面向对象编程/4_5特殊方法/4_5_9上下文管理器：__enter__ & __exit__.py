# file = open('test.txt', 'w')
#
# try:
#     file.write('hello')
# finally:
#     file.close()

# with open()

# open()

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f' __enter__: 打开文件')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(' __exit__: 关闭文件')
        if self.file:
            self.file.close()
        return None

# with FileManager('test.txt', 'w') as f:
#     print('执行 with 代码块, 写入文件')
#     f.write('Hello, Context Manager!')
#
# print(f.closed)

# with FileManager('test.txt', 'w') as f:
#     print('执行代码块')
#     raise ValueError('测试异常')

# print(f.closed)

class DBConnection:
    def __init__(self, host):
        self.host = host
        self.conn = None

    def __enter__(self):
        print(f' __enter__: 连接数据库 {self.host}')
        self.conn = f'数据库连接对象 - {self.host}'
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f' __exit__: 断开数据库 {self.host} 连接')
        if exc_type:
            print(f'捕获异常: {exc_type.__name__} - {exc_val}')
            return False
        return False

# with DBConnection('127.0.0.1') as conn:
#     print('执行数据库操作...')
#     raise RuntimeError('数据库插入失败')
#
# print('程序继续执行...')

import time

class TimeoutDBConnection:
    def __init__(self, host, timeout=5):
        self.host = host
        self.timeout = timeout
        self.conn = None

    # def __enter__(self):
    #     print(f'尝试连接 {self.host}, 超时时间 {self.timeout} 秒')
    #     start = time.time()
    #     time.sleep(2)
    #     if time.time() - start > self.timeout:
    #         raise TimeoutError('数据库连接超时')
    #     self.conn = f'有效连接 - {self.host}'
    #     print(f'连接成功: {self.conn}')
    #     return self.conn

    def __enter__(self):
        print(f'尝试连接 {self.host}, 超时时间 {self.timeout} 秒')
        start = time.time()
        time.sleep(2)
        try:
            if time.time() - start > self.timeout:
                raise TimeoutError('数据库连接超时')
            self.conn = f'有效连接 - {self.host}'
            print(f'连接成功: {self.conn}')
        except TimeoutError as e:
            # 捕获异常，可记录日志等操作，不向外抛出，让__enter__正常结束
            self.conn = None  # 标记连接失败
            print(f"__enter__内捕获异常：{e}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """释放连接，处理异常（优化缩进冗余）"""
        print('执行 __exit__ ')
        # 1. 释放资源（缩进正确，逻辑无误）
        if self.conn:
            print(f'断开连接：{self.conn}')
            self.conn = None
        # 2. 处理特定异常（优化缩进，简化返回值）
        if exc_type == TimeoutError:
            print(f'连接失败：{exc_val}')
            return False  # 吞掉超时异常
        elif exc_type:  # 替代原elif，缩进更简洁，逻辑等价
            print(f'数据库操作异常：{exc_val}')
            return False  # 其他异常正常抛出
        # 正常无异常时，默认返回None，无需显式return

# print('==== 正常连接 ====')
# with TimeoutDBConnection('127.0.0.1') as conn:
#     print(f'执行查询: {conn}')
# #
print('==== 超时连接 ====')
with TimeoutDBConnection('127.0.0.1', timeout= 1) as conn:
    print(f'执行查询 :{conn}')
    raise TimeoutError('连接超时异常')

print(f'\n程序未中断, 继续执行 ...')