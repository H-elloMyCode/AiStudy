# import pyautogui
# import os
#
#
# def auto_notepad_operation():
#     try:
#         os.system("start notepad")
#         pyautogui.sleep(2)
#
#         text_content = "Pythonpyautogui2026-01-19"
#         pyautogui.typewrite(text_content, interval=0.05)
#         pyautogui.sleep(1)
#
#         pyautogui.hotkey("ctrl", "s")
#         pyautogui.sleep(2)
#
#         file_name = "pyautogui.txt"
#         pyautogui.typewrite(file_name, interval=0.05)
#         pyautogui.sleep(0.5)
#
#         pyautogui.press("enter")
#         pyautogui.sleep(1)
#
#         pyautogui.hotkey("alt", "f4")
#         print("记事本自动化操作完成！文件已保存为：", file_name)
#
#     except Exception as e:
#         print(f"操作失败！错误信息：{e}")
#
#
# if __name__ == '__main__':
#     auto_notepad_operation()
# import os.path
#
# import pyautogui
# import time
#
# def auto_screenshot_operation():
#     save_folder = "./自动化截图"
#
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#
#     try:
#         print("开始全屏截图")
#         pyautogui.sleep(2)
#
#         full_screen_name = f"全屏截图_{time.strftime('%Y%m%d_%H%M%S')}.png"
#         full_screen_path = os.path.join(save_folder, full_screen_name)
#
#         pyautogui.screenshot(full_screen_path)
#         print(f"全屏截图保存成功：{full_screen_path}")
#
#         print("开始指定区域截图...")
#         pyautogui.sleep(2)
#
#         screenshot_region = (100, 100, 800, 600)
#         region_name = f"指定区域截图_{time.strftime('%Y%m%d_%H%M%S')}.png"
#         region_path = os.path.join(save_folder, region_name)
#
#         pyautogui.screenshot(region_path, region=screenshot_region)
#         print(f"指定区域截图保存成功：{region_path}")
#
#     except Exception as e:
#         print(f"截图失败！错误信息：{e}")
#
#
# if __name__ == '__main__':
#     auto_screenshot_operation()

import pyautogui
import time
import os

# def auto_mouse_operation():
#     try:
        # this_pc_x, this_pc_y = 50, 50
        # print(f"移动鼠标到：({this_pc_x}, {this_pc_y})")
        # pyautogui.moveTo(this_pc_x, this_pc_y, duration=1)
        # pyautogui.sleep(0.5)
        #
        # pyautogui.doubleClick(this_pc_x, this_pc_y)
        # print("成功打开「此电脑」")
        # pyautogui.sleep(3)
        # drag_start_x, drag_start_y = 200, 200
        # drag_end_x, drag_end_y = 100, 100
        # print(f"拖拽文件：({drag_start_x}, {drag_start_y}) → ({drag_end_x}, {drag_end_y})")
        # pyautogui.moveTo(drag_start_x, drag_start_y, duration=0.5)
        # pyautogui.dragTo(drag_end_x, drag_end_y, duration=1, button='left')  # 左键拖拽
        # pyautogui.sleep(1)
        # print("拖拽操作完成")

        # print("向下滚动鼠标滚轮...")
        # pyautogui.moveTo(300, 300)
        # pyautogui.scroll(-500, x=300, y=300)  # 在(300,300)位置向下滚动500单位
        # pyautogui.sleep(1)
        # print("滚动操作完成")

#         os.system("start notepad")
#         pyautogui.sleep(2)
#
#         pyautogui.hotkey("alt", "f4")
#
#     except Exception as e:
#         print(f"鼠标操作失败！错误信息：{e}")
#
#
# if __name__ == '__main__':
#     auto_mouse_operation()

import pyautogui
import os
import time


def auto_desktop_office_flow():
    """桌面办公自动化组合流程"""
    # 配置参数
    save_screenshot_folder = "./办公自动化截图"
    notepad_file_name = "testtest.txt"
    # 创建截图文件夹
    if not os.path.exists(save_screenshot_folder):
        os.makedirs(save_screenshot_folder)

    try:
        # 步骤1：打开记事本
        os.system("start notepad")
        pyautogui.sleep(2)
        print("步骤1：记事本已打开")

        # 步骤2：输入文本
        """
        桌面办公自动化组合流程演示\n
        1. 自动打开记事本\n2. 输入指定文本\n3. 截图保存\n4. 保存并关闭记事本\n
        """
        pyautogui.hotkey("ctrl", "v")
        pyautogui.sleep(1)
        print("步骤2：文本输入完成")

        # 步骤4：保存记事本文件
        pyautogui.hotkey("ctrl", "s")
        pyautogui.sleep(2)
        pyautogui.typewrite(notepad_file_name, interval=0.1)
        pyautogui.press("enter")
        pyautogui.sleep(1)
        print(f"步骤3：记事本文件保存成功，文件名：{notepad_file_name}")

        # 步骤5：关闭记事本
        pyautogui.hotkey("alt", "f4")
        print("步骤4：记事本已关闭")

        # 步骤3：截图保存（记事本窗口区域）
        screenshot_name = f"test_{time.strftime('%Y%m%d_%H%M%S')}.png"
        screenshot_path = os.path.join(save_screenshot_folder, screenshot_name)

        # 自定义记事本区域（可根据实际情况调整）
        notepad_region = (50, 50, 600, 400)
        pyautogui.screenshot(screenshot_path, region=notepad_region)
        print(f"步骤5：截图保存成功，路径：{screenshot_path}")

        print("\n========== 桌面办公自动化组合流程全部完成！ ==========")
    except Exception as e:
        print(f"组合流程执行失败！错误信息：{e}")


# 主程序执行
if __name__ == "__main__":
    auto_desktop_office_flow()