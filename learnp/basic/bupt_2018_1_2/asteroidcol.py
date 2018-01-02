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
Time:17:09
'''
def asteroidcol(asteroids:list):
    from math import fabs
    po = []
    ne = []
    for ast in asteroids:
        po.append(ast) if ast > 0 else ne.append(ast)
    stk = []
    for i in range(len(asteroids)-1,-1,-1):
        if len(stk):
            if (stk[-1] >> 31 & 1) == (asteroids[i] >> 31 & 1):
                stk.append(asteroids[i])
            else:
                if -stk[-1] == asteroids[i]:
                    stk.pop()
                elif fabs(asteroids[i]) > fabs(stk[-1]):
                    stk[-1] = asteroids[i]
                else:
                    pass
        else:
            stk.append(asteroids[i])

    return stk

print(asteroidcol([-2,-1,1,2]))