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
Date:2018-06-11
Time:16:18
'''

# print()函数的高级用法

# print本身是可以接受不定长的打印对象的，并且可以以指定的分隔符连接，终止符也可以指定
# 默认的分隔符是' ',默认的终止符是'\n'，
# 现在假设有一个整形的数组[1,2,3]，希望将他以','连接作为一个字符串打印。

# 通常的写法
a = [1,2,3]
# print(','.join(str(x) for x in a))

# 更优雅的写法
# 这种写法的比上面好就好在，join方法要求序列的元素必须是str类型。
# def print(self, *args, sep=' ', end='\n', file=None) 这是print方法的签名
# 可以看出，实际上用变长参数
# print(*a,sep=',')

# 文件路径名相关的操作，使用os.path
path = r'C:\Users\waiting\Desktop\contest\idea_wirkspace\learnp\cookbook\cha5\5-1.py'
import os
# 根据一个完整的文件路径获取文件名
x = os.path.basename(path)
# print(x)

#根据一个完整的文件路径获取目录路径
dir_name = os.path.dirname(path)
# print(dir_name)

# 测试文件是否存在
file_exist = os.path.exists(path)
# print(file_exist)

# 测试目录是否存在
dir_exist = os.path.exists(dir_name)
# print(dir_exist)

# 判断是是否文件
is_file = os.path.isfile(dir_name)
# print(is_file)

# 判断是否是目录
is_dir = os.path.isdir(x)
# print(is_dir)
# 在任何时候处理文件路径相关的问题时，都应该使用os.path而不是使用标准的字符串操作，
# 因为os.path知道如何处理unix和windows的平台差异，对诸如文件分隔符等问题进行处理。
if __name__ == '__main__':
    pass
    