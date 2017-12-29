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
Date:2017-12-29
Time:15:57
'''

def mincostclista(cost:list) -> int:
    dp = [0] * (len(cost) + 1)
    for i in range(2,len(dp)):
        dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[-1]
print(mincostclista(cost = [1, 100]))