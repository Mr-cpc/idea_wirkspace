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
Date:2018-05-09
Time:17:14
'''
from sys import stdin
x,y = [int(ele) for ele in stdin.readline().strip().split(" ")]
dp = [[0 for i in range(y+1)] for j in range(x+1)]
dp[0] = [1] * (y+1)
for i in range(x+1):
    dp[i][0] = 1
for i in range(1,x+1):
    for j in range(1,y+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[x][y])
if __name__ == '__main__':
    pass
    