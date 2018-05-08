import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2018-05-08
Time:10:49
'''

def radix_sort(nums:list):
    d = defaultdict(list)
    round = len(str(max(nums)))
    for i in range(round):
        print(nums)
        for j in nums:
            d[(j//(10 ** i)) % 10].append(j)
        nums.clear()
        for k in range(10):
            nums.extend(d[k])
        d.clear()
if __name__ == '__main__':
    nums = [278  ,   109   , 63  , 930   ,589   ,184   ,505   , 269  , 8   , 83]
    radix_sort(nums)
    print(nums)
    