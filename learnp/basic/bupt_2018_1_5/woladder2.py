from collections import Counter

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
Date:2018-01-05
Time:15:14
'''
@time_statistic
def wordlad2(beginWord:str,endWord:str,wordList:list) -> list:
    from collections import deque,namedtuple
    if endWord not in wordList:
        return []
    q = deque()
    Status = namedtuple('Status',['val','step','prev'])
    q.append(Status(beginWord,0,None))
    candis = []
    min_step = None
    while len(q):
        cur = q.popleft()
        if min_step is not None and cur.step > min_step:
            break
        if cur.val == endWord:
            if min_step is None:
                candis.append(cur)
                min_step = cur.step
                continue
            elif cur.step == min_step:
                candis.append(cur)
        else:
            q.extend(Status(word,cur.step+1,cur) for word in next_words(cur.val,wordList))
    ans = []
    for candi in candis:
        stk = deque()
        while candi:
            stk.appendleft(candi.val)
            candi = candi.prev
        ans.append(list(stk))
    return ans
def next_words(cur_word:str,wordList:list) -> list:
    nexts = []
    for word in wordList :
        dif = 0
        for i in range(len(word)):
            if word[i] != cur_word[i]:
                dif += 1
                if dif > 1:
                    break
        else:
            if dif == 1:
                nexts.append(word)
    return nexts
# def next_words(cur_word:str,wordList:list) -> list:
#     nexts = []
#     for word in wordList :
#         counter = Counter(word)
#         counter.subtract(cur_word)
#         if len(counter) == len(cur_word)+1:
#             nexts.append(word)
#     return nexts

print(wordlad2(beginWord = "qa",
endWord = "sq",
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
