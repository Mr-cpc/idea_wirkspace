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
Date:2018-05-08
Time:11:00
'''

def sa(s:str) ->list:
    suffixs = [s[i:] for i in range(len(s))]
    suffixs.sort()
    return suffixs
if __name__ == '__main__':
    ss = "aabaaaab"
    for s in sa(ss):
        print(s)
    