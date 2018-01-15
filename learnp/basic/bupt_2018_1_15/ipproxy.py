from bs4 import BeautifulSoup
from pip._vendor import requests
import random
import re
ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
port_pattern = re.compile(r'<td>\d+</td>')
protocol_pattern = re.compile(r'HTTPS?')

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'html.parser',from_encoding='gbk')
    ips = soup.find_all('tr')
    ip = []
    ports = []
    protocols = []
    urls = []
    for ite in ips:
        ite = str(ite)
        ip = re.findall(ip_pattern,ite)
        port = re.findall(port_pattern,ite)
        protocol = re.findall(protocol_pattern,ite)
        if ip and port and protocol:
            urls.append('{}://{}:{}'.format(protocol[0].lower(),ip[0],port[0][4:-5]))
            protocols.append(protocol[0].lower())
    print(len(urls))
    print(len(protocols))
    ip_dict = {protocols[i]:urls[i] for i in range(len(urls))}
    print(ip_dict)
    return ip_dict

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

url = 'http://www.kxdaili.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
ip_list = get_ip_list(url, headers=headers)