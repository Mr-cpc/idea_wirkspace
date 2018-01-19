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
Date:2018-01-19
Time:11:07
'''
def mxgap(nums:list):
    if len(nums) < 2:
        return 0
    bucket = [0] * (max(nums) + 1)
    for val in nums:
        bucket[val] += 1
    sorted_form = []
    for key,val in enumerate(bucket):
        if val != 0:
            sorted_form.extend([key]*val)
    ans = 0
    for i in range(len(nums)-1):
        ans = max(ans,sorted_form[i+1]-nums[i] if sorted_form[i+1] >= nums[i] else nums[i] - sorted_form[i+1])
    return ans