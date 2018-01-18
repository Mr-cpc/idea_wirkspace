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
        cookies = {"device_id":"10272229-E368-4457-95B9-427D8EEDA461", "sid":"Ieqh_xBURWcRSFIXx_mv80c1cQoj9pY6PZP5U1Ib", "NTES_SESS":"htGIQEPHahQqM5WvOLSUa7WxTZgng2S1mMOeyBLpy8lDBhbjjfx80JKEDDF7FBf4_rqVLnr9t1POyRnauOas06dmfqE9glNk87h7NkpsFU9tdd0lriXv1dTFh7weY5dqYFOdhGvVOpVeLrfc8NH7N7lmzr3Nm4hQAOEcNkNRLlLo4Q84JiG.PP9lY2siR3oyyyCkZvgC95RQ9PrA.7yZm2cIZ", "_ga":"GA1.2.2096250666.1513858580", "_ntes_nnid":"ecaac034c11f75726577b33dbb2c28ae,1514797131942", "_ntes_nuid":"ecaac034c11f75726577b33dbb2c28ae"}
        self.cookies = cookies
        self.headers = headers
    def login(self):
        login_url = ppt['login_url']
        headers = {'Accept':'*/*',
                   'Accept-Encoding':'gzip, deflate',
                   'Accept-Language':'zh-cn',
                   'Connection':'keep-alive',
                   'Content-Type':'application/x-www-form-urlencoded',
                   'Cookie':'device_id=10272229-E368-4457-95B9-427D8EEDA461; sid=rWdiC_1mS4L5dUxGCW0D1HF1UUduM-WociQ1B199',
                   'Host':'xyq-ios2.cbg.163.com',
                   'If-Modified-Since':'0',
                   'Proxy-Connection':'keep-alive',
                   'User-Agent':'xyqcbg2/2.3.2 CFNetwork/758.5.3 Darwin/15.6.0'}
        datas = {'act':'chose_role',
                 'app_version':'2.3.2',
                 'roleid':'28634442',
                 'device_name':'My iPhone',
                 'obj_serverid':'39',
                 'device_token':'<b685f8fb fba4c7fb 40e0c955 b1810053 244493f1 5bf149f5 f6ec0911 1d32a298>',
                 'platform':'ios',
                 'os_version':'9.3.3',
                 'os_name':'iPhone OS',
                 'device_id':'10272229-E368-4457-95B9-427D8EEDA461',
                 'device_type':'2'}
        r = requests.post(login_url,data=datas,headers=headers)
        print(r.json())
    def json_query(self):
        ip_list = []
        proxies = {'http':'http://39.134.161.12:8080'}
        self.r = requests.get(self.url,self.cookies,verify=False,headers = self.headers)
        if self.r.json()['status'] != 1:
            print(self.r.json())
            raise Exception('请求失败')
        return self.r.json()

    def text_query(self):
        self.r = requests.get(self.url,self.cookies)
        return self.r.text


ppt = PptHelper()
def tianshiquery(jinyi:str = ''):
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
            if has_jinyi(x,jinyi,f):
                qinghua.append(x)
            # print(x,file=f)
        qinghua.sort(key=lambda d:float(d['price_desc']))
        print('所有的：{}'.format(len(all_roles)))
        print('{}：{}'.format(jinyi,len(qinghua)))
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

tianshiquery('冰寒')
# cbg = CBG(ppt['global_angel_zhu_url'])
# cbg.login()