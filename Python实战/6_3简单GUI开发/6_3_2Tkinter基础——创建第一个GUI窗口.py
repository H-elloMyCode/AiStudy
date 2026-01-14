import tkinter as tk

root = tk.Tk()

root.title("我的第一个 Tkinter 窗口")
root.geometry("500x300")

label = tk.Label(
    master=root,
    text="你好，Tkinter！这是我的第一个GUI窗口",
    font=("微软雅黑", 12),
    fg="blue"
)

label.pack(pady=50)

# root.resizable(False, False)

root.mainloop()