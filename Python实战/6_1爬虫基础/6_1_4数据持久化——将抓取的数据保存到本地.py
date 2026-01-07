import requests
from bs4 import BeautifulSoup


def get_parsed_data():
    target_url = 'https://www.baidu.com'

    nav_data_list = []
    nav_text_str = "百度首页导航信息\n=================\n"
    try:
        response = requests.get(target_url, timeout=5)
        response.raise_for_status()
        response.encoding = 'utf-8'
        html_content = response.text

        soup = BeautifulSoup(html_content, 'lxml')
        all_nav_tags = soup.find_all("a", class_="mnav")
        # print(all_nav_tags)
        for index, nav_tag in enumerate(all_nav_tags, 1):
            nav_text = nav_tag.text.strip()
            nav_href = nav_tag.get('href', '无链接')

            nav_dict = {"序号": index, "导航文本": nav_text, "链接地址": nav_href}
            nav_data_list.append(nav_dict)

            nav_text_str += f"{index}. 文本：{nav_text} | 链接：{nav_href}\n"
        print("数据解析完成，准备保存")
        return nav_data_list, nav_text_str
            # print(nav_dict)
    except requests.exceptions.RequestException as e:
        print(f"解析数据失败: {e}")
        return [], ""

def save_to_txt(text_content, file_path="baidu_nav.txt"):
    if not text_content:
        print("无有效文本数据，无需保存")
        return
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
            print(f"文本数据已成功保存到：{file_path}")

    except Exception as e:
        print(f"保存 TXT 失败: {e}")

import csv
def save_to_csv(data_list, file_path="baidu_nav.csv"):
    if not data_list:
        print("无有效结构化数据，无需保存")
        return

    try:
        header = data_list[0].keys()
        with open(file_path, 'w', encoding='utf-8', newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=header)
            csv_writer.writeheader()

            csv_writer.writerows(data_list)
            print(f"结构化数据已成功保存到：{file_path}")
    except Exception as e:
        print(f"保存 CSV 失败: {e}")

if __name__ == '__main__':
    nav_data, nav_text = get_parsed_data()
    # save_to_txt(nav_text)
    # print(nav_data, nav_text)
    save_to_csv(nav_data)