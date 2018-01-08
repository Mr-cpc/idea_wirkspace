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
Date:2018-01-08
Time:15:58
'''
def isn(s:str):
    import re
    s = re.sub(r'\s+','',s)
    if s.isdigit():
        return True
    elif all(x.isdigit for x in s.split('.')):
        return True
    elif all(x.isdigit for x in s.split('e')):
        return True
    else:
        return False

print(all(x.isdigit for x in '1.5'.split('.')))