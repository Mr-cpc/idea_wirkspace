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
Time:14:50
'''
def longvalidpalin(s:str):
    dp = [0] * len(s)
    ans = 0
    for i in range(1,len(s)):
        if s[i] ==')':
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            elif i - 1 - dp[i-1] >= 0 and s[i - 1 - dp[i-1]] == '(':
                dp[i] = dp[i-1] + 2 + dp[i- dp[i-1] -2]
            ans = max(ans,dp[i])
    return ans
if __name__ == '__main__':
    print(longvalidpalin("(()"))