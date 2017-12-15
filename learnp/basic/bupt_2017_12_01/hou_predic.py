import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelBinarizer, MinMaxScaler, Imputer

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

from basic.bupt_2017_12_01.hou_prepro import find_num_attr, find_text_attr, find_related_num_attr, load_obj
from basic.bupt_2017_12_04.Property import Property

'''
User:waiting
Date:2017-12-13
Time:9:46
'''
ppt = Property(r'G:\idea_wirkspace\learnp\basic\bupt_2017_12_04\global.properties')
ran_fore_reg = joblib.load(ppt['model_path'])
df = pd.read_csv(ppt['te'])
df.pop('Id')
prt(load_obj(ppt['rel_attr_path']))
related_num_df = df[load_obj(ppt['rel_attr_path'])]
scaler = MinMaxScaler()
pipeline = Pipeline([('imputer',Imputer(strategy='median')),('scaler',scaler)])
ans = ran_fore_reg.predict(pipeline.fit_transform(related_num_df))
prt(ans)
with open(ppt['res_path'],'w') as f:
    f.write('Id,SalePrice\n')
    for i in range(len(ans)):
        f.write("{},{}\n".format(1461+i,ans[i]))
