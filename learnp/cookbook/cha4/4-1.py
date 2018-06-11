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
Date:2018-06-08
Time:9:22
'''

# iter()方法返回迭代器，即返回一个实现了__next__方法的对象
a = [1,2,3]
it = iter(a)
# 生成器一定是迭代器，但是迭代器不一定是生成器
# 自定义一个浮点数的range函数
def frange(start,stop,inc = 0.1):
    x = start
    print("start")
    while x < stop:
        yield x
        x += inc
# 浮点数运算不准确，0.1 + 0.2 > 0.3,0.7 + 0.1 < 0.8
# for x in g:
#     print(x)
# 这一步只是返回了generator,实际上frange函数里的一行代码都还没有执行，也不会打印出 “start”
g = frange(0,0.8)
# 当第一次对generator调用next时，frange函数里的代码才开始第一次执行
# print(next(g))
# with open('a.txt','r') as f:
#     for line in f:
#         print(len(line))
iter(lambda x:x.startswith('#'),True)
# print(sum(frange(0,0.8)))
if __name__ == '__main__':
    pass
    