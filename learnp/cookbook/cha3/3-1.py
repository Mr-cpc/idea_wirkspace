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
Date:2018-06-05
Time:10:15
'''
'''
浮点数的格式化输出
使用内置的format方法，接受一个浮点数，一个格式说明的字符串
0.2f表示，保留两位小数的浮点数
'''
def retain(num:float,n:int) -> str:
    return format(num,'0.{}f'.format(n))
# print(retain(1.2,20))
'''
分数形式的运算，fractions模块的Fraction对象接受一个分子，一个分母，可以
以分数的形式来表示一个有理数。
以给定分子分母的形式构造，如1/4，Fraction(1,4)
也可以直接传入一个数字来构造，比如Fraction(1.2)
但是要注意，这种情况得到的并不是我们想象中的6/5，而是两个非常长的数字之比，
因为只要不是2的整数次幂的数字，在内存中都不是精确表示的。
因此，如果想直接以小数的形式构造，应该传入一个字符串形式的小数，像Fraction('1.2')
就会得到预想中的6/5
'''
from fractions import Fraction
a = Fraction(3,4)
b = Fraction(1,16)
c = Fraction("1.2")
'''
通过numerator属性获得分母，denominator属性获得分子
'''
# print(c.numerator)
# print(c.denominator)

'''
随机抽样
random模块使用的mersenne twister算法来产生伪随机数的
这是目前被认为最高效的伪随机数生成算法
使用ramdom模块来产生随机数和随机的抽样。
从序列中随机选择一个元素，使用choice方法
'''
import random
values = list(range(10))
# print(random.choice(sets))
'''
使用sample方法来从序列中随机选择n个元素
'''
# print(random.sample(values,3))
'''
使用shuffle来打乱序列
'''
random.shuffle(values)
# print(values)
if __name__ == '__main__':
    n = 5
    pos = len([x for x in range(n) if random.randint(0,1) == 1])
    print(pos / n)


    