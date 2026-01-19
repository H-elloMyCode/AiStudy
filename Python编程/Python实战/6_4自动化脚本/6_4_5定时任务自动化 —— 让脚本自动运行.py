# import time
# from datetime import datetime
#
#
# def target_task():
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"【任务执行成功】当前时间：{current_time} | 执行目标任务")
#
#     with open("定时任务日志.txt", "a", encoding="utf-8") as f:
#         f.write(f"固定间隔任务执行：{current_time}\n")
# #
#
# def fixed_interval_schedule(interval_seconds):
#     print(f"固定间隔定时任务已启动 | 间隔：{interval_seconds}秒")
#     print("====================================\n")
#     try:
#         while True:
#             target_task()
#             time.sleep(interval_seconds)
#     except KeyboardInterrupt:
#         print("\n====================================")
#         print("固定间隔定时任务已手动终止")
#     except Exception as e:
#         print(f"\n任务执行异常：{e}")
#
#
# if __name__ == '__main__':
#     interval = 5
#     fixed_interval_schedule(interval)

# import schedule
# import time
# from datetime import datetime
#
#
# def target_task():
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     task_info = f"【任务执行成功】当前时间：{current_time} | 执行目标任务"
#     print(task_info)
#     with open("复杂定时任务日志.txt", "a", encoding="utf-8") as f:
#         f.write(f"{task_info}\n")
#
#
# def flexible_schedule():
#     schedule.every(5).seconds.do(target_task)
#
#     schedule.every().day.at("23:52").do(target_task)
#
#     schedule.every().friday.at("18:00").do(target_task)
#
#     print("灵活定时任务已启动 | 支持多规则并发执行")
#     print("====================================\n")
#
#     try:
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\n====================================")
#         print("灵活定时任务已手动终止")
#     except Exception as e:
#         print(f"\n任务执行异常：{e}")
#
#
# if __name__ == '__main__':
#     flexible_schedule()

