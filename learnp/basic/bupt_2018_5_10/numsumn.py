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
Date:2018-05-10
Time:9:11
'''
def comb(nums:list,target:int) :
    all_subset_num = 1 << len(nums)
    ans = 0
    for i in range(all_subset_num):
        sum = 0
        for j in range(len(nums)):
            if ((i >> j) & 0x1) == 1:
                sum += nums[j]
            if sum > target:
                break
        if sum == target:
            ans += 1
    return ans
def comb2(nums:list,target:int) :
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(target ,num - 1,-1):
            dp[i] = dp[i] + dp[i - num]
    return dp[target]
from sys import stdin
n,target = [int(ele) for ele in stdin.readline().strip().split(' ')]
nums = [int(ele) for ele in stdin.readline().strip().split(' ')]
print(comb2(nums,target))
if __name__ == '__main__':

    pass
    