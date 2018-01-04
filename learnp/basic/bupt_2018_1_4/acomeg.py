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
Date:2018-01-04
Time:14:47
'''
def acountmeg(accounts:list):
    from collections import defaultdict
    d = defaultdict(list)
    for account in accounts:
        d[account[0]].append(account[1:])
    ans = []
    # print(d)
    from basic.bupt_2017_12_29.delandear import UF
    for name,accountss in d.items():
        uf = UF(accountss)
        for i in range(len(accountss)):
            for j in range(i+1,len(accountss)):
                if set(accountss[i]) & set(accountss[j]):
                    uf.union(i,j)
        d_ = defaultdict(list)
        for i,value in enumerate(uf.id):
            d_[value].append(accountss[i])
        # print(d_)
        for value in d_.values():
            cur = [name]
            s = set()
            for accounts in value:
                s |= set(accounts)
            cur.extend(sorted(list(s)))
            ans.append(cur)
    return ans
print(acountmeg([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))