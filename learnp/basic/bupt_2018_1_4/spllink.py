import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from basic.bupt_2017_10_13.atn import ListNode
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
Time:10:35
'''
def splitlinked(root:ListNode,k:int):
    if root is None:
        return [None] * k
    length = get_len(root)
    ans = []
    if length <= k:
        while root:
            cur = root
            ans.append(root)
            root = root.next
            cur.next = None
        ans.extend([None] * (k-len(ans)))
        return ans
    else:
        rem = length % k
        num = length // k
        i = 0
        while i < rem:
            ans.append(root)
            for j in range(num):
                root = root.next
            cur = root
            root = root.next
            cur.next = None
            i += 1
        while i < k:
            ans.append(root)
            for j in range(num-1):
                root = root.next
            cur = root
            root = root.next
            cur.next = None
            i += 1
        return ans

def get_len(root:ListNode):
    i = 0
    while root:
        i+=1
        root = root.next
    return i
