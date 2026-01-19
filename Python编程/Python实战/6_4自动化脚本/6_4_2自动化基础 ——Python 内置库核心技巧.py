# import os
#
# file_path = "test.txt"
# folder_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹"
import shutil
# if os.path.exists(file_path):
#     print(f"文件「{file_path}」存在")
# else:
#     print(f"文件「{file_path}」不存在")
#
# if os.path.exists(folder_path):
#     print(f"文件夹「{folder_path}」存在")
# else:
#     print(f"文件夹「{folder_path}」不存在")
#
# if os.path.isfile(file_path):
#     print(f"「{file_path}」是一个文件")
#
# if os.path.isdir(folder_path):
#     print(f"「{folder_path}」是一个目录")

# all_items = os.listdir(folder_path)
# print(f"文件夹内所有内容：{all_items}")
#
# file_list = []
# for item in all_items:
#     item_full_path = os.path.join(folder_path, item)
#     if os.path.isfile(item_full_path):
#         file_list.append(item)
#
# print(f"文件夹内所有文件：{file_list}")
#
# txt_file_list = [f for f in file_list if f.endswith(".txt")]
# print(f"文件夹内所有.txt文件：{txt_file_list}")

# def batch_rename_files():
#     folder_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹"
#     if not os.path.exists(folder_path):
#         print("文件夹不存在!")
#         return
#
#     file_list = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
#     for index, old_name in enumerate(file_list, start=1):
#         old_full_path = os.path.join(folder_path, old_name)
#
#         new_name = f"photo_{index}.jpg"
#         new_full_path = os.path.join(folder_path, new_name)
#
#         os.rename(old_full_path, new_full_path)
#         print(f"重命名成功：{old_name} → {new_name}")
#
# if __name__ == '__main__':
#     batch_rename_files()

# import os
# import shutil
#
#
# def copy_files_demo():
#     source_file = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹\\1.png"
#     target_file = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹\\1_copy.png"
#     target_folder = os.path.dirname(target_file)
#
#     if not os.path.exists(target_folder):
#         os.makedirs(target_folder)
#
#     shutil.copy2(source_file, target_file)
#     print(f"文件复制成功：{source_file} → {target_file}")
#
#     source_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹"
#     target_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹_copy"
#
#     shutil.copytree(source_dir, target_dir)
#     print(f"目录复制成功：{source_dir} → {target_dir}")
#
#
# if __name__ == '__main__':
#     copy_files_demo()

# import os
# import shutil
#
#
# def move_files_demo():
#     source_file = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹\\2.jpg"
#     target_file = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹\\2_move.jpg"
#     # target_folder = os.path.dirname(target_file)
#     #
#     # if not os.path.exists(target_folder):
#     #     os.makedirs(target_folder)
#
#     os.makedirs(os.path.dirname(target_file), exist_ok=True)
#
#     shutil.move(source_file, target_file)
#     print(f"文件移动成功：{source_file} → {target_file}")
#
#     source_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹_copy"
#     target_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹\\图片文件夹_copy_move"
#
#     shutil.move(source_dir, target_dir)
#     print(f"目录移动成功：{source_dir} → {target_dir}")
#
#
# if __name__ == '__main__':
#     move_files_demo()

# import os
# import shutil
#
#
# def delete_files_demo():
#     file_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹\\file_6.txt"
#     if os.path.isfile(file_path):
#         os.remove(file_path)
#         print(f"文件删除成功：{file_path}")
#
#     empty_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\空目录1"
#     if os.path.isdir(empty_dir):
#         os.rmdir(empty_dir)
#         print(f"空目录删除成功：{empty_dir}")
#
#     non_empty_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\非空目录1"
#     if os.path.isdir(non_empty_dir):
#         shutil.rmtree(non_empty_dir)
#         print(f"非空目录删除成功：{non_empty_dir}")
#
# if __name__ == '__main__':
#     delete_files_demo()
#

