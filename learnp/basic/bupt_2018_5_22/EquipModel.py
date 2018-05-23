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

'''
User:waiting
Date:2018-05-22
Time:9:54
'''
import re
x = r'([\u4e00-\u9fa5]+)( \+)(\d+)'
pattern = re.compile(r'([\u4e00-\u9fa5]+)( \+)(\d+)')
def grasp_shanghai(desp:str) -> str:
    m = re.search(r'(伤害)( \+)(\d+)',desp)
    return m.group(3)


def grasp_mingzhong(desp:str) -> str:
    m = re.search(r'(命中)( \+)(\d+)',desp)
    return m.group(3)
def grasp_duanshu(desp:str) -> str:
    m = re.search(r'(锻炼)(\d+)(级)',desp)
    if not m:
        return 0
    return m.group(2)


def fujiashuxing(desp:str):
    if not desp:
        return ""
    res = []
    for x in pattern.findall(desp):
        res.append('{}:+{}'.format(x[0],x[2]))
    return ','.join(res)

class EquipModel:
    '''
    伤害
    命中
    段数
    区
    价格
    总伤
    附加属性
    收藏人数
    上架时间
    '''
    def __init__(self,obj):
        self.shanghai = grasp_shanghai(obj['desc_sumup_short'])
        self.mingzhong = grasp_mingzhong(obj['desc_sumup_short'])
        self.qu = '{}-{}'.format(obj['area_name'],obj['server_name'])
        self.zongshang = int(self.shanghai) + int(self.mingzhong) / 3
        self.price = obj['price_desc']
        self.duanshu = grasp_duanshu(obj['desc_sumup'])
        self.shouchangshu = obj['collect_num']
        self.shangjiashijian = obj['selling_time']
        fujia = obj.get('agg_added_attrs','')
        self.fujia = fujiashuxing(fujia[0]) if fujia else ""
    def __str__(self):
        return '伤害:{}\n' \
               '命中:{}\n' \
               '段数:{}\n' \
               '总伤:{}\n' \
               '区:{}\n' \
               '价格:{}\n' \
               '双加:{}\n' \
               '收藏数:{}\n' \
               '何时上架:{}\n'.format(self.shanghai,self.mingzhong,self.duanshu,self.zongshang,self.qu,self.price,self.fujia,self.shouchangshu,self.shangjiashijian)
if __name__ == '__main__':
    pass