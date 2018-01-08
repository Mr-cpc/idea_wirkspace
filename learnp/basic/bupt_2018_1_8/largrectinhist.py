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
Time:16:22
'''
def largrectinhist(heights:list):
    ans = 0
    for i in range(len(heights)):
        for j in range(i+1,len(heights)+1):
            ans = max(ans,min(heights[i:j]) * (j-i))
    return ans
def method_2(heights:list):
    stk = []
    ans = 0
    for i in range(len(heights)):
        if len(stk):
            if heights[i] >= heights[stk[-1]]:
                stk.append(i)
            else:
                ans = max(ans,len(stk) * stk[0])
                stk = [i]
        else:
            stk.append(i)
    return ans
print(method_2([2,1,5,6,2,3]))
