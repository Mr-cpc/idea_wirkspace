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
Date:2018-06-13
Time:9:46
'''
def maxEnvelopes(envelopes:list):
    if not envelopes:
        return 0
    envelopes.sort(key = lambda x:x[0])
    dp = [1] * len(envelopes)
    ans = 1
    for i in range(1,len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                dp[i] = max(dp[i],dp[j] + 1)
        ans = max(ans,dp[i])
    return ans
if __name__ == '__main__':
    print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
    