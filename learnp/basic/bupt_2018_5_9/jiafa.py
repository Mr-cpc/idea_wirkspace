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
Time:16:49
'''
from sys import stdin
a,b = [ele for ele in stdin.readline().strip().split(" ")]
print(a.isdigit())
print(b.isdigit())
if a.isdigit() and b.isdigit():
    print(int(a) + int(b))
else:
    print('Error')
if __name__ == '__main__':
    pass
    