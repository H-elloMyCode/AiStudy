import tkinter as tk
from textwrap import fill

# root = tk.Tk()
# root.title("pack()布局演示")
# root.geometry("400x300")
#
# btn1 = tk.Button(root, text="按钮1", font=("微软雅黑", 12), bg="lightblue")
# btn2 = tk.Button(root, text="按钮2", font=("微软雅黑", 12), bg="lightgreen")
# btn3 = tk.Button(root, text="按钮3", font=("微软雅黑", 12), bg="lightcoral")
#
# # btn1.pack(pady=10, padx=20)
# # btn2.pack(pady=10, fill=tk.X, padx=20)
# # btn3.pack(pady=10, padx=20, anchor=tk.W)
#
# btn1.pack(side=tk.LEFT, padx=5, pady=50)
# btn2.pack(side=tk.LEFT, padx=5, pady=50)
# btn3.pack(side=tk.LEFT, padx=5, pady=50)
#
# root.mainloop()


# root = tk.Tk()
# root.title("grid()布局演示")
# root.geometry("350x200")
#
# label_user = tk.Label(root, text="账号: ", font=("微软雅黑", 12))
# label_pwd = tk.Label(root, text="密码: ", font=("微软雅黑", 12))
# entry_user = tk.Entry(root, font=("微软雅黑", 12), width=20)
# entry_pwd = tk.Entry(root, font=("微软雅黑", 12), width=20, show="*")
# btn_login = tk.Button(root, text="登录", font=("微软雅黑", 11), bg="#4169E1", fg="white")
# btn_cancel = tk.Button(root, text="取消", font=("微软雅黑", 11), bg="#DCDCDC")
#
# label_user.grid(row=0, column=0, pady=20, padx=10, sticky=tk.E)
# entry_user.grid(row=0, column=1, pady=20, padx=10)
#
# label_pwd.grid(row=1, column=0, pady=5, padx=10, sticky=tk.E)
# entry_pwd.grid(row=1, column=1, pady=5, padx=10)
#
# btn_login.grid(row=2, column=0, columnspan=2, pady=15, padx= 50)
# # btn_cancel.grid(row=2, column=1, pady=15, padx= 50)
#
# root.mainloop()

# root = tk.Tk()
# root.title("place()布局演示（精准定位）")
# root.geometry("400x300")
#
# label = tk.Label(root, text="精准定位的标签", font=("微软雅黑", 12), bg="lightyellow")
# btn = tk.Button(root, text="精准定位的按钮", font=("微软雅黑", 11), bg="lightblue")
#
# # label.place(x=100, y=50, width=200, height=30)
# # btn.place(x=150, y=120)
# label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#
# root.mainloop()

# import tkinter as tk

# import tkinter as tk

root = tk.Tk()
root.title("三种布局综合演示")
root.geometry("450x350")

# 1. pack()布局：标题标签（垂直居中，水平填充）→ 父容器：root
title_label = tk.Label(root, text="信息录入窗口", font=("微软雅黑", 14, "bold"), bg="#E6E6FA")
title_label.pack(fill=tk.X, pady=10)  # 水平填充，上下留白10

# ✅ 关键修复：新增一个Frame容器承载所有表单控件，解决pack/grid冲突
form_frame = tk.Frame(root)
form_frame.pack()  # Frame在root中用pack布局，内部可以自由用grid

# 2. grid()布局：表单内容（账号、年龄、性别）→ 父容器：form_frame（不是root了！）
# 账号
label_user = tk.Label(form_frame, text="账号：", font=("微软雅黑", 11))
entry_user = tk.Entry(form_frame, font=("微软雅黑", 11), width=25)
label_user.grid(row=0, column=0, pady=8, padx=50, sticky=tk.E)
entry_user.grid(row=0, column=1, pady=8, padx=10)

# 年龄
label_age = tk.Label(form_frame, text="年龄：", font=("微软雅黑", 11))
entry_age = tk.Entry(form_frame, font=("微软雅黑", 11), width=25)
label_age.grid(row=1, column=0, pady=8, padx=50, sticky=tk.E)
entry_age.grid(row=1, column=1, pady=8, padx=10)

# 性别 ✅修复两个BUG：公共变量+不重叠显示
label_gender = tk.Label(form_frame, text="性别：", font=("微软雅黑", 11))
gender_var = tk.StringVar(value="男")  # 定义公共变量，默认选中男
r1 = tk.Radiobutton(form_frame, text="男", font=("微软雅黑", 10), variable=gender_var, value="男")
r2 = tk.Radiobutton(form_frame, text="女", font=("微软雅黑", 10), variable=gender_var, value="女")
label_gender.grid(row=2, column=0, pady=8, padx=50, sticky=tk.E)
r1.grid(row=2, column=1, sticky=tk.W)
r2.grid(row=2, column=2, sticky=tk.W)  # 修改列数，横向并排不重叠

# 3. place()布局：提交按钮（精准定位在底部）→ 父容器：root，和pack共存无冲突
submit_btn = tk.Button(root, text="提交信息", font=("微软雅黑", 11), bg="#32CD32", fg="white")
submit_btn.place(x=180, y=280, width=100, height=30)  # 底部居中精准定位

# 启动消息循环
root.mainloop()