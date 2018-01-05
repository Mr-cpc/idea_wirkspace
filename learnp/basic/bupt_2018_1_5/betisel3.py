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
Date:2018-01-05
Time:14:48
'''
def bestitose1(prices:list):
    ans,low = 0,prices[0]
    for i in range(1,len(prices)):
        dif = prices[i] - low
        if dif < 0:
            low = prices[i]
        else:
            ans = max(ans,dif)
    return ans


def bestitose(prices:list):
    ans = bestitose1(prices)
    for i in range(1,len(prices)):
        ans = max(ans,bestitose1(prices[:i]) + bestitose1(prices[i:]))
    return ans
print(bestitose([7,6,4,3,1]))
