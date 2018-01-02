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
Time:15:27
'''
def reachnum(target:int):
    from collections import deque
    q = deque()
    from collections import namedtuple
    Ele = namedtuple('Ele',['val','step'])
    q.append(Ele(0,1))
    while len(q):
        cur = q.popleft()
        if cur.val == target:
            return cur.step - 1
        else:
            q.extend([Ele(cur.val - cur.step,cur.step+1),Ele(cur.val+cur.step,cur.step+1)])


print(reachnum(4))