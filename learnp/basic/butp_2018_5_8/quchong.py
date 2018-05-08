import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

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

def quchong(s:str) -> str:
    d = defaultdict(int)
    for i in range(len(s) -3):
        for j in range(2,len(s)):
            if i + j >= len(s):
                break
            substr = s[i:i+j]
            k = 1
            while i + j * k < len(s) and s[i+j*k:].startswith(substr):
                k += 1
                d[substr] += 1
    for key in d:
        st = s.find(key)
        s = s[:st+len(key)] + s[st+(d[key]+1)*len(key):]
    return s
if __name__ == '__main__':
    print(quchong("abcdabcde"))
