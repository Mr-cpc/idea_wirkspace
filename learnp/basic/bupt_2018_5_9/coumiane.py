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

'''
User:waiting
Date:2018-05-09
Time:15:54
'''
def comb(coins:list,deno:int) -> int:
    ans = set()
    comb0(coins,deno,defaultdict(int),ans)
    return len(ans)
def coin_change(coins:list,deno:int) -> int:
    dp = [0] * (deno+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1,deno+1):
            dp[i] = dp[i] + dp[i - coin] if i >= coin else dp[i]
    return dp[deno]
def comb0(coins:list,deno:int,cur:defaultdict,ans:set):
    if deno < 0:
        return
    elif deno == 0:
        ans.add(tuple((key,val) for key,val in cur.items()))
    else:
        for coin in coins:
            cur[coin] += 1
            comb0(coins,deno - coin,cur,ans)
            cur[coin] -= 1
from sys import stdin

deno = int(stdin.readline())
print(coin_change([3,5,10,20,50,100],deno))
# print(comb([1,5,10,20,50,100],deno))
if __name__ == '__main__':
    # print(comb([1,5,10,20,50,100],5))
    pass