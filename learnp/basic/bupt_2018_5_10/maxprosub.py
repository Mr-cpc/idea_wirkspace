
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
Date:2018-05-10
Time:16:54
'''
def maxprosub(nums:list):
    if len(nums) == 0:
        return 0
    ans = nums[0]
    ma = [0] * len(nums)
    mi = [0] * len(nums)
    ma[0] = mi[0] = nums[0]
    for i in range(1,len(nums)):
        candi = [nums[i],nums[i] * ma[i-1],nums[i] * mi[i-1]]
        ma[i] = max(candi)
        mi[i] = min(candi)
        ans = max(ans,ma[i])
    print(ma)
    print(mi)
    return ans
if __name__ == '__main__':
    print(maxprosub([2,3,-2,4]))
    