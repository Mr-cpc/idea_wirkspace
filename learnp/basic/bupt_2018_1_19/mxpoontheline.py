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

from basic.bupt_2018_1_19.unionfind import UF

'''
User:waiting
Date:2018-01-19
Time:9:45
'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def mxpotontheline(points:list):
    uf_x = UF(points,lambda p1,p2:p1.x == p2.x)
    uf_y = UF(points,lambda p1,p2:p1.y == p2.y)

    uf_x.grouping()
    ans = 0
    for k,v in uf_x.groups.items():
        ans = max(ans,len(v))
    uf_y.grouping()
    for k,v in uf_y.groups.items():
        ans = max(ans,len(v))
    return ans
def cal_slope(p1,p2):
    return Decimal(p1.y -p2.y) / Decimal(p1.x - p2.x) if p1.x != p2.x else float('inf')
def mxpotontheline2(points:list):
    if len(points) < 1:
        return 0
    if len(points) == 2:
        return 2
    ans = 1
    from collections import defaultdict
    for i in range(len(points)):
        d = defaultdict(int)
        same = 0
        for j in range(i+1,len(points)):
            if points[i].x == points[j].x and points[i].y == points[j].y:
                same += 1
            else:
                d[cal_slope(points[i],points[j])] += 1
        if not d:
            d[float('inf')] = 0
        for key in d:
            d[key] += same
        print(d)
        ans = max(ans,max(d.values())+1) if d else ans

    return ans
if __name__ == '__main':
    from decimal import Decimal
    d = defaultdict(int)
    print(mxpotontheline2([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)]))
    x = Decimal(94911150) /Decimal(94911151)
    y = Decimal(949111500) /Decimal(949111510)