"""
    日志工具模块：提供格式化的日志输出功能
"""
import datetime

def write_log(content, level='INFO'):
    """
    输出格式化日志
    :param content:
    :param level:
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
    log_line = f'[{timestamp} [{level}] {content}]'
    print(log_line)

if __name__ == '__main__':
    write_log('测试信息日志')
    write_log('测试警告日志', level='WARN')
    write_log('测试错误日志', level='ERROR')