# crtwzxrsktxucjca

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# def send_text_email():
#     smtp_server = "smtp.qq.com"
#     smtp_port = 465
#     sender_email = "1612102142@qq.com"
#     sender_auth = "ogrlifccqklsehgi"
#     receiver_email = "helloworldhh2026@163.com"
#
#     mail_title = "【自动化通知】纯文本邮件测试"
#     mail_content = "这是一封由Python自动化脚本发送的纯文本邮件，无需手动发送！"
#
#     msg = MIMEText(mail_content, "plain", "utf-8")
#     msg["From"] = Header(sender_email, "utf-8")
#     msg["To"] = Header(receiver_email, "utf-8")
#     msg["Subject"] = Header(mail_title, "utf-8")
#
#     try:
#         with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#             server.login(sender_email, sender_auth)
#             server.sendmail(sender_email, receiver_email, msg.as_string())
#             print("纯文本邮件发送成功!")
#     except Exception as e:
#         print(f"邮件发送失败！错误信息：{e}")
#
# if __name__ == '__main__':
#     send_text_email()

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# def send_text_email():
#     # 配置信息
#     smtp_server = "smtp.qq.com"  # QQ邮箱SMTP服务器，固定不变
#     smtp_port = 465              # SSL加密端口，固定不变
#     sender_email = "dingjiaxiong@qq.com"  # 你的QQ发送邮箱，不用改
#     sender_auth = "ogrlifccqklsehgi"  # 【必改】替换成正确授权码
#     receiver_email = "helloworldhh2026@163.com"  # 收件人邮箱，不用改
#
#     # 邮件内容
#     mail_title = "【自动化通知】纯文本邮件测试"
#     mail_content = "这是一封由Python自动化脚本发送的纯文本邮件，无需手动发送！"
#
#     # 构建邮件对象
#     msg = MIMEText(mail_content, "plain", "utf-8")
#     msg["From"] = sender_email  # 发件人：纯字符串，无需Header
#     msg["To"] = receiver_email   # 收件人：纯字符串，无需Header
#     msg["Subject"] = Header(mail_title, "utf-8")  # 标题有中文，必须用Header格式化
#
#     try:
#         # 建立SSL加密连接，发送邮件
#         with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#             server.login(sender_email, sender_auth)
#             # 【关键修正】收件人必须传列表格式
#             server.sendmail(sender_email, [receiver_email], msg.as_string())
#             print("✅ 纯文本邮件发送成功!")
#     except Exception as e:
#         print(f"❌ 邮件发送失败！错误信息：{e}")
#
# if __name__ == '__main__':
#     send_text_email()

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# def send_text_email():
#     # 配置信息 全部不变 ✔️
#     smtp_server = "smtp.qq.com"
#     smtp_port = 465
#     sender_email = "dingjiaxiong@qq.com"
#     sender_auth = "ogrlifccqklsehgi"
#     receiver_email = "helloworldhh2026@163.com"
#
#     # 邮件内容 全部不变 ✔️
#     mail_title = "【自动化通知】纯文本邮件测试"
#     mail_content = "这是一封由Python自动化脚本发送的纯文本邮件，无需手动发送！"
#
#     # 构建邮件对象 全部不变 ✔️
#     msg = MIMEText(mail_content, "plain", "utf-8")
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = Header(mail_title, "utf-8")
#
#     try:
#         # ============ 只改这里 ↓↓↓ 核心修改 ============
#         server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 手动创建连接
#         server.login(sender_email, sender_auth)
#         server.sendmail(sender_email, [receiver_email], msg.as_string())
#         print("✅ 纯文本邮件发送成功!")
#         server.quit() # 用quit()优雅退出，而非close()强制关闭
#         # ============ 只改这里 ↑↑↑ 核心修改 ============
#     except Exception as e:
#         print(f"❌ 邮件发送失败！错误信息：{e}")
#
# if __name__ == '__main__':
#     send_text_email()

# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from email.header import Header
#
# def send_attachment_email():
#     # 配置信息 全部不变 ✔️
#     smtp_server = "smtp.qq.com"
#     smtp_port = 465
#     sender_email = "dingjiaxiong@qq.com"
#     sender_auth = "ogrlifccqklsehgi"
#     receiver_email = "helloworldhh2026@163.com"
#
#     attachment_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹\\file_1.txt"
#
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = Header("【自动化通知】带附件邮件测试", "utf-8")
#
#     mail_content = "这是一封带附件的自动化邮件，请查收附件！"
#     msg.attach(MIMEText(mail_content, "plain", "utf-8"))
#
#     if os.path.isfile(attachment_path):
#         with open(attachment_path, 'rb') as f:
#             mime = MIMEBase("application", "octet-stream")
#             mime.set_payload(f.read())
#             encoders.encode_base64(mime)
#
#             file_name = os.path.basename(attachment_path)
#             # ============ 核心修改 ↓↓↓ 就改这一行 ============
#             # 万能兼容：中英文文件名都不报错、不乱码
#             mime.add_header("Content-Disposition", "attachment", filename=("utf-8", "", file_name))
#             # ============ 核心修改 ↑↑↑ 结束 ============
#
#             msg.attach(mime)
#             print(f"附件「{file_name}」添加成功")
#
#     try:
#         server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#         server.login(sender_email, sender_auth)
#         server.sendmail(sender_email, [receiver_email], msg.as_string())
#         print("✅ 带附件邮件发送成功!")
#         server.quit()
#     except Exception as e:
#         print(f"❌ 邮件发送失败！错误信息：{e}")
#
# if __name__ == '__main__':
#     send_attachment_email()

import os

def backup_folder():
    source_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\图片文件夹"
    backup_dir = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\文件夹备份"

    import time
    backup_folder_name = f"备份_{time.strftime('%Y%m%d_%H%M%S')}"
    target_backup_dir = os.path.join(backup_dir, backup_folder_name)

    if not os.path.isdir(source_dir):
        print(f"错误：源文件夹「{source_dir}」不存在！")
        return False, "源文件夹不存在"

    os.makedirs(backup_dir, exist_ok=True)

    try:
        shutil.copytree(source_dir, target_backup_dir)
        backup_info = f"备份成功！\n源文件夹：{source_dir}\n备份路径：{target_backup_dir}"
        print(backup_info)
        return True, backup_info
    except Exception as e:
        error_info = f"备份失败！错误信息：{str(e)}"
        print(error_info)
        return False, error_info

def send_notify_email(backup_result, info):
    # 配置信息 全部不变 ✔️
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    sender_email = "dingjiaxiong@qq.com"
    sender_auth = "ogrlifccqklsehgi"
    receiver_email = "helloworldhh2026@163.com"

    if backup_result:
        title = "【自动化备份】文件夹备份成功通知"
        content = info
    else:
        title = "【自动化备份】文件夹备份失败警告"
        content = info

    # 构建邮件对象 全部不变 ✔️
    msg = MIMEText(content, "plain", "utf-8")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = Header(title, "utf-8")

    try:
        # ============ 只改这里 ↓↓↓ 核心修改 ============
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # 手动创建连接
        server.login(sender_email, sender_auth)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("✅ 纯文本邮件发送成功!")
        server.quit() # 用quit()优雅退出，而非close()强制关闭
        # ============ 只改这里 ↑↑↑ 核心修改 ============
    except Exception as e:
        print(f"❌ 邮件发送失败！错误信息：{e}")


if __name__ == '__main__':
    backup_result, backup_info = backup_folder()
    send_notify_email(backup_result, backup_info)