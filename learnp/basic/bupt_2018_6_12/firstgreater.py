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
Time:9:24
'''
def firstgreaterthan(nums:list) -> list:
    ans = [-1] * len(nums)
    stk = [0]
    for i in range(1,len(nums)):
        while stk and nums[stk[-1]] < nums[i]:
            ans[stk[-1]] = nums[i]
            stk.pop()
        stk.append(i)
    return ans
if __name__ == '__main__':
    nums = [2, 5, 3, 7, 1, 2, 8]
    print(firstgreaterthan(nums))