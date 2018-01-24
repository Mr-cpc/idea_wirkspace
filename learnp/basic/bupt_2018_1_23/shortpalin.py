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
Time:16:54
'''
# def shortpalin(s:str):
#     l = []
#     for x in s:
#         l.append('#')
#         l.append(x)
#     l.append('#')
#     p = [0] * len(l)
#     center,max_right = 0,0
#     for i in range(len(l)):
#         if i < max_right:
#             p[i] = min(max_right - i,p[2 * center - i])
#         else:
#             p[i] = 1
#         while i + p[i] < len(p) and i - p[i] >= 0 and l[i+p[i]] == l[i-p[i]]:
#             p[i] += 1
#         if i + p[i] - 1> max_right:
#             max_right = i + p[i] - 1
#             center = i
#     print([str(x) for x in p])
#     print(l)
#     print(''.join(l))

'''
brute force
'''
def shortpalin(s:str):
    for i in range(len(s),0,-1):
        x = s[:i]
        if x == x[::-1]:
            break
    print(i)
    return s[i:][::-1] + s
def shortpalin2(s:str):
    t = '{}#{}*'.format(s,s[::-1])
    _next_ = next(t)
    print(_next_[-1])
    print(_next_)
    return '{}{}'.format(s[_next_[-1]:][::-1],s)

def next(s:str):
    _next_ = [0] * len(s)
    _next_[0] = -1
    for i in range(2,len(s)):
        k = _next_[i-1]
        while k != -1 and s[k] != s[i-1]:
            k = _next_[k]
        _next_[i] = k + 1
    return _next_
if __name__ == '__main__':
    # a = shortpalin('ass')
    # print(next('abaa'))
    a = shortpalin2('')
    print(a)
    pass

    