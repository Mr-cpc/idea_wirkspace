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
Date:2018-05-08
Time:14:41

昨天晚上第一次看到这个题，感觉题意听的明白但是就是不知道怎么写，感觉是用正则表达式。今天白天想了一下，用暴力写了出来。基本思想是以每个字符开头，分别查找长为1,2..n的子串，看是否有出现重复，如果有，记录重复的次数和当前最开始重复的位置放到dict里面，一旦某个位置找到了长为i的重复子串，则长度大于i的就不再考虑了。最后根据dict中的内容构造出去重的字符串。dict的key为一个二元tuple,tuple[0]存放重复的子串，tuple[1]存放该子串开始重复的初始位置，之所以同时存两个而不是仅仅存重复子串，是因为更后面的某个位置可能也出现相同的重复子串，如果直接计数，最后根据dict构造的去重字符串就不对了。下面是python代码：
'''
from collections import defaultdict
def quchong(s:str) -> str:
    d = defaultdict(int)
    i = 0
    while i < len(s) - 2:
        flag = False
        for j in range(2,len(s)):
            if i + j >= len(s):
                break
            substr = s[i:i+j]
            if substr.isdigit():
                break
            k = 1
            while i + j * k < len(s) and s[i+j*k:].startswith(substr):
                k += 1
                d[(substr,i)] += 1
                flag = True
            if flag:
                i = i + k * j
                break
        if not flag:
            i += 1
    for key in sorted(d.keys(),key=lambda key:-key[1]):
        s = s[:key[1]+len(key[0])] + s[key[1]+(d[key]+1)*len(key[0]):]
    return s
if __name__ == '__main__':
    x = "刚才我说了我要退款我要退款我要退款，我都说了我要退款我要退款我要退款"
    print(quchong(x))
