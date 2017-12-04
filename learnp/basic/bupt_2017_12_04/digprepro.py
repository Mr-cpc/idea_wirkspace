import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from basic.bupt_2017_10_30.deco import time_statistic
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

from basic.bupt_2017_12_04.Property import Property

'''
User:waiting
Date:2017-12-04
Time:14:18
'''
@time_statistic
def save(tr_set:pd.DataFrame,tr_lab:pd.Series,shape:tuple):
    for i in range(len(tr_set)):
        plt.imshow(tr_set.iloc[i].as_matrix().reshape(shape),cmap='gray')
        plt.title(tr_lab[i])
        plt.savefig('{}th.png'.format(i+1))

ppt = Property('global.properties')
df = pd.read_csv(ppt['tr'])
tr_set = df.iloc[:20,1:]
tr_lab = df.iloc[:20,0]
# save(tr_set,tr_lab,(28,28))
# prt(tr_set)


