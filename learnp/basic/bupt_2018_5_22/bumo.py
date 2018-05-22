import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

from basic.bupt_2017_12_04.Property import Property
from basic.bupt_2018_1_11.doubleharm import page_inc
from basic.bupt_2018_1_15.angelzhu import CBG
from basic.bupt_2018_5_22.EquipModel import EquipModel

'''
User:waiting
Date:2018-05-22
Time:9:17
'''
def get_bumo_info():
    ppt = Property(r'..\bupt_2017_11_24\global.properties')
    url = ppt['jianyi_110_bumo_shanzi']
    # url = ppt['bumo_100_shanzi']
    with open('100bumo.txt','w',encoding='utf-8') as f:
        cbg = CBG(url)
        objs = []
        while True:
            json_data = cbg.json_query()
            if json_data['status'] != 1:
                print('请求失败')
                return
            equip_list = json_data['equip_list']
            if len(equip_list) == 0:
                break
            for obj in equip_list:
                equip = EquipModel(obj)
                objs.append(equip)
                # print(equip,file=f)
            cbg.url = page_inc(cbg.url)
        objs.sort(key=lambda obj:obj.zongshang)
        for obj in objs:
            print(obj,file=f)
if __name__ == '__main__':
    get_bumo_info()
    