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
Time:15:27
'''
def atleasttwice(nums:list) -> int:
    if len(nums) == 1:
        return -1
    max_num,sec_num,max_num_idx = (nums[0],nums[1],0) if nums[0] > nums[1] else (nums[1],nums[0],1)
    for i,num in enumerate(nums,2):
        if num > max_num:
            sec_num,max_num,max_num_idx = max_num,num,i
        elif num >= sec_num:
            sec_num = num
        else:
            pass
    return max_num_idx if max_num >= (sec_num << 1) else -1

print(atleasttwice(nums = [1,2,3,4]))
