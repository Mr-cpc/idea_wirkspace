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

from basic.bupt_2018_1_15.angelzhu import sub_serverid

'''
User:waiting
Date:2018-01-17
Time:10:07
'''
def genserveridpro():
    with open(r'G:\idea_wirkspace\learnp\basic\bupt_2018_1_16\serverid.txt',encoding='utf-8') as f:
        d = {x[1:-2].split(',')[2]:x[1:-2].split(',')[0] for x in f}
    with open('serverid.properties','w',encoding='utf-8') as f:
        for k,v in d.items():
            print('{}={}'.format(k[2:-1],v),file=f)

# genserveridpro()
def query(serv_name:str):
    ppt = PptHelper()
    ppt_servid = PptHelper('serverid.properties')
    try:
        serv_id =ppt_servid[serv_name]
    except KeyError:
        print('no this server')
        return
    url = sub_serverid(ppt['shijie_double_harm_url'],serv_id)
    import basic.bupt_2018_1_11.doubleharm
    basic.bupt_2018_1_11.doubleharm.query(url,'{}.txt'.format(serv_name))

query('a')

