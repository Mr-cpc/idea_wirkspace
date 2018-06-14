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
Date:2018-06-14
Time:10:37
'''


def can_split(nums:list, mid:int, m:int):
    cur_sum = 0
    cur_seg = 1
    for num in nums:
        cur_sum += num
        if cur_sum > mid:
            cur_sum = num
            cur_seg += 1
        if cur_seg > m:
            return False
    return True

def splitarr(nums:list,m:int):
    l,r = 0,0
    for num in nums:
        r += num
        l = max(l,num)
    while l <= r:
        mid = l + ((r - l) >> 1)
        if can_split(nums,mid,m):
            r = mid - 1
        else:
            l = mid + 1
    return l
nums = [7,2,5,10,8]
print(can_split(nums,12,3))
print(splitarr(nums,2))
if __name__ == '__main__':
    pass
    