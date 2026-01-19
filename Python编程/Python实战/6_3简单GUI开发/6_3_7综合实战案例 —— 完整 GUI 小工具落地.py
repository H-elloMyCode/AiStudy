import tkinter as tk
from tkinter import messagebox

def clear_text():
    if text_box.get("1.0", tk.END).strip() != "":
        text_box.delete("1.0", tk.END)
        messagebox.showinfo("提示", "文本已成功清空!")
    else:
        messagebox.showwarning("警告", "文本框已为空，无需清空！")

def to_upper():
    text_content = text_box.get(1.0, tk.END)
    if text_content.strip() == "":
        messagebox.showwarning("警告", "请先输入文本内容！")
        return
    # 删除原有内容，插入大写文本
    text_box.delete(1.0, tk.END)
    text_box.insert(1.0, text_content.upper())
    messagebox.showinfo("提示", "文本已成功转为大写！")

def to_lower():
    text_content = text_box.get(1.0, tk.END)
    if text_content.strip() == "":
        messagebox.showwarning("警告", "请先输入文本内容！")
        return
    text_box.delete(1.0, tk.END)
    text_box.insert(1.0, text_content.lower())
    messagebox.showinfo("提示", "文本已成功转为小写！")

def save_to_file():
    text_content = text_box.get(1.0, tk.END)
    if text_content.strip() == "":
        messagebox.showerror("错误", "无有效文本可保存！")
        return
    try:
        # 写入文件（utf-8编码，避免中文乱码）
        with open("文本处理结果.txt", "w", encoding="utf-8") as f:
            f.write(text_content)
        messagebox.showinfo("成功", "文本已保存到「文本处理结果.txt」！")
    except Exception as e:
        messagebox.showerror("保存失败", f"错误信息：{str(e)}")

root = tk.Tk()
root.title("简易文本处理工具（Tkinter综合实战）")
root.geometry("600x700")
root.iconbitmap("bitbug_favicon.ico")
root.resizable(True, True)

text_frame = tk.Frame(root, bg="#F5F5F5", bd=1, relief=tk.SUNKEN)
btn_frame = tk.Frame(root, bg="#E6E6FA")

text_frame.pack(expand=True, padx=10, pady=10)
btn_frame.pack(padx=10, pady=5)

text_box = tk.Text(
    text_frame,
    font=("微软雅黑", 11),
    bg="white",
    fg="#333333",
    wrap=tk.WORD
)
text_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

btn_clear = tk.Button(
    btn_frame,
    text="清空文本",
    font=("微软雅黑", 10),
    width=12,
    bg="#FF6B6B",
    fg="white")
btn_upper = tk.Button(
    btn_frame,
    text="转为大写",
    font=("微软雅黑", 10),
    width=12,
    bg="#4ECDC4",
    fg="white")
btn_lower = tk.Button(
    btn_frame,
    text="转为小写",
    font=("微软雅黑", 10),
    width=12,
    bg="#45B7D1",
    fg="white")
btn_save = tk.Button(
    btn_frame,
    text="保存到文件",
    font=("微软雅黑", 10),
    width=12,
    bg="#96CEB4",
    fg="white")

btn_clear.grid(row=0, column=0, padx=15, pady=10)
btn_upper.grid(row=0, column=1, padx=15, pady=10)
btn_lower.grid(row=0, column=2, padx=15, pady=10)
btn_save.grid(row=0, column=3, padx=15, pady=10)
btn_clear.config(command=clear_text)
btn_upper.config(command=to_upper)
btn_lower.config(command=to_lower)
btn_save.config(command=save_to_file)

if __name__ == '__main__':
    root.mainloop()