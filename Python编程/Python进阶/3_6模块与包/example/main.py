from log_utils import write_log

write_log('程序启动')

try:
    result = 10 / 0
except ZeroDivisionError:
    write_log('除以0错误', level='ERROR')

write_log('程序结束')