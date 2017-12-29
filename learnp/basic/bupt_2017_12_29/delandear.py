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
Date:2017-12-29
Time:17:01
'''


def get_max(group):
    if (len(group) & 1) == 1:
        return sum(group[::2])
    else:
        return sum()


def delandearn(nums:list) ->int:
    uf = UF(nums)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[j] - nums[i]) in (1,-1):
                uf.union(i,j)
    print('finally {} groups'.format(uf.count))
    from collections import defaultdict
    d = defaultdict(list)
    for i,value in enumerate(uf.id):
        d[value].append(nums[i])
    print(d)
    return sum(get_max(group) for group in d.values())
class UF:
    def __init__(self,nums):
        self.count = len(nums)
        self.id = [i for i in range(self.count)]

    def find(self,i):
        return self.id[i]

    def union(self,x,y):
        id_x = self.find(x)
        id_y = self.find(y)
        if id_x == id_y:
            return
        else:
            self.id[y] = self.id[x]
            self.count -= 1

nums = [1,2,4,5,7,8,9,11,12]
delandearn(nums)