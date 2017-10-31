from bs4 import BeautifulSoup
from pip._vendor import requests

response = requests.get(open("url.txt").readline())
response.encoding = "gbk"
print(response.content)
print(response.text)