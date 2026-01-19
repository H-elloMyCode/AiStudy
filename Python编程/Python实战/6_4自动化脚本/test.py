# import os
# import shutil
# from datetime import datetime
#
#
# def auto_backup():
#     source_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\办公自动化截图"  # 绝对路径
#     backup_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\自动备份"  # 绝对路径
#     backup_name = f"备份_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
#     target_dir = os.path.join(backup_dir, backup_name)
#
#     if not os.path.exists(backup_dir):
#         os.makedirs(backup_dir)
#
#     if os.path.exists(source_dir):
#         shutil.copytree(source_dir, target_dir)
#
#     with open("D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\自动备份\\备份日志.txt", "a", encoding="utf-8") as f:
#         f.write(f"备份成功：{datetime.now()} → {target_dir}\n")
#
#
# if __name__ == "__main__":
#     auto_backup()

import schedule
import time
import os
import shutil
from datetime import datetime


def log_record(content):
    """日志记录函数"""
    log_file = "定时备份日志.txt"
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"[{log_time}] {content}\n"

    # 打印日志并写入文件
    print(log_content.strip())
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_content)


def auto_folder_backup():
    """自动备份文件夹任务"""
    # 配置参数（使用绝对路径）
    source_folder = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\办公自动化截图"
    backup_root = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\办公数据自动备份"
    try:
        # 校验源文件夹是否存在
        if not os.path.isdir(source_folder):
            log_record(f"备份失败：源文件夹「{source_folder}」不存在")
            return

        # 创建备份根目录
        os.makedirs(backup_root, exist_ok=True)
        # 定义备份文件夹名称（带时间戳）
        backup_folder_name = f"数据备份_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        target_backup_folder = os.path.join(backup_root, backup_folder_name)

        # 执行备份
        shutil.copytree(source_folder, target_backup_folder)
        log_record(f"备份成功：{source_folder} → {target_backup_folder}")
    except Exception as e:
        log_record(f"备份异常：{str(e)}")


def main_schedule():
    """主定时调度配置"""
    # 1. 每天早8点备份（日常备份）
    schedule.every().day.at("08:00").do(auto_folder_backup)

    # 2. 每周五晚6点备份（周度归档）
    schedule.every().friday.at("18:00").do(auto_folder_backup)

    # 3. 测试用：每2分钟备份一次（可删除，正式环境注释掉）
    schedule.every(10).seconds.do(auto_folder_backup)

    log_record("定时备份任务已启动，等待执行...")
    # 持续检测任务
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main_schedule()