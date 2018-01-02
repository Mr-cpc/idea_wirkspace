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
Date:2018-01-02
Time:15:53
'''
def dailytemp(temperatures:list):
    ans = [0] * len(temperatures)
    from collections import namedtuple
    stk = []
    Ele = namedtuple('Ele',['val','idx'])
    for i in range(len(temperatures)-1,-1,-1):
        if not len(stk):
            ans[i] = 0
        else:
            while len(stk) and stk[-1].val <= temperatures[i]:
                stk.pop()
            ans[i] = stk[-1].idx - i if len(stk) else 0
        stk.append(Ele(temperatures[i],i))
    return ans

print(dailytemp(temperatures = [73, 74, 75, 71, 69, 72, 76, 73]))