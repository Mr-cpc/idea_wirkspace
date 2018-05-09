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
Time:17:26
'''
from sys import stdin
from functools import cmp_to_key
while True:
    try:
        n = int(stdin.readline().strip())
        nums = [ele for ele in stdin.readline().strip().split(" ")]
        nums.sort(key=cmp_to_key(lambda x,y:int(y+x)-int(x+y)))
        print("".join(nums))
    except:
        break
if __name__ == '__main__':
    pass
    