import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

title = soup.title.text
print(title)