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
Time:15:29
'''

'''
给定整数m以及n各数字A1,A2,..An，
将数列A中所有元素两两异或，共能
得到n(n-1)/2个结果，请求出这些
结果中大于m的有多少个。
'''

from sys import stdin
n, m= [int(num) for num in stdin.readline().strip().split(" ")]
nums = [int(ele) for ele in stdin.readline().strip().split(" ")]
ans = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] ^ nums[j] > m:
            ans += 1
print(ans)
if __name__ == '__main__':
    pass
    