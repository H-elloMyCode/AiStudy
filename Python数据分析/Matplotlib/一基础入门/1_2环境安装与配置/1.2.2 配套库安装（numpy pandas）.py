import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print(np.__version__)
# print(pd.__version__)

# x = np.array([1, 2, 3, 4])
# y = x * 2
#
# plt.plot(x, y)
# plt.title('配套库安装成功')
# plt.show()

df = pd.read_csv('test_data.csv')
print(df)

plt.plot(df['x'], df['y'])
plt.title('pandas + matplotlib 正常使用')
plt.show()