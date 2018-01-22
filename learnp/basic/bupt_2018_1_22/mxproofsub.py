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
Date:2018-01-22
Time:15:22
'''
def maxproifsub(nums:list):
    if not nums:
        return 0
    prev_max = nums[0]
    prev_min = None
    cur_max = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > 0 :
            cur_max = max(prev_max * nums[i],cur_max)
            prev_max = cur_max
            prev_min = prev_min * nums[i] if prev_min is not None else None
        elif nums[i] < 0:
            if prev_min is None:
                prev_min = nums[i] * prev_max
                prev_max = 1
            else:
                cur_max = max(prev_min * nums[i],cur_max)
                prev_max = cur_max
        else:
            prev_max,prev_min = 1,None
        print('i:{},curmax:{},min:{},max:{}'.format(i,cur_max,prev_min,prev_max))
    return cur_max
if __name__ == '__main__':
    l1 = [2,3,-2,4,-2]
    l2 = []
    a = maxproifsub([1,-2,3,-4,2])
    print(a)
    pass