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
Time:15:47
'''
def countSubstrings(s:str):
    dp = [[i <= j for i in range(len(s))]for j in range(len(s))]
    ans = len(s)
    for j in range(1,len(s)):
        for i in range(len(s) - j):
            dp[i][j + i] = (s[i] == s[j + i] and dp[i + 1][j - 1 + i])
            if dp[i][j + i]:
                ans += 1
    return ans
print(countSubstrings('aaa'))
if __name__ == '__main__':
    pass
    