import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Iterable

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2017-12-06
Time:15:58
'''
#use yield from
def flat_list(items:Iterable):
    for item in items:
        if isinstance(item,Iterable) and not isinstance(item,str):
            yield from flat_list(item)
        else:
            yield item
# use for loop
# def flat_list2(item:Iterable):
#     for item in items:
#         if isinstance(item,Iterable) and not isinstance(item,str):
#             for i in flat_list2(item):
#                 yield i
#         else:
#             yield item
def gen(n):
    for x in (i for i in range(n)):
        yield x

items = [2,[1,2],3,[[1],[2]],4,"aa"]
g = gen(5)
for x in iter(lambda :next(g),2):
    print(x)