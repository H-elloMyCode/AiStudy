import time
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.use('Agg')

# 开始总计时
start_total = time.perf_counter()

# ===================== 字体设置 =====================
plt.rcParams["font.family"] = ["DejaVu Sans", "SimHei", "Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

# ===================== 生成数据（计时） =====================
start_data = time.perf_counter()
x = np.linspace(0, 10, 100000000)  # 1亿个点
y = np.sin(x)
end_data = time.perf_counter()

# ===================== 绘图渲染（计时） =====================
start_plot = time.perf_counter()
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
ax.plot(x, y, linewidth=1, marker='', antialiased=False)

ax.grid(False)
ax.set_frame_on(True)
end_plot = time.perf_counter()

# ===================== 保存图片（计时） =====================
start_save = time.perf_counter()
plt.savefig("高速渲染图无Agg2.png", bbox_inches='tight')
plt.close()
end_save = time.perf_counter()

# ===================== 总结束时间 =====================
end_total = time.perf_counter()

# ===================== 输出时间结果 =====================
print("="*50)
print(f"数据生成耗时：{end_data - start_data:.2f} 秒")
print(f"绘图渲染耗时：{end_plot - start_plot:.2f} 秒")
print(f"保存图片耗时：{end_save - start_save:.2f} 秒")
print(f"✅ 程序总耗时：{end_total - start_total:.2f} 秒")
print("="*50)

print("画布渲染速度提升完成！")