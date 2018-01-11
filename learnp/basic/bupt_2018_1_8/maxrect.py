from collections import Counter

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

from basic.bupt_2018_1_8.largrectinhist import method_2

'''
User:waiting
Date:2018-01-08
Time:16:35
'''
def maxrect(matrix:list):
    heights = [None] * len(matrix)
    for i in range(len(matrix)):
        heights[i] = [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            heights[i][j] = Counter(matrix[k][j] for k in range(i))[1]
    return max(method_2(height) for height in heights)


print(maxrect([[1,1,1,0,0],
               [1,1,1,0,1],
               [1,1,1,1,1],
               [1,0,0,1,0]]))
