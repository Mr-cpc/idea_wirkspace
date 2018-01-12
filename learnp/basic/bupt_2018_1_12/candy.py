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
Date:2018-01-12
Time:9:42
'''
def candy(ratings:list):
    candies = [1] * len(ratings)
    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(len(ratings) - 2,-1,-1):
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
    print(candies)
    return sum(candies)
def partition(nums:list,idx:int) -> int:
    nums[0],nums[idx] = nums[idx],nums[0]
    x = nums[0]
    l,h = 0,len(nums) - 1
    while l < h:
        while l < h and nums[h] >= x:
            h -= 1
        nums[l] = nums[h]
        while l < h and nums[l] <= x:
            l += 1
        nums[h] = nums[l]
    nums[l] = x
    return l

print(candy([8,5]))