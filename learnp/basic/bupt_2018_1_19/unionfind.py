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
Date:2018-01-19
Time:9:55
'''
class UF:
    def __init__(self,eles,is_connected):
        self.count = len(eles)
        self.id = [i for i in range(self.count)]
        self.is_connected = is_connected
        self.eles = eles

    def grouping(self):
        for i in range(len(self.eles)):
            for j in range(i+1,len(self.eles)):
                if self.is_connected(self.eles[i],self.eles[j]):
                    self.union(i,j)
        from collections import defaultdict
        d = defaultdict(list)
        for val in self.id:
            d[val].append(self.eles[val])
        self.groups = d

    def find(self,i):
        return self.id[i]

    def union(self,x,y):
        id_x = self.find(x)
        id_y = self.find(y)
        if id_x == id_y:
            return
        else:
            for i in range(len(self.id)):
                self.id[i] = self.id[x] if self.id[i] == self.id[y] else self.id[i]
            self.count -= 1