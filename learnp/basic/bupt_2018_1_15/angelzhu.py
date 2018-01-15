import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from basic.bupt_2017_11_24.ppthelper import PptHelper
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns
from pip._vendor import requests
import re
from basic.bupt_2018_1_11.doubleharm import page_inc

'''
User:waiting
Date:2018-01-15
Time:9:55
'''
class CBG:
    def __init__(self,url:str):
        self.url = url
        headers = {'User-Agent': 'xyqcbg2/2.3.2 CFNetwork/758.5.3 Darwin/15.6.0'}
        cookies={"device_id":"10272229-E368-4457-95B9-427D8EEDA461", "sid":"sN-FxhNkASiyOmcEF0pKaaFgGeitMOQsxE-S9TLW"}
        self.cookies = cookies
        self.headers = headers

    def json_query(self):
        ip_list = []
        proxies = {'http':'http://39.134.161.12:8080','http':'http://211.159.247.232'}
        self.r = requests.get(self.url,self.cookies,verify=False,headers = self.headers)
        if self.r.json()['status'] == 0:
            raise Exception('请求失败')
        return self.r.json()

    def text_query(self):
        self.r = requests.get(self.url,self.cookies)
        return self.r.text


ppt = PptHelper()
def tianshiquery():
    query = CBG(ppt['global_angel_zhu_url'])
    i = 0
    all_roles = []
    qinghua = []
    with open('info.txt','w',encoding='utf-8') as f:
        while True:
            json = query.json_query()
            contents = json[ppt['eq_list']]
            if len(contents) == 0:
                break
            else:
                all_roles.extend(contents)
                query.url = page_inc(query.url)
                i += 1
            # print(i)
        for x in all_roles:
            if has_jinyi(x,'青花',f):
                qinghua.append(x)
            # print(x,file=f)
        qinghua.sort(key=lambda d:float(d['price_desc']))
        print('所有的：{}'.format(len(all_roles)))
        print('青花：{}'.format(len(qinghua)))
        for content in qinghua:
            print('----\nname:{}---\nprice:{}----\nqu:{}'.format(content['equip_name'],content['price_desc'],content['server_name']),file=f)
def has_jinyi(role_overall_info:dict,target:str,f):

    url = sub_ordersn(ppt['role_detail'],role_overall_info[ppt['ordersn']])
    url = sub_serverid(url,role_overall_info['serverid'])
    # print('ordersn:{}'.format(url))
    query = CBG(url)
    try:
        content = query.json_query()
        equ_desc = content['equip']['equip_desc']
        f.write(equ_desc)
        return target in equ_desc
    except Exception:
        return False

def sub_ordersn(url:str,ordersn:str):
    return re.sub(r'(game_ordersn=)(\d+_\d+_\d+)',matchcase(ordersn),url)
def sub_serverid(url:str,serverid:str):
    return re.sub(r'(serverid=)(\d+)',matchcase(serverid),url)
def matchcase(ordersn:str):
    def replace(m):
        return '{}{}'.format(m.group(1),ordersn)
    return replace

tianshiquery()