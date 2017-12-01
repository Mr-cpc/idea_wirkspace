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
Date:2017-12-01
Time:9:07
'''

a = np.arange(9).reshape(3,3)
print(a)
a = a[:,0][:,np.newaxis]
print(a)
prt(a.shape)