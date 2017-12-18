import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2017-12-18
Time:9:54
'''

prefix = input('package prefix(like cn.bupt.xxxx):')
prefix = re.sub(r'\.',r'/',prefix)
contents = ['controller/inf','service/impl','component','constants',
           'filter','model','util','listener','interceptor','dao/autogenerate','entity/autogenerate']
configs = ['map/autogenerate']
for content in contents:
    os.makedirs("{}/{}".format(prefix,content),exist_ok=True)
