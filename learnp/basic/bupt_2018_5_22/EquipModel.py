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
class EquipModel:
    '''
    伤害
    命中
    段数
    区
    价格
    总伤
    '''
    def __init__(self,obj):
        self.shanghai = grasp_shanghai(obj['desc_sumup_short'])
        self.mingzhong = grasp_mingzhong(obj['desc_sumup_short'])
        self.qu = '{}-{}'.format(obj['area_name'],obj['server_name'])
        self.zongshang = int(self.shanghai) + int(self.mingzhong) / 3
        self.price = obj['price_desc']
        self.duanshu = grasp_duanshu(obj['desc_sumup'])
    def __str__(self):
        return '伤害:{}\n' \
               '命中:{}\n' \
               '段数:{}\n' \
               '总伤:{}\n' \
               '区:{}\n' \
               '价格:{}\n'.format(self.shanghai,self.mingzhong,self.duanshu,self.zongshang,self.qu,self.price)
if __name__ == '__main__':
    pass