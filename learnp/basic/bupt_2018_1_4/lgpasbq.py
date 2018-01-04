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
Date:2018-01-04
Time:9:07
'''
def lgpasbq(s:str):
    s_rev = s[::-1]
    dp = [[0 for i in range(len(s) + 1)] for j in range(len(s)+ 1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp)):
            dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == s_rev[j-1] else max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

print(lgpasbq(''))