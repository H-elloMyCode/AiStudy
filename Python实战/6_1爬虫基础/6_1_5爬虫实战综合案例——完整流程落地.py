import requests
from bs4 import BeautifulSoup
import csv
import time


def get_book_html():
    target_url = "https://book.douban.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        time.sleep(1)
        # response = requests.get(target_url, timeout=10)
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        print("✅ 网页抓取成功！")
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"❌ 网页抓取失败：{e}")
        return None


def parse_book_data(html_text):
    if not html_text:
        print("❌ 无HTML内容可解析")
        return [], ""

    book_data_list = []
    book_text_str = "豆瓣读书最新推荐书籍\n=====================\n"

    soup = BeautifulSoup(html_text, 'lxml')

    book_ul = soup.find("ul", class_="list-col list-col5 list-express slide-item")
    # print(book_ul)
    if not book_ul:
        print("⚠️ 未找到目标书籍列表，尝试备用选择器...")
        book_ul = soup.find("ul", class_=lambda c: c and "list-col" in c and "slide-item" in c)
        if not book_ul:
            print("❌ 未找到任何书籍列表")
            return [], ""

    book_tags = book_ul.find_all("li")
    # print(book_tags)
    for index, book_tag in enumerate(book_tags, 1):
        title_a = book_tag.find("div", class_="title").find("a") if book_tag.find("div", class_="title") else None
        # print(title_a)
        book_name = title_a.get("title", "").strip() if title_a else "未知书名"
        if not book_name and title_a:
            book_name = title_a.text.strip()

        # print(book_name)
        author_div = book_tag.find("div", class_="author")
        author = author_div.text.strip().replace("&nbsp;", "/") if author_div else "未知作者"
        # print(author)

        more_meta = book_tag.find("div", class_="more-meta")
        # print(more_meta)
        publish_year = "未知年份"
        publisher = "未知出版社"
        abstract = "无简介"

        if more_meta:
            year_span = more_meta.find("span", class_="year")
            if year_span:
                publish_year = year_span.text.strip()
            # print(publish_year)
            pub_span = more_meta.find("span", class_="publisher")
            if pub_span:
                publisher = pub_span.text.strip()
            # print(publisher)
            abstract_p = more_meta.find("p", class_="abstract")
            if abstract_p:
                abstract = abstract_p.text.strip().replace("\n", "").replace("  ", "")
            # print(abstract)

        cover_a = book_tag.find("div", class_="cover").find("a") if book_tag.find("div", class_="cover") else None
        # print(cover_a)
        book_url = cover_a.get("href", "") if cover_a else ""
        # print(book_url)
        cover_img = cover_a.find("img").get("src", "") if (cover_a and cover_a.find("img")) else ""
        # print(cover_img)

        book_dict = {
            "序号": index,
            "书名": book_name,
            "作者": author,
            "出版年份": publish_year,
            "出版社": publisher,
            "书籍链接": book_url,
            "封面图链接": cover_img,
            "简介": abstract
        }

        book_data_list.append(book_dict)
    # print(book_data_list)
        book_text_str += (
            f"{index}. 书名：{book_name}\n"
            f"   作者：{author}\n"
            f"   出版：{publish_year} | {publisher}\n"
            f"   链接：{book_url}\n"
            f"   ————————————————\n"
        )
    print(f"✅ 数据解析完成！共提取到{len(book_data_list)}本新书")
    return book_data_list, book_text_str

def save_book_to_txt(text_content, file_path="douban_new_books.txt"):
    if not text_content:
        print("❌ 无数据可保存到TXT文件")
        return
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        print(f"✅ TXT文件保存成功：{file_path}")
    except Exception as e:
        print(f"❌ 保存TXT失败：{e}")

def save_book_to_csv(data_list, file_path="douban_new_books.csv"):
    if not data_list:
        print("❌ 无数据可保存到CSV文件")
        return
    try:
        # 确保表头顺序固定（避免字典无序问题）
        header = ["序号", "书名", "作者", "出版年份", "出版社", "书籍链接", "封面图链接", "简介"]
        with open(file_path, "w", encoding="utf-8-sig", newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data_list)
        print(f"✅ CSV文件保存成功：{file_path}")
    except Exception as e:
        print(f"❌ 保存CSV失败：{e}")

if __name__ == '__main__':
    print("=== 豆瓣读书新书爬虫开始运行 ===")
    html_content = get_book_html()
    # print(html_content)
    book_data, book_text = parse_book_data(html_content)
    # print(book_data)
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(book_text)
    save_book_to_txt(book_text)
    save_book_to_csv(book_data)
    print("=== 豆瓣读书新书爬虫运行结束 ===")
