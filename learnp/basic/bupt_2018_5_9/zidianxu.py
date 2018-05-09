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
Date:2018-05-09
Time:14:58
'''
def zidianxu(n:int,m:int) -> int:
    nums = (str(num) for num in range(1,n+1))
    return int(sorted(nums)[m-1])
def zidianxu2(n:int,m:int) -> int:
    nums = list(range(1,n+1))
    low,high = 0,n-1
    while True:
        j = partition(nums,low,high)
        if j == m - 1:
            return nums[j]
        elif j < m - 1:
            low = j +1
        else:
            high = j - 1
def partition(nums,low:int,high:int) -> int:
    x = nums[low]
    while low < high:
        while low < high and str(nums[high]) >= str(x):
            high -= 1
        nums[low] = nums[high]
        while low < high and str(nums[low]) <= str(x):
            low += 1
        nums[high] = nums[low]
    nums[low] = x
    return low
from sys import stdin
# n,m = [int(num) for num in stdin.readline().split(" ")]
# print(zidianxu(n,m))
if __name__ == '__main__':
    print(zidianxu2(11,4))