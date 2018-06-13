from typing import Callable

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
Date:2018-06-13
Time:16:40
'''
# lambda中引用的外部变量是在调用时确定值的
x = 10
a = lambda y:x+y
x = 20
b = lambda y:x +y
# print(a(10))
# print(b(10))

x = 10
a = lambda y,x = x:x + y
x = 20
b = lambda y,x = x:x + y
# print(a(10))
# print(b(10))

# 使用functools的partial包装函数使之更容易使用
def call(a,b,c,d):
    print(a,b,c,d)
from functools import partial
def warpper1(obj,*args,**kwargs) -> Callable:
    return partial(obj,*args,**kwargs)
wrapper_call = warpper1(call,c= 1, d=3)
wrapper_call(2,4)
if __name__ == '__main__':
    pass
    