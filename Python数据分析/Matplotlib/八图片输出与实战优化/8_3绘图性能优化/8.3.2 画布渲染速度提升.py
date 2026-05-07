# import matplotlib

# matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["DejaVu Sans", "SimHei", "Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 100000000)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(7, 4), dpi=150)

ax.plot(x, y, linewidth=1, marker='', antialiased=False)

ax.grid(False)
ax.set_frame_on(True)
# ax.autoscale(enable=False)

plt.savefig("高速渲染图无Agg.png", bbox_inches='tight')
plt.close()

print("画布渲染速度提升完成！")
# plt.show()
