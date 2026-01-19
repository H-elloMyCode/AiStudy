# import urllib.request
#
# reuq = urllib.request.urlopen('http://httpbin.org/get')

import requests


def get_web_content():
    target_url = 'http://www.baidu.com'

    try:
        response = requests.get(target_url, timeout=5)

        response.encoding = 'utf-8'

        print(response.status_code)
        if response.status_code == 200:
            print("请求成功! 可以继续获取网页内容")

            html_content = response.text
            # print("网页 HTML 内容（前 500 字符）: \n", html_content[:500])
            if "<title>" in html_content and "</title>" in html_content:
                title_start = html_content.find("<title>") + len("<title>")
                title_end = html_content.find("</title>")
                # print()

                web_title = html_content[title_start:title_end]
                return web_title
        else:
            print(f'请求失败，状态码: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'网络请求失败: {e}')
        return None

if __name__ == '__main__':
    web_title = get_web_content()
    print(web_title)
