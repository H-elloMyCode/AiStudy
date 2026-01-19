# import openpyxl
#
# print(openpyxl.__version__)

import os


def batch_rename_txt():
    folder_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试文件夹"
    # folder_path = "D:\\Projects\\AiStudy\\Python实战\\6_4自动化脚本\\测试件夹"
    if not os.path.exists(folder_path):
        print(f"错误：文件夹「{folder_path}」不存在！")
        return

    file_list = os.listdir(folder_path)
    txt_file_list = [file for file in file_list if file.endswith(".txt")]

    if len(txt_file_list) == 0:
        print("提示：文件夹内无.txt文件，无需重命名！")
        return

    for index, file_name in enumerate(txt_file_list, start=1):
        old_file_path = os.path.join(folder_path, file_name)
        new_file_name = f"file_{index}.txt"
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)
        print(f"重命名成功：{file_name} → {new_file_name}")

    print(f"\n全部完成！共重命名 {len(txt_file_list)} 个.txt文件")

if __name__ == '__main__':
    batch_rename_txt()