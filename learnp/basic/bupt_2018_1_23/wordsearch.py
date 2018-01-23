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
Date:2018-01-23
Time:9:42
'''


def dfs(board:list, pos:tuple,word:str,s:set):
    if not word:
        return True
    elif pos in s:
        return False
    elif not ((0 <= pos[1] < len(board[0])) and (0 <= pos[0] < len(board))):
        return False
    elif word[0] != board[pos[0]][pos[1]]:
        return False
    else:
        for i in (-1,1):
            if dfs(board,(pos[0],pos[1]+i),word[1:],{*s,pos}):
                return True
            if dfs(board,(pos[0]+i,pos[1]),word[1:],{*s,pos}):
                return True
        return False
def contain(board:list, word:str):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board,(i,j),word,set()):
                return True
    return False


def wdsearch(board:list,words:list):
    return [word for word in set(words) if contain(board,word)]
if __name__ == '__main__':
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    board = [['a']]
    # print(bool(board))

    words = ["a",'a']
    # words = []
    print(wdsearch(board,words))

    