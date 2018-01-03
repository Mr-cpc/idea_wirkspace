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
Date:2018-01-03
Time:14:37
'''
def floodfill(image:list,sr:int,sc:int,newColor:int):
    from collections import deque
    q = deque()
    q.append((sr,sc))
    start_color = image[sr][sc]
    while len(q):
        cur = q.popleft()
        if image[cur[0]][cur[1]] == start_color:
            image[cur[0]][cur[1]] = newColor
            for i in (1,-1):
                if 0 <= cur[0] + i < len(image):
                    q.append((cur[0]+i,cur[1]))
                if 0 <= cur[1] + i < len(image[0]):
                    q.append((cur[0],cur[1]+i))
    return image




print(floodfill(image = [[1,1,1],[1,1,0],[1,0,1]],
sr = 1, sc = 1, newColor = 2))
