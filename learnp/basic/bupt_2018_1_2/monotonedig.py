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
Date:2018-01-02
Time:16:24
'''
def monodig(N:int) -> int:
    N = list(str(N))
    for i in range(len(N)-1,0,-1):
        if int(N[i]) >= int(N[i-1]):
            continue
        else:
            for j in range(i,len(N)):
                N[j] = '9'
            if int(N[i-1]) >= 1:
                N[i-1] = str(int(N[i-1])-1)
            else:
                N[i-1] = '9'
                j = i - 2
                while j >= 0 and int(N[j]) < 1:
                    N[j] = '9'
                    j -= 1
                if j >= 0:
                    N[j] = str(int(N[j])-1)
                else:
                    return int("".join(N[1:]))
    return int("".join(N))

print(monodig(1032))