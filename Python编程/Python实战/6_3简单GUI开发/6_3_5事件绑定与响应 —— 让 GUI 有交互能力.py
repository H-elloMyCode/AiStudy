import tkinter as tk

# def btn_click_response():
#     result_label.config(text="按钮被点击了！", fg="red")
#     print("命令式绑定: 按钮点击事件触发")
#
# root = tk.Tk()
# root.title("命令式绑定（command参数）演示")
# root.geometry("400x200")
#
# tip_label = tk.Label(root, text="请点击下方按钮", font=("微软雅黑", 12))
#
# click_btn = tk.Button(
#     root,
#     text="点击我",
#     font=("微软雅黑", 12),
#     bg="#4169E1",
#     fg="white",
#     command=btn_click_response
# )
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12))
#
# tip_label.pack(pady=20)
# click_btn.pack(pady=10)
# result_label.pack(pady=10)
#
# root.mainloop()

# def btn_click_with_param(name, age):
#     result_text = f"姓名: {name}, 年龄: {age}"
#     result_label.config(text=result_text, fg="blue")
#     print(f"命令式绑定（带参数）：{result_text}")
#
# root = tk.Tk()
# root.title("带参数的command绑定（lambda）")
# root.geometry("400x200")
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12))
# result_label.pack(pady=30)
#
# btn1 = tk.Button(
#     root,
#     text="传递参数1",
#     font=("微软雅黑", 10),
#     command=lambda: btn_click_with_param("张三", 20)
# )
#
# btn2 = tk.Button(
#     root,
#     text="传递参数2",
#     font=("微软雅黑", 10),
#     command=lambda: btn_click_with_param("李四", 25)
# )
#
# btn1.pack(side=tk.LEFT, padx=50, pady=10)
# btn2.pack(side=tk.LEFT, padx=50, pady=10)
#
# root.mainloop()

# def mouse_click(event):
#     click_info = f"左键点击：x={event.x}, y={event.y}"
#     result_label.config(text=click_info, fg="red")
#     print(f"通用绑定：{click_info}")
#
# def mouse_right_click(event):
#     right_info = "右键点击：禁止操作！"
#     result_label.config(text=right_info, fg="orange")
#     print(f"通用绑定：{right_info}")
#
# def mouse_move(event):
#     move_info = f"鼠标移动：x={event.x}, y={event.y}"
#     # 实时更新鼠标位置（不打印控制台，避免刷屏）
#     move_label.config(text=move_info)
#
#
# root = tk.Tk()
# root.title("通用事件绑定（鼠标事件）演示")
# root.geometry("450x250")
#
# click_label = tk.Label(
#     root,
#     text="点击我（左键/右键）\n或在我身上移动鼠标",
#     font=("微软雅黑", 11),
#     bg="#E6E6FA",
#     padx=20,
#     pady=15
# )
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12))
# move_label = tk.Label(root, text="", font=("微软雅黑", 10), fg="gray")
#
# click_label.bind("<Button-1>", mouse_click)
# click_label.bind("<Button-3>", mouse_right_click)
# click_label.bind("<Motion>", mouse_move)
#
# click_label.pack(pady=20)
# result_label.pack(pady=10)
# move_label.pack(pady=10)
#
# root.mainloop()

# def key_press(event):
#     """任意键盘按键按下响应"""
#     # event.keysym：获取按键名称（如a、Enter、Shift_L）
#     key_info = f"按下按键：{event.keysym}"
#     result_label.config(text=key_info, fg="blue")
#     print(f"通用绑定：{key_info}")
#
# # 定义指定按键（Enter键）响应函数
# def enter_key_press(event):
#     """Enter键按下响应"""
#     enter_info = "Enter键按下：提交成功！"
#     result_label.config(text=enter_info, fg="green")
#     print(f"通用绑定：{enter_info}")
#
# # 1. 创建主窗口
# root = tk.Tk()
# root.title("通用事件绑定（键盘事件）演示")
# root.geometry("400x200")
#
# # 2. 创建控件
# tip_label = tk.Label(root, text="请先点击窗口激活，再按键盘", font=("微软雅黑", 11))
# result_label = tk.Label(root, text="", font=("微软雅黑", 12))
#
# # 3. 绑定键盘事件（绑定到root窗口，全局监听）
# root.bind("<KeyPress>", key_press)  # 任意按键
# root.bind("<KeyPress-Return>", enter_key_press)  # Enter键（Return=Enter）
#
# # 4. 布局控件
# tip_label.pack(pady=30)
# result_label.pack(pady=20)
#
# # 5. 启动消息循环
# root.mainloop()

# import tkinter as tk

# import tkinter as tk
# from tkinter import ttk

# 定义按钮输入响应函数（command绑定，带参数）
def btn_input(num):
    """按钮输入数字或符号"""
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(num))
    # 输入新内容时清空结果提示
    result_label.config(text="", fg="blue")

