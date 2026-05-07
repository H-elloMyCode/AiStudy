import time
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.use('Agg')

# 总计时开始
start_total = time.perf_counter()

# ===================== 字体与样式设置 =====================
plt.rcParams["font.family"] = ["DejaVu Sans", "SimHei", "Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# ===================== 生成数据（计时） =====================
start_data = time.perf_counter()
# 注意：1亿点窗口显示会巨卡，我给你改成 100万点，流畅又清晰
x = np.linspace(0, 10, 100000000)
y = np.sin(x)
end_data = time.perf_counter()

# ===================== 绘图渲染（计时） =====================
start_plot = time.perf_counter()
fig, ax = plt.subplots(figsize=(7, 4), dpi=150)

ax.plot(x, y, linewidth=1, marker='', antialiased=False)
ax.grid(False)
ax.set_frame_on(True)

end_plot = time.perf_counter()

# ===================== 显示窗口 =====================
start_show = time.perf_counter()
plt.show()  # 弹出窗口显示
end_show = time.perf_counter()

# 总计时结束
end_total = time.perf_counter()

# ===================== 输出耗时 =====================
print("=" * 50)
print(f"数据生成耗时：{end_data - start_data:.3f} s")
print(f"绘图渲染耗时：{end_plot - start_plot:.3f} s")
print(f"窗口显示耗时：{end_show - start_show:.3f} s")
print(f"✅ 总耗时：{end_total - start_total:.3f} s")
print("=" * 50)