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
Date:2018-01-08
Time:14:19
'''

class Interval:
    def __init__(self,s = 0,e = 0):
        self.start = s
        self.end = e
    def __str__(self):
        return '[{},{}]'.format(self.start,self.end)
def insitv(intervals:list,newInterval:list):
    # if newInterval[-1] < intervals[0][0]:
    #     return [newInterval,*intervals]
    # elif newInterval[-1] == intervals[0][0]:
    #     return [[newInterval[0],intervals[0][-1]],*intervals[1:]]
    # elif newInterval[0] > intervals[-1][-1]:
    #     intervals.append(newInterval)
    #     return intervals
    # elif newInterval[0] == intervals[-1][-1]:
    #     intervals[-1][-1] = newInterval[-1]
    #     return intervals
    # else:
    #     for i in range(1,len(intervals)):

    intervals.append(newInterval)
    for i in range(len(intervals)-1,0,-1):
        if intervals[i].start < intervals[i-1].start:
            intervals[i],intervals[i-1] = intervals[i-1],intervals[i]
        else:
            break
    print(intervals)
    ans = [intervals[0]]
    prev = intervals[0]
    for i in range(1,len(intervals)):
        if intervals[i].start > prev.end:
            ans.append(intervals[i])
            prev = intervals[i]
        elif intervals[i].end > prev.end:
            ans[-1] = Interval(prev.start,intervals[i].end)
            prev = ans[-1]
        else:
            continue
    return ans
def merge(itv1:list,itv2:list):
    s = set()
    if itv1[-1] < itv2[0]:
        s.add(tuple(itv1))
        s.add(tuple(itv2))
        return s
    elif itv1[-1] == itv2[0]:
        s.add((itv1[0],itv2[-1]))
        return s
    elif itv1[-1] <= itv2[-1] :
        s.add((itv1[0],itv2[-1]))
        return s
    else:
        s.add(tuple(itv1))
        return s
for x in insitv([Interval(1,3),Interval(6,9)],Interval(2,5)):
    print(x)
# print(merge((1,5),(6,9)))




















