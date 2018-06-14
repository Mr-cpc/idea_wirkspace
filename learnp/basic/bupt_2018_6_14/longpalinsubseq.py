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
Date:2018-06-14
Time:14:20
'''
def longestpalinsubsequence(s:str):
    if not s:
        return 0
    dp =[[int(i == j) for i in range(len(s))] for j in range(len(s))]
    i,j = 0,1
    while j < len(s):
        for k in range(len(s)-j):
            dp[i+k][j+k] = dp[i+k+1][j+k-1] + 2 if s[i+k] == s[j+k] else max(dp[i+k+1][j+k],dp[i+k][j+k-1])
        j += 1
    return dp[0][-1]

s = 'adghbebja'
print(longestpalinsubsequence(s))
if __name__ == '__main__':
    pass
    