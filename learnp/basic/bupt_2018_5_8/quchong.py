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
Date:2018-05-08
Time:14:41

'''
from collections import defaultdict
def quchong(s:str) -> str:
    d = defaultdict(int)
    i = 0
    while i < len(s) - 2:
        flag = False
        for j in range(2,len(s)):
            if i + j >= len(s):
                break
            substr = s[i:i+j]
            if substr.isdigit():
                break
            k = 1
            while i + j * k < len(s) and s[i+j*k:].startswith(substr):
                k += 1
                d[(substr,i)] += 1
                flag = True
            if flag:
                i = i + k * j
                break
        if not flag:
            i += 1
    for key in sorted(d.keys(),key=lambda key:-key[1]):
        s = s[:key[1]+len(key[0])] + s[key[1]+(d[key]+1)*len(key[0]):]
    return s
if __name__ == '__main__':
    x = "刚才我说了我要退款我要退款我要退款，我都说了我要退款我要退款我要退款"
    print(quchong(x))
