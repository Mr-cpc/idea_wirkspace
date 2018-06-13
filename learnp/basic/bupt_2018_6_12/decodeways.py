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
Date:2018-06-12
Time:16:10
'''
def deway(s:str):
    dp = [0] * len(s)
    if not s:
        return 0
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    dp[0] = 1
    if (s[0] == '1' and s[1] != '0') or (s[0] == '2' and '1' <= s[1] <= '6'):
        dp[1] = 2
    else:
        if s[0] > '2' and s[1] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
    for i in range(2,len(s)):
        if s[i] == '0':
            if '0' < s[i-1] <= '2':
                dp[i] = dp[i-2]
            else:
                dp[i] = 0
        else:
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6') :
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
    return dp[-1]
if __name__ == '__main__':
    print(deway("20"))
    