# 定义计算响应函数（command绑定，无参数）
def calc_add():
    """执行加法计算，增强容错逻辑"""
    try:
        input_text = entry.get().strip()
        # 判空
        if not input_text:
            result_label.config(text="提示：请输入计算表达式", fg="orange")
            return
        # 判断是否包含加号
        if "+" not in input_text:
            result_label.config(text="格式错误：请输入加法表达式（如12+34）", fg="red")
            return
        # 处理连续加号、首尾是加号的情况
        num_list = input_text.split("+")
        num_list = [n.strip() for n in num_list if n.strip()]  # 过滤空值
        if len(num_list) < 2:
            result_label.config(text="格式错误：请勿输入连续加号/首尾加号", fg="red")
            return
        # 遍历计算总和，支持多个数相加（如 1+2+3+4）
        total = 0.0
        for num_str in num_list:
            total += float(num_str)
        # 显示结果，保留两位小数更美观
        result_label.config(text=f"计算结果：{input_text} = {round(total, 2)}", fg="green")
        entry.delete(0, tk.END)
    except ValueError:
        result_label.config(text="输入错误：请输入纯数字（支持小数）", fg="red")
    except Exception as e:
        result_label.config(text=f"系统错误：{str(e)}", fg="red")

# 定义清空输入框函数
def clear_input():
    """清空输入框和结果提示"""
    entry.delete(0, tk.END)
    result_label.config(text="", fg="blue")

# 定义键盘回车响应函数（bind绑定，接收event参数）
def key_enter(event):
    """键盘Enter键触发计算"""
    calc_add()  # 复用计算函数

# 1. 创建主窗口
root = tk.Tk()
root.title("简易加法计算器（优化完整版）")
root.geometry("380x350")  # 扩大窗口适配
root.resizable(False, False)  # 固定窗口大小，不允许拉伸

# 2. 创建控件 - 统一美化样式
entry = tk.Entry(root, font=("微软雅黑", 16), width=22, justify=tk.RIGHT)
entry.config(bg="#f8f9fa", bd=2, relief=tk.GROOVE)  # 输入框浅背景+边框
result_label = tk.Label(root, text="", font=("微软雅黑", 12), height=2)

# 数字按钮（1-9、0）、+号、=号、清空按钮
btn_1 = tk.Button(root, text="1", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(1), bg="#ffffff")
btn_2 = tk.Button(root, text="2", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(2), bg="#ffffff")
btn_3 = tk.Button(root, text="3", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(3), bg="#ffffff")
btn_4 = tk.Button(root, text="4", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(4), bg="#ffffff")
btn_5 = tk.Button(root, text="5", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(5), bg="#ffffff")
btn_6 = tk.Button(root, text="6", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(6), bg="#ffffff")
btn_7 = tk.Button(root, text="7", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(7), bg="#ffffff")
btn_8 = tk.Button(root, text="8", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(8), bg="#ffffff")
btn_9 = tk.Button(root, text="9", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(9), bg="#ffffff")
btn_0 = tk.Button(root, text="0", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input(0), bg="#ffffff")
btn_plus = tk.Button(root, text="+", font=("微软雅黑", 12), width=5, height=1, command=lambda: btn_input("+"), bg="#FFD700")
btn_eq = tk.Button(root, text="=", font=("微软雅黑", 12), width=5, height=1, command=calc_add, bg="#32CD32", fg="#ffffff")
btn_clear = tk.Button(root, text="C", font=("微软雅黑", 12), width=5, height=1, command=clear_input, bg="#FF6347", fg="#ffffff")

# 3. 布局控件 - 统一用grid，彻底解决布局错乱问题【核心修复】
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=15)
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# 数字按钮网格布局
btn_7.grid(row=2, column=0, padx=5, pady=5)
btn_8.grid(row=2, column=1, padx=5, pady=5)
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_4.grid(row=3, column=0, padx=5, pady=5)
btn_5.grid(row=3, column=1, padx=5, pady=5)
btn_6.grid(row=3, column=2, padx=5, pady=5)
btn_1.grid(row=4, column=0, padx=5, pady=5)
btn_2.grid(row=4, column=1, padx=5, pady=5)
btn_3.grid(row=4, column=2, padx=5, pady=5)
btn_0.grid(row=5, column=0, padx=5, pady=5)
btn_plus.grid(row=5, column=1, padx=5, pady=5)
btn_eq.grid(row=5, column=2, padx=5, pady=5)
btn_clear.grid(row=6, column=1, padx=5, pady=8)  # 清空按钮居中

# 4. 绑定事件
root.bind("<KeyPress-Return>", key_enter)  # 绑定回车触发计算
root.bind("<KP_Enter>", key_enter)         # 兼容小键盘回车
entry.focus_set()  # 默认聚焦输入框，支持键盘直接输入

# 5. 启动消息循环
root.mainloop()