import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from basic.bupt_2017_11_09.bstm import TreeNode
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2018-05-16
Time:14:22
'''
def lca(root:TreeNode,p:TreeNode,q:TreeNode) -> TreeNode:
    if p == root:
        return p
    if q == root:
        return q
    stk = []
    pre = None
    p_is_found,q_is_found = False,False
    ancestor_of_p = None
    ancestor_of_q = None
    while root or stk:
        while root:
            stk.append(root)
            root = root.left
        root = stk[-1]
        if root.right == pre or root.right is None:
            stk.pop()
            if root == p:
                p_is_found = True
                ancestor_of_p = stk[::-1]
            if root == q:
                q_is_found = True
                ancestor_of_q = stk[::-1]
            pre = root
            root = None
            if p_is_found and q_is_found:
                break
        else:
            root = root.right
    if len(ancestor_of_p) > len(ancestor_of_q):
        p,q = q,p
        ancestor_of_p,ancestor_of_q = ancestor_of_q,ancestor_of_p
    if p in ancestor_of_q:
        return p
    for ancestor_p in ancestor_of_p:
        for ancestor_q in ancestor_of_q:
            if ancestor_p == ancestor_q:
                return ancestor_p
    return None
if __name__ == '__main__':
    pass
    