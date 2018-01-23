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
Date:2018-01-23
Time:10:34
'''
def hourob2(nums:list):
    sub1,sub2 = nums[1:],nums[:-1]
    dp1,dp2 = [0] * len(nums),[0] * len(nums)
    dp1[1],dp2[0] = sub1[0],sub2[0]
    for i in range(2,len(dp1)):
        dp1[i] = max(dp1[i-1],dp1[i-2]+sub1[i-1])
        dp2[i] = max(dp2[i-1],dp2[i-2]+sub2[i-1])
    return max(dp1[-1],dp2[-1])
if __name__ == '__main__':
    print(hourob2([]))
    pass
    