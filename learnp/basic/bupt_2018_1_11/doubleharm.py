from datetime import datetime

from pip._vendor import requests as req

from basic.bupt_2017_11_24.ppthelper import PptHelper
from basic.bupt_2017_12_04.Property import Property
from collections import Counter
import re
import threading
import time
ppt = PptHelper()
# ([a-zA-Z0-9%_.\-]*)
shijie_url = ppt['shijie_double_harm_url']

cookies = {"device_id":"10272229-E368-4457-95B9-427D8EEDA461", "sid":"Ieqh_xBURWcRSFIXx_mv80c1cQoj9pY6PZP5U1Ib", "NTES_SESS":"htGIQEPHahQqM5WvOLSUa7WxTZgng2S1mMOeyBLpy8lDBhbjjfx80JKEDDF7FBf4_rqVLnr9t1POyRnauOas06dmfqE9glNk87h7NkpsFU9tdd0lriXv1dTFh7weY5dqYFOdhGvVOpVeLrfc8NH7N7lmzr3Nm4hQAOEcNkNRLlLo4Q84JiG.PP9lY2siR3oyyyCkZvgC95RQ9PrA.7yZm2cIZ", "_ga":"GA1.2.2096250666.1513858580", "_ntes_nnid":"ecaac034c11f75726577b33dbb2c28ae,1514797131942", "_ntes_nuid":"ecaac034c11f75726577b33dbb2c28ae"}
def query(url:str,path:str):
    with open(path,'w',encoding='utf-8') as f:
        i = 1
        j = 1
        res = []
        while True:
            r = req.get(url,verify=False,cookies = cookies)
            contents = r.json()[ppt['eq_list']]
            if len(contents) > 0:
                pattern = re.compile('^{}'.format(ppt['harm']))

                print('第{}页，{}个'.format(i,len(contents)))
                # print(contents[0],file=f)
                # print('---------page{}'.format(i),file=f)
                for content in contents:
                    a = pattern.match(content[ppt['main_attr']])
                    b= Counter(content[ppt['down']][0].split(' '))[ppt['harm']] >= 2
                    if a and b:
                        res.append(content)
                        # print('----\nname:{}---\nprice:{}----\nmain:{}-----\ndown:{}----\nqu:{}'.format(content['equip_name'],content['price_desc'],content[ppt['main_attr']],content[ppt['down']],content['server_name']),file=f)
                        # print(j,file=f)
                        # j+=1
                url = re.sub(r'(page=)(\d+)',matchcase(),url)
                i += 1
            else:break
        res.sort(key=lambda d:(float(d['price_desc']),d['server_name']))
        for idx,content in enumerate(res):
            print('----\nname:{}---\nprice:{}----\nmain:{}-----\ndown:{}----\nqu:{}'.format(content['equip_name'],content['price_desc'],content[ppt['main_attr']],content[ppt['down']],content['server_name']),file=f)
            print(idx+1,file=f)
def page_inc(url):
    return re.sub(r'(page=)(\d+)',matchcase(),url)
def matchcase():
    def replace(m):
        return '{}{}'.format(m.group(1),int(m.group(2))+1)
    return replace
if __name__ == '__main__':
    while True:
        num = query(ppt['global_double_harm_7_url'],'jinglian7.txt')
        time.sleep(100)