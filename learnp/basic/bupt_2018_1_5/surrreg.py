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
Date:2018-01-05
Time:16:30
'''
def surreg(board:list):
    s = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) in s:
                continue
            elif board[i][j] == 'X':
                continue
            else:
                pass