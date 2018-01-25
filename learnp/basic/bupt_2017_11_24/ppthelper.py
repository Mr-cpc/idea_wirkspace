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

from basic.bupt_2017_12_04.Property import Property

'''
User:waiting
Date:2018-01-15
Time:10:15
'''

class PptHelper:
    def __init__(self,path = r'G:\idea_wirkspace\learnp\basic\bupt_2017_11_24\global.properties'):
        self.ppt = Property(path)

    def __getitem__(self, item):
        return self.ppt[item]

    def __iter__(self):
        return iter(self.ppt.d)