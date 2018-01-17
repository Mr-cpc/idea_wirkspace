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

from basic.bupt_2018_1_11.doubleharm import page_inc
from basic.bupt_2018_1_15.angelzhu import CBG

'''
User:waiting
Date:2018-01-16
Time:16:48
'''
def get_serverid():
    ppt = PptHelper()
    query = CBG(ppt['global_all'])
    # query.login()
    serverids = set()
    i = 0
    while True:
        cur_len = len(serverids)
        res = query.json_query()[ppt['eq_list']]
        for x in res:
            serverids.add((x[ppt['serv_id']],x[ppt['daqu']],x[ppt['qu']]))
        query.url = page_inc(query.url)
        # if len(serverids) == cur_len:
        #     break
        i += 1
        if len(serverids) > 400 or i > 400:
            break
    return serverids

def exec():
    with open('qu.txt','w',encoding='utf-8') as f:
        serverids = sorted(list(get_serverid()),key=lambda d:(d[1],d[2]))
        for x in serverids:
            print(x,file=f)

# exec()
