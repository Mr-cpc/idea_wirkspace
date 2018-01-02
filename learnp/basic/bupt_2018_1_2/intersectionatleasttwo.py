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
Date:2018-01-02
Time:14:44
'''
def atleatwo(intervals:list) ->int:
    intervals.sort(key=lambda itv:(itv[1],itv[0]))
    print(intervals)
    ans = 2
    prev_end = intervals[0][-1]
    for i in range(1,len(intervals)):
        if intervals[i][0] == prev_end:
            ans += 1
            prev_end = intervals[i][-1]
        elif intervals[i][0] < prev_end:
            pass
        else:
            ans += 2
            prev_end = intervals[i][-1]
    return ans
print(atleatwo(intervals =  [[8,9],[4,21],[3,19],[5,9],[1,5]]))
# std 4