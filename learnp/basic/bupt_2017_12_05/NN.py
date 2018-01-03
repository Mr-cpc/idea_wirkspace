import math
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
Date:2017-12-05
Time:10:00
'''

'''
one hid layer and one output unit NN
'''
class Unit:
    def __init__(self,W_num,act_f = lambda x : 1 / (1 + math.e ** -x)):
        self.act_f = act_f
        self.w = np.array([0] * (W_num+1))

    def _sum(self,sam:np.ndarray):
        return np.dot(self.w,sam)

    def out(self,sam):
        return self.act_f(self._sum(sam))


class NN:
    def __init__(self,N_in:int,N_hid:int,learn_rate = 0.1):
        self.N_in = N_in
        self.N_hid = N_hid
        self.hid_units = [Unit(N_in) for i in range(N_hid)]
        self.out_unit = Unit(N_hid,lambda x:x)
        self.learn_rate = learn_rate

    def fit(self,sams,targets):
        sams = np.array([[1] + sam for sam in sams])
        targets = np.array(targets)
        while True:
            for i in range(len(sams)):
                # signal forward propagation
                g = np.array([1] + [hid_unit.out(sams[i]) for hid_unit in self.hid_units])
                y_pre = self.out_unit.out(g)
                # calculate the output layer error
                out_err = y_pre - targets[i]

                # error backwward propagation
                self.out_unit.w -= self.learn_rate * out_err * g
                hid_errs = out_err * self.out_unit.w
                for hid_unit in self.hid_units:
                    hid_unit.w -= self.learn_rate * hid_errs *sams
        pass


    def predict(self,sam):
        sam = np.array([1]+sam)
        g = np.array([1]+[hid_unit.out(sam) for hid_unit in self.hid_units])
        return self.out_unit.out(g)

nn = NN(1,2)
print(nn.predict([1]))