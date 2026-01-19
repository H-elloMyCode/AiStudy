import pandas as pd
import numpy as np

# 定义3个文件的配置：文件名 + 数据列 + 数据行数
file_configs = [
    {
        "filename": "sales_data.xlsx",
        "columns": ["产品ID", "产品名称", "销售数量", "单价", "销售额"],
        "rows": 50
    },
    {
        "filename": "user_info.xlsx",
        "columns": ["用户ID", "用户名", "年龄", "性别", "注册时间"],
        "rows": 30
    },
    {
        "filename": "weather_data.xlsx",
        "columns": ["日期", "城市", "最高温度", "最低温度", "天气状况"],
        "rows": 20
    }
]

# 生成随机数据并写入Excel
for config in file_configs:
    data = {}
    # 为每一列生成随机数据
    for col in config["columns"]:
        if col in ["产品ID", "用户ID"]:
            data[col] = np.arange(1, config["rows"] + 1)
        elif col == "产品名称":
            data[col] = np.random.choice(["手机", "电脑", "耳机", "平板", "充电器"], config["rows"])
        elif col in ["销售数量", "单价", "销售额"]:
            data[col] = np.random.randint(1, 100, config["rows"])
        elif col == "用户名":
            data[col] = [f"user_{i}" for i in range(1, config["rows"] + 1)]
        elif col == "年龄":
            data[col] = np.random.randint(18, 60, config["rows"])
        elif col == "性别":
            data[col] = np.random.choice(["男", "女", "未知"], config["rows"])
        elif col == "注册时间":
            data[col] = pd.date_range(start="2025-01-01", periods=config["rows"], freq="D")
        elif col == "日期":
            data[col] = pd.date_range(start="2026-01-01", periods=config["rows"], freq="D")
        elif col == "城市":
            data[col] = np.random.choice(["北京", "上海", "广州", "深圳"], config["rows"])
        elif col in ["最高温度", "最低温度"]:
            data[col] = np.random.randint(-10, 35, config["rows"])
        elif col == "天气状况":
            data[col] = np.random.choice(["晴", "阴", "雨", "雪"], config["rows"])

    # 构建DataFrame并写入Excel
    df = pd.DataFrame(data)
    df.to_excel(config["filename"], index=False, engine="openpyxl")
    print(f"已生成文件: {config['filename']}")

print("3个Excel文件全部生成完成！")