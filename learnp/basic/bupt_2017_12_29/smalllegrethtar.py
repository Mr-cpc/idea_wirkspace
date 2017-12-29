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
Time:16:40
'''
def smalegrethta(letters:list,target:str) -> str:
    letters.sort()
    for i,ch in enumerate(letters):
        if ch <= target:
            continue
        else:
            return ch
    else:
        return letters[0]

print(smalegrethta(letters = ["c", "f", "j"],
target = "c"))