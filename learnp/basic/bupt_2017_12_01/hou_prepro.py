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
Date:2017-12-01
Time:9:27
'''
def find_null(rate:float,df:pd.DataFrame) -> list:
    se = df.isnull().sum()
    return [x for x in se.index if se[x] / len(df) >= rate]
df = pd.read_csv("tr.csv")
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
x = df.sort_values(by='GrLivArea',ascending=False)[['GrLivArea']].head(2)
prt(x)