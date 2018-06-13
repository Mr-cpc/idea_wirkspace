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
Time:11:30
'''


def guessnum(n:int) -> int:
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    cost(1,n,dp)
    return dp[1][n]


def cost(_from:int,_to:int,dp:list):
    if _from >= _to:
        return 0
    elif dp[_from][_to] != 0:
        return dp[_from][_to]
    else:
        ans = float('inf')
        for i in range(_from,_to+1):
            ans = min(ans,i + max(cost(_from,i-1,dp),cost(i+1,_to,dp)))
        dp[_from][_to] = ans
        return ans
if __name__ == '__main__':
    guessnum(20)