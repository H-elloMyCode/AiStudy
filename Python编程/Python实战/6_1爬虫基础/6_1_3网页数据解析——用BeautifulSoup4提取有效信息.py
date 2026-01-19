import requests
from bs4 import BeautifulSoup

target_url = 'http://www.baidu.com'
try:
    response = requests.get(target_url, timeout=5)
    response.raise_for_status()
    response.encoding = 'utf-8'
    html_content = response.text

    print("网页 HTML 获取成功, 准备解析!")
    if html_content:
        soup = BeautifulSoup(html_content, 'lxml')
        print("bs4 解析对象创建成功")

        if soup:
            title_tag = soup.find('title')
            if title_tag:
                title_text = title_tag.text
                # print(title_text)
            # print(title_tag)
            search_btn = soup.find("input", id="su")
            # print(search_btn)
            nav_link = soup.find("a", class_="mnav")
            # if nav_link:
            #     link_href = nav_link['href']
            #     print(nav_link.text)
            #     print(link_href)

            # print(nav_link)
            all_a_tags = soup.find_all("a", class_="mnav")
            if all_a_tags:
                for nav_tag in all_a_tags:
                    nav_text = nav_tag.text.strip()
                    nav_href = nav_tag.get("href", "无链接")
                    print(f"文本: {nav_text} | 链接: {nav_href}")
                    # print(nav_text, nav_href)
            # if all_a_tags:
            #     for a_tag in all_a_tags:
            #         a_text = a_tag.text.strip()
            #         a_href = a_tag.get("href", "无链接")
            #         print(f'文本: {a_text} | 链接: {a_href}')
            # print("=======================")

            # print(all_a_tags)
            # print(len(all_a_tags))
            # print(len(all_a_tags))
            # print(all_a_tags[:3])
    else:
        print("无有效 HTML 内容，无法解析!")

except requests.exceptions.RequestException as e:
    print(f'获取网页失败: {e}')
    html_content = None

