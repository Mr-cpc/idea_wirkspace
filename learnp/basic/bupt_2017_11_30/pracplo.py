import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt

'''
User:waiting
Date:2017-11-30
Time:15:18
'''

df = pd.read_csv("tr.csv")
s = df['Age']
# prt(s)
# s.value_counts().hist()
# s.value_counts().plot(kind = "pie")
df.plot(y='Pclass',kind = "pie")
plt.show()