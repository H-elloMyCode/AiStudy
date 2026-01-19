# import tkinter as tk
# from tkinter import messagebox
#
# def show_info():
#     messagebox.showinfo("提示", "操作成功！这是普通信息弹窗")
#
# def show_warning():
#     messagebox.showwarning("警告", "请注意：输入内容不规范，请重新输入")
#
# def show_error():
#     messagebox.showerror("错误", "操作失败！请检查参数是否正确")
#
# def ask_confirm():
#     result = messagebox.askyesno("确认", "你确定要删除这条数据吗？")
#     if result:
#         tip_label.config(text="你选择了：是（删除数据）", fg="red")
#     else:
#         tip_label.config(text="你选择了：否（取消删除）", fg="blue")
#
# root = tk.Tk()
# root.title("消息弹窗演示")
# root.geometry("450x300")
#
# # 2. 创建控件
# tip_label = tk.Label(root, text="点击下方按钮触发对应弹窗", font=("微软雅黑", 12))
# btn_info = tk.Button(root, text="普通提示", font=("微软雅黑", 10), command=show_info)
# btn_warning = tk.Button(root, text="警告提示", font=("微软雅黑", 10), command=show_warning)
# btn_error = tk.Button(root, text="错误提示", font=("微软雅黑", 10), command=show_error)
# btn_confirm = tk.Button(root, text="确认弹窗", font=("微软雅黑", 10), command=ask_confirm)
#
# # 3. 布局控件
# tip_label.pack(pady=20)
# btn_info.pack(side=tk.LEFT, padx=20, pady=10)
# btn_warning.pack(side=tk.LEFT, padx=20, pady=10)
# btn_error.pack(side=tk.LEFT, padx=20, pady=10)
# btn_confirm.pack(side=tk.LEFT, padx=20, pady=10)
#
# root.mainloop()

# import tkinter as tk
# from tkinter import simpledialog
#
#
# def get_user_input():
#     user_input = simpledialog.askstring(
#         title="输入提示",
#         prompt="请输入你的姓名: ",
#         initialvalue="张三"
#     )
#     if user_input is not None and user_input.strip() != "":
#         result_label.config(text=f'你好, {user_input}!', fg="green")
#     else:
#         result_label.config(text="你未输入有效内容（或取消输入）", fg="red")
#
#
# root = tk.Tk()
# root.title("输入弹窗演示")
# root.geometry("400x200")
#
# btn_input = tk.Button(root, text="弹出输入框", font=("微软雅黑", 12), command=get_user_input)
# result_label = tk.Label(root, text="", font=("微软雅黑", 12))
#
# btn_input.pack(pady=30)
# result_label.pack(pady=20)
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.title("Frame容器演示")
# root.geometry("450x350")
#
# title_frame = tk.Frame(root, bg="#E6E6FA")
# operate_frame = tk.Frame(root, bg="#F5F5F5")
# result_frame = tk.Frame(root, bg="#FFFFFF", bd=1, relief=tk.SUNKEN)
#
# title_label = tk.Label(title_frame, text="Frame容器演示（界面分层）", font=("微软雅黑", 14, "bold"), bg="#E6E6FA")
# btn1 = tk.Button(operate_frame, text="按钮1", font=("微软雅黑", 10), width=8)
# btn2 = tk.Button(operate_frame, text="按钮2", font=("微软雅黑", 10), width=8)
# btn3 = tk.Button(operate_frame, text="按钮3", font=("微软雅黑", 10), width=8)
#
# result_label = tk.Label(result_frame, text="操作结果将显示在这里", font=("微软雅黑", 12), fg="blue", bg="#FFFFFF")
#
# title_label.pack(pady=10)
# btn1.pack(side=tk.LEFT, padx=20, pady=15)
# btn2.pack(side=tk.LEFT, padx=20, pady=15)
# btn3.pack(side=tk.LEFT, padx=20, pady=15)
# result_label.pack(pady=20)
#
# title_frame.pack(fill=tk.X)
# operate_frame.pack(pady=10)
# result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
#
# root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog


def collect_info():
    name = simpledialog.askstring("姓名采集", "请输入你的姓名: ")
    if not name or name.strip() == "":
        messagebox.showwarning("警告", "姓名不能为空!")
        return
    age = simpledialog.askstring("年龄采集", "请输入你的年龄：")
    if not age or not age.isdigit():
        messagebox.showwarning("错误", "年龄必须是有效数字！")
        return

    messagebox.showinfo("成功", f'信息采集成功！\n姓名：{name}\n年龄：{age}')
    result_label.config(text=f"姓名：{name}\n年龄：{age}", justify=tk.LEFT)


root = tk.Tk()
root.title("用户信息采集（弹窗+Frame整合）")
root.geometry("400x300")

top_frame = tk.Frame(root, bg="#E6E6FA")
bottom_frame = tk.Frame(root)

tip_label = tk.Label(top_frame, text="点击按钮采集用户信息", font=("微软雅黑", 12), bg="#E6E6FA")
collect_btn = tk.Button(top_frame, text="采集信息", font=("微软雅黑", 11), bg="#4169E1", fg="white",
                        command=collect_info)

result_title = tk.Label(bottom_frame, text="采集结果：", font=("微软雅黑", 12, "bold"))
result_label = tk.Label(bottom_frame, text="暂无信息", font=("微软雅黑", 11), fg="blue")

tip_label.pack(pady=10)
collect_btn.pack(pady=5)
result_title.pack(pady=10)
result_label.pack()

top_frame.pack(fill=tk.X)
bottom_frame.pack(pady=20)

root.mainloop()
