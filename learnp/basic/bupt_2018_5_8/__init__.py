import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from basic.bupt_2017_10_30.deco import time_statistic
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2018-05-08
Time:9:40
'''
@time_statistic
def solve():
    ans = 0
    with open("ans.txt","w") as f:
        for i in range(100000000,1000000000):
            num = str(i)
            num = int(num[:4]+num[5:])
            if i % num == 0:
                ans += 1
                f.write(str(i))
                f.write("\n")
    print(ans)
if __name__ == '__main__':
    solve()