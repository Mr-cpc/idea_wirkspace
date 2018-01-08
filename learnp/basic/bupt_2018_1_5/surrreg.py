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
Date:2018-01-05
Time:16:30
'''


def bfs(board:list, cur:tuple, visited:set, region:list):
    if 0<=cur[0]<len(board) and 0<= cur[1]<len(board[0]):
        if cur in visited:
            return
        elif board[cur[0]][cur[1]] == 'O':
            visited.add(cur)
            region.append(cur)
            for i in (1,-1):
                bfs(board,(cur[0]+i,cur[1]),visited,region)
                bfs(board,(cur[0],cur[1]+i),visited,region)




def check(board:list,edges):
    print(edges)
    for edge in edges:
        if 0 < edge[0] < len(board)-1 and 0 < edge[1] < len(board[0]) -1:
            continue
        else:
            return False
    else:
        return True
    # for i in (1,-1):
    #     if board[edges.most_left[0]-1][edges.most_left[1]] ==  board[edges.most_left[0]][edges.most_left[1]+i] == 'X':
    #         continue


def surreg(board:list):
    visited = set()
    regions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) in visited:
                continue
            elif board[i][j] == 'X':
                continue
            else:
                region = []
                bfs(board,(i,j),visited,region)
                regions.add(tuple(region))
    for region in regions:
        left_right = sorted(region,key=lambda d:d[1])

        up_down = sorted(region,key=lambda d:d[0])
        from collections import namedtuple
        Edges = namedtuple('Edges',['most_left' ,'most_right','most_up','most_down'])
        edges = Edges(left_right[0], left_right[-1],up_down[0],up_down[-1])
        # most_left ,most_right= left_right[0], left_right[-1]
        # most_up,most_down = up_down[0],up_down[-1]
        if check(board,edges):
            for pos in region:
                board[pos[0]][pos[1]] = 'X'
    print(board)


print(surreg([['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','X'],
        ['X','O','X','X']]))