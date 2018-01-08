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
Date:2018-01-08
Time:11:18
'''
def jumpga2(nums:list):
    max_reach = [0] * len(nums)
    for i in range(len(max_reach)):
        max_reach[i] = nums[i] + i
    dp = [float('inf')] * len(nums)
    dp[0] = 0
    for i in range(1,len(dp)):
        for j in range(0,i):
            dp[i] = min(dp[j]+1,dp[i]) if max_reach[j] >= i else dp[i]
    return dp[-1]


print(jumpga2([2,3,1,1,4]))

