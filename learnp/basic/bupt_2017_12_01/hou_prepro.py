import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer, MinMaxScaler, Imputer
from sklearn.tree import DecisionTreeRegressor

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2017-12-01
Time:9:27
'''


def find_null(rate:float,df:pd.DataFrame) -> list:
    se = df.isnull().sum()
    return [x for x in se.index if se[x] / len(df) >= rate]

def find_not_null(rate:float,df:pd.DataFrame) -> list:
    se = df.notnull().sum()
    return [x for x in se.index if se[x] / len(df) >= rate]


def find_num_attr(df:pd.DataFrame) -> list:
    return list(df.dtypes[(df.dtypes == 'int64') | (df.dtypes == 'float64')].index.values)


def find_related_num_attr(rate:float,df:pd.DataFrame,target_attr:str) -> list:
    num_attr = find_num_attr(df)
    corr = df[num_attr].corr()[target_attr].sort_values(ascending=False)
    return list(corr.index[np.abs(corr.values) >= rate])

def find_text_attr(df:pd.DataFrame) -> list:
    return list(df.dtypes[df.dtypes == 'object'].index.values)

def save_obj(path:str,obj:object):
    with open(path,'wb') as f:
        pickle.dump(obj,f)

def load_obj(path:str):
    with open(path,'rb') as f:
        obj = pickle.load(f)
    return obj
df = pd.read_csv("tr.csv")
df.pop('Id')
num_attr = find_num_attr(df)
num_df = df[num_attr]
text_attr = find_text_attr(df)
text_df = df[text_attr]
# label_encoder = LabelEncoder()
# msz_label_encoded = label_encoder.fit_transform(text_df['MSZoning']).reshape(-1,1)
# oh_enc = OneHotEncoder()
# msz_oh_encoder =  oh_enc.fit_transform(msz_label_encoded)
# prt(msz_oh_encoder.toarray())
# label_binarizer = LabelBinarizer(sparse_output=False)
# msz_label_bin = label_binarizer.fit_transform(text_df['MSZoning'])
# prt(msz_label_bin)
# related_num_attr = find_related_num_attr(0.5,df,'SalePrice')
# related_num_df = num_df[related_num_attr]
not_null_num_attr = find_not_null(0.7,num_df)
not_null_num_df = num_df[not_null_num_attr]
scaler = MinMaxScaler()
labels = not_null_num_df['SalePrice']
pipeline = Pipeline([('imputer',Imputer(strategy='median')),('scaler',scaler)])
not_null_num_df.pop('SalePrice')
save_obj('relate_attr.pkl',list(not_null_num_df.columns.values))
X = pipeline.fit_transform(not_null_num_df)
# lin_reg = LinearRegression()
# lin_reg.fit(X,labels.values)
dec_tre_reg = DecisionTreeRegressor()
ran_fore_reg = RandomForestRegressor()
scores = cross_val_score(ran_fore_reg,X,labels,cv=10,scoring="neg_mean_squared_error")
prt(scores)
prt(scores.mean())
ran_fore_reg.fit(X,labels)
# dec_tre_reg.fit(X,labels.values)
joblib.dump(ran_fore_reg,'reg.m')

# prt(related_num_df.values)
# prt(related_num_attr)
# prt(related_num_df)
# df.info()
# print(df['YearBuilt'].value_counts())
# print(df['YearBuilt'].value_counts())
# x = df.dtypes[df.dtypes == 'object'].index
# -----------------------------------------------
#SalePrice的hist
# sns.distplot(df['SalePrice'])
# -----------------------------------------------
#SalePrice and GrLivArea's scatter
# x = pd.concat([df['SalePrice'],df['GrLivArea']],axis=1)
# x.plot.scatter(x='GrLivArea',y='SalePrice')
# ------------------------------------------------
# SalePrice and OverallQual's box
# x = pd.concat([df['SalePrice'],df['OverallQual']],axis=1)
# sns.boxplot(x = 'OverallQual',y = 'SalePrice',data=x)
# ------------------------------------------------
# SalePrice and YearBuilt's box
# x = pd.concat([df['SalePrice'],df['YearBuilt']],axis=1)
# sns.boxplot(x = 'YearBuilt',y = 'SalePrice',data=df.loc[:,['SalePrice','YearBuilt']])
# x = df.corr()
# prt(x)
# sns.heatmap(x)
# se = df.isnull().sum()/df.isnull().count()
# drops = [x for x in se.index if se[x] >= 0.15]
# sns.boxplot(x = 'MiscFeature',y = 'SalePrice',data=df[['MiscFeature','SalePrice']])
# plt.show()
# x = df.sort_values(by='GrLivArea',ascending=False)[['GrLivArea']].head(2)
# prt(x)