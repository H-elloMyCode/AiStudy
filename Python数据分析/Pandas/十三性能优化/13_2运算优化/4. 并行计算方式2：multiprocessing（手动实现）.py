import numpy as np
import pandas as pd
import multiprocessing as mp
import time

# 获取CPU核心数
cpu_cores = mp.cpu_count()


# ===================== 你的核心计算函数 =====================
def calc_net_profit(row):
    """计算单件净利润 + 总净利润（模拟复杂逻辑）"""
    base_profit = row['售价(元)'] - row['成本(元)'] - row['配送费(元)']
    discount_factor = 1 - row['促销折扣(%)'] / 100
    tax_factor = 1 - row['税率(%)'] / 100
    single_net = base_profit * discount_factor * tax_factor
    total_net = single_net * row['销量']
    return pd.Series([single_net, total_net])


# ===================== 分块处理函数 =====================
def apply_chunk(chunk):
    """分块应用计算函数"""
    return chunk.apply(calc_net_profit, axis=1)


# ===================== 并行计算主函数（已修复分块bug） =====================
def parallel_apply(df, func, axis=1):
    # 🔥 修复点：正确分割 DataFrame，保证每个 chunk 都是 DataFrame
    chunks = [df.iloc[i] for i in np.array_split(range(len(df)), cpu_cores)]

    # 创建进程池
    pool = mp.Pool(processes=cpu_cores)
    # 并行处理
    results = pool.map(apply_chunk, chunks)

    pool.close()
    pool.join()
    # 合并结果
    return pd.concat(results, ignore_index=True)


# ===================== 主程序入口 =====================
if __name__ == '__main__':
    print(f"检测到CPU核心数：{cpu_cores}")

    # 1. 读取你的数据
    file_path = r'parallel_compute.csv'
    df = pd.read_csv(file_path, encoding='utf-8')
    print(f"原始数据行数：{len(df)}")

    # 2. 放大数据
    df = pd.concat([df] * 10000, ignore_index=True)
    print(f"放大后数据行数：{len(df)}")

    # 3. 单线程计算
    print("\n开始单线程计算...")
    start_time = time.time()
    single_result = df.apply(calc_net_profit, axis=1)
    single_time = time.time() - start_time
    print(f"单线程耗时：{single_time:.4f} 秒")

    # 4. 多进程并行计算
    print("\n开始多进程并行计算...")
    start_time = time.time()
    df_result = parallel_apply(df, calc_net_profit, axis=1)
    df[['单件净利润_手动并行', '总净利润_手动并行']] = df_result
    manual_time = time.time() - start_time

    # 5. 输出结果
    speed_up_manual = single_time / manual_time
    print(f"\n多进程并行耗时：{manual_time:.4f} 秒")
    print(f"并行提速倍数：{speed_up_manual:.1f} 倍")
    print("\n计算完成！")