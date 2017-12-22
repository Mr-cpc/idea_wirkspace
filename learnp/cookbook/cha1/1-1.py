import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2017-12-22
Time:14:06
'''

# 将可迭代对象同时赋值给多个变量是允许的，唯一的要求就是，变量的个数要与可迭代对象中元素的数量相同
series = [1,'a',2,(3,4)]
a,b,c,d = series
# print(d[0])

# 当变量的个数与可迭代对象中元素数量不相同时，会raise一个ValueError

# a,b,c,d,e = series
# a,b,c = series

#迭代器、生成器、字符串、文件对象也可以直接使用这种语法
it = iter(series)
a,b,c,d = it
a,b,c,d = 'abcd'
# print(d[0])

# *表达式在这种语法中的作用，如果只想取得可迭代对象中的前n个，后n个，或者中间的n个元素，可以使用*表达式
# *表达式一定是以列表的类型返回

a,*b,c = series #中间n-2个
# print(b)
*a,b,c = series #前n-2个
# print(a)

a,b,*c = series #后n-2个
# print(c)

# 保留最后(最近)n个元素，使用collections模块的deque,比如，在一个文件中按指定的模式逐行匹配文本
from collections import deque
def search(lines,pattern,history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if re.match(pattern,line):
            yield line,previous_lines
            previous_lines.append(line)
def use():
    with open('a.txt') as f:
        for matched,previous_lines in search(f,r'\d+'):
            print('cur_matched:{}'.format(matched))
            print('previous_lines:{}'.format(previous_lines))
            print('---------------')
# use()

# 查找集合中最大/最小的 n个元素，使用collections模块的heapq,
import heapq
def nlargest(series,n,key = None):
    return heapq.nlargest(n,series,key)
def nsmallest(series,n,key = None):
    return heapq.nsmallest(n,series,key)
series = range(10)
previous_3_largest = nlargest(series,3)
# print(previous_3_largest)
previous_3_smallest = nsmallest(series,3)
# print(previous_3_smallest)
# 如果待比较对象是一个复杂对象，希望按指定的属性进行比较，可以通过传入一个匿名函数，其返回值为指定的属性；也可以返回包含多个属性的元组,优先级依次递减
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 100, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

m=  nlargest(portfolio,3, lambda x:(x['shares'],x['price']))
m=  nlargest(portfolio,3, lambda x:x['shares'])
# print(m)

# 一键映射多个值的字典，使用collections模块的defaultdict可以为每个key生成一个默认的value映射，避免raise ValueError，并且使用起来更加优雅
from collections import defaultdict
d = defaultdict(list) # key的默认映射是空列表，[]
d = defaultdict(int) # key的默认映射是0
# 通过zip函数让字典按值比较，首先翻转dict的键与值的顺序，让形成的元组value在前，key在后
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
m = min(zip(prices.values(),prices.keys()))
# print(m)
# 寻找两个dict的相同点，dict的keys()方法和items方法都可以被当做集合来使用
prices.keys() & prices.keys()
prices.items() & prices.items()

# 消除序列中的重复元素并保持剩下的元素的相对顺序，可以使用生成器和set来解决
def generate_no_dup(series,key = None): # 若不传key，此方法仅仅对于序列元素是hashable的时候，dict不是hashable
    seen = set()
    for item in series:
        if item not in seen:
            val = item if key is None else key(item)
            seen.add(val)
            yield item
prt(list(generate_no_dup([1,2,3,5,2,3])))

# 对于dict类型，对上述代码需要进行一点修改，dict本身不可hashble，但是二元组的list是hashable
a = [(1,2)]
b = [1,2]
s = {a}
print(b in s)
# prt(list(generate_no_dup( [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}])))