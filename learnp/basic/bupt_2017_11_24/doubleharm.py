from datetime import datetime

from pip._vendor import requests as req

from basic.bupt_2017_12_04.Property import Property
from collections import Counter
import re
import threading
import time
ppt = Property('global.properties')

# url = "http://xyq-ios2.cbg.163.com/app2-cgi-bin//xyq_search.py?orderby=selling_time%20DESC&act=super_query&search_type=overall_lingshi_search&equip_level_min=80&equip_level_max=100&kindid=61&damage=1&added_attr_logic=and&added_attr=2&added_attr_repeat_num=2&serverid=39&page=1&platform=ios&app_version=2.3.2&device_name=My%20iPhone&os_name=iPhone%20OS&os_version=9.3.3&device_id=10272229-E368-4457-95B9-427D8EEDA461"
url = 'http://xyq-ios2.cbg.163.com/app2-cgi-bin//xyq_search.py?orderby=selling_time%20DESC&act=super_query&search_type=overall_lingshi_search&equip_level_min=80&equip_level_max=100&kindid=61&damage=1&added_attr_logic=and&added_attr=2&added_attr_repeat_num=2&server_type=3&page=8&platform=ios&app_version=2.3.2&device_name=My%20iPhone&os_name=iPhone%20OS&os_version=9.3.3&device_id=10272229-E368-4457-95B9-427D8EEDA461'
cookies = {"device_id":"10272229-E368-4457-95B9-427D8EEDA461", "sid":"Ieqh_xBURWcRSFIXx_mv80c1cQoj9pY6PZP5U1Ib", "NTES_SESS":"htGIQEPHahQqM5WvOLSUa7WxTZgng2S1mMOeyBLpy8lDBhbjjfx80JKEDDF7FBf4_rqVLnr9t1POyRnauOas06dmfqE9glNk87h7NkpsFU9tdd0lriXv1dTFh7weY5dqYFOdhGvVOpVeLrfc8NH7N7lmzr3Nm4hQAOEcNkNRLlLo4Q84JiG.PP9lY2siR3oyyyCkZvgC95RQ9PrA.7yZm2cIZ", "_ga":"GA1.2.2096250666.1513858580", "_ntes_nnid":"ecaac034c11f75726577b33dbb2c28ae,1514797131942", "_ntes_nuid":"ecaac034c11f75726577b33dbb2c28ae"}
ppt = Property('global.properties')
def query():
    r = req.get(url,verify=False,cookies = cookies)
    contents = r.json()[ppt['eq_list']]
    pattern = re.compile('^{}'.format(ppt['harm']))
    with open('src.info','w',encoding='utf-8') as f:
        print(len(contents))
        print(contents[0],file=f)
        for content in contents:
            a = pattern.match(content[ppt['main_attr']])
            b= Counter(content[ppt['down']][0].split(' '))[ppt['harm']] >= 2
            if a and b:
                print('----\nname:{}---\nprice:{}----\nmain:{}-----\ndown:{}----\nqu:{}'.format(content['equip_name'],content['price_desc'],content[ppt['main_attr']],content[ppt['down']],content['server_name']),file=f)
def printtime():
    print(datetime.now())
def timer_task():
    timer = threading.Timer(1,printtime)
    timer.start()

while True:

    query()
    time.sleep(100)