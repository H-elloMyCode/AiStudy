import tkinter as tk

# root = tk.Tk()
# root.title("Label标签控件演示")
#
# root.geometry("400x200")
#
# label = tk.Label(
#     master=root,
#     text="这是Label标签\n支持换行显示",
#     font=("微软雅黑", 14),
#     fg="white",
#     bg="#2F4F4F",
#     padx=20,
#     pady=15
# )
#
# label.pack()
#
# root.mainloop()

# def btn_click():
#     """按钮点击后执行的操作"""
#     print("按钮被点击了!")
#     label.config(text="按钮已点击！")
#
# root = tk.Tk()
# root.title("Button按钮控件演示")
#
# root.geometry("400x200")
#
# label = tk.Label(root, text="请点击下方按钮", font=("微软雅黑", 12))
# label.pack(pady=20)
#
# btn = tk.Button(
#     master=root,
#     text="点击我",
#     font=("微软雅黑", 12),
#     width=10,
#     height=2,
#     bg="#4169E1",
#     fg="white",
#     command=btn_click
# )
#
# btn.pack()
#
# root.mainloop()

# def get_input():
#     input_text = entry.get()
#     print(f'输入框内容: {input_text}')
#
#     result_label.config(text=f'你输入的是: {input_text}')
#     entry.delete(0, tk.END)
#
# root = tk.Tk()
# root.title("Entry输入框控件演示")
#
# root.geometry("400x250")
#
# tip_label = tk.Label(root, text="请输入内容（单行）: ", font=("微软雅黑", 12))
# tip_label.pack(pady=10)
#
# entry = tk.Entry(
#     master=root,
#     font=("微软雅黑", 12),
#     width=30,
#     # show="*"
# )
#
# entry.pack(pady=5)
#
# get_btn = tk.Button(root, text="获取输入内容", font=("微软雅黑", 10), command=get_input)
# get_btn.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12), fg="red")
# result_label.pack()
#
# root.mainloop()

# def get_check_status():
#     hobby_list = []
#     if var1.get() == 1:
#         hobby_list.append("阅读")
#     if var2.get() == 1:
#         hobby_list.append("运动")
#     if var3.get() == 1:
#         hobby_list.append("编程")
#     result_label.config(text=f"你的爱好: {','.join(hobby_list) if hobby_list else '未勾选'}")
#
# root = tk.Tk()
# root.title("CheckButton复选框控件演示")
# root.geometry("400x300")
#
# tip_label = tk.Label(root, text="请选择你的爱好（可多选）: ", font=("微软雅黑", 12))
# tip_label.pack(pady=15)
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# var3 = tk.IntVar()
#
# c1 = tk.Checkbutton(
#     master=root,
#     text="阅读",
#     font=("微软雅黑", 11),
#     variable=var1
# )
#
# c1.pack(pady=5)
#
# c2 = tk.Checkbutton(
#     master=root,
#     text="运动",
#     font=("微软雅黑", 11),
#     variable=var2
# )
#
# c2.pack(pady=5)
#
# c3 = tk.Checkbutton(
#     master=root,
#     text="编程",
#     font=("微软雅黑", 11),
#     variable=var3
# )
#
# c3.pack(pady=5)
#
# get_btn = tk.Button(root, text="确认选择", font=("微软雅黑", 10), command=get_check_status)
# get_btn.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12), fg="blue")
# result_label.pack()
#
# root.mainloop()

# def get_radio_status():
#     gender = var.get()
#     print(f"选中的性别: {gender}")
#     result_label.config(text=f"你的性别: {gender}")
#
# root = tk.Tk()
# root.title("RadioButton单选框控件演示")
# root.geometry("400x250")
#
# tip_label = tk.Label(root, text="请选择你的性别（单选）: ", font=("微软雅黑", 12))
# tip_label.pack(pady=15)
#
# var = tk.StringVar()
# var.set("男")
#
# r1 = tk.Radiobutton(
#     master=root,
#     text="男",
#     font=("微软雅黑", 11),
#     variable=var,
#     value="男"
# )
# r1.pack(pady=5)
#
# r2 = tk.Radiobutton(
#     master=root,
#     text="女",
#     font=("微软雅黑", 11),
#     variable=var,
#     value="女"
# )
# r2.pack(pady=5)
#
#
# get_btn = tk.Button(root, text="确认选择", font=("微软雅黑", 10), command=get_radio_status)
# get_btn.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("微软雅黑", 12), fg="red")
# result_label.pack()
#
# root.mainloop()

# 定义提交信息函数
def submit_info():# 获取输入框内容
    name = entry_name.get()# 获取单选框姓名
    gender = var_gender.get()# 获取复选框爱好
    hobby_list = []
    if var_hobby1.get() == 1:
        hobby_list.append("阅读")
    if var_hobby2.get() == 1:
        hobby_list.append("运动")
    if var_hobby3.get() == 1:
        hobby_list.append("编程")
    # 拼接信息
    info = f"姓名：{name}\n性别：{gender}\n爱好：{','.join(hobby_list) if hobby_list else '无'}"
    # 显示结果
    result_label.config(text=info, justify="left")  # justify：文字左对齐
    entry_name.delete(0, tk.END)
    print("提交的信息：", info)

# 1. 创建主窗口
root = tk.Tk()
root.title("信息收集窗口（整合所有核心控件）")
root.geometry("450x400")

# 2. 姓名输入区域
label_name = tk.Label(root, text="姓名：", font=("微软雅黑", 11))
label_name.place(x=50, y=30)  # place布局：指定坐标
entry_name = tk.Entry(root, font=("微软雅黑", 11), width=25)
entry_name.place(x=100, y=30)

# 3. 性别单选区域
label_gender = tk.Label(root, text="性别：", font=("微软雅黑", 11))
label_gender.place(x=50, y=80)
var_gender = tk.StringVar()
var_gender.set("男")
r1 = tk.Radiobutton(root, text="男", font=("微软雅黑", 10), variable=var_gender, value="男")
r1.place(x=100, y=80)
r2 = tk.Radiobutton(root, text="女", font=("微软雅黑", 10), variable=var_gender, value="女")
r2.place(x=180, y=80)

# 4. 爱好复选区域
label_hobby = tk.Label(root, text="爱好：", font=("微软雅黑", 11))
label_hobby.place(x=50, y=130)
var_hobby1 = tk.IntVar()
var_hobby2 = tk.IntVar()
var_hobby3 = tk.IntVar()
c1 = tk.Checkbutton(root, text="阅读", font=("微软雅黑", 10), variable=var_hobby1)
c1.place(x=100, y=130)
c2 = tk.Checkbutton(root, text="运动", font=("微软雅黑", 10), variable=var_hobby2)
c2.place(x=180, y=130)
c3 = tk.Checkbutton(root, text="编程", font=("微软雅黑", 10), variable=var_hobby3)
c3.place(x=260, y=130)

# 5. 提交按钮
submit_btn = tk.Button(root, text="提交信息", font=("微软雅黑", 11), bg="#32CD32", fg="white", command=submit_info)
submit_btn.place(x=180, y=180)

# 6. 结果展示区域
result_label = tk.Label(root, text="", font=("微软雅黑", 11), justify="left")
result_label.place(x=50, y=230)

# 7. 启动消息循环
root.mainloop()