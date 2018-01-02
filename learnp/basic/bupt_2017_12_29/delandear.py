import collections
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


def get_max(group,counter:collections.Counter):
    choose_one ,choose_two = 0, 0
    for i in range(0,len(group),2):
        choose_one += counter[group[i]] * group[i]
    for j in range(1,len(group),2):
        choose_two += counter[group[j]] * group[j]
    return max(choose_one,choose_two)

def delandearn(nums) ->int:
    from collections import Counter
    counter = Counter(nums)
    nums = list(set(nums))
    print("set后的nums：{}".format(nums))
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
    return sum(get_max(group,counter) for group in d.values())
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

nums = [10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5]
print(delandearn(nums))
# std 338