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
Date:2018-05-10
Time:10:34
'''
'''
输入
3 5 
2 4 2 
1 3 
3 5 
3 7 
5 9 
1 10

输出20
'''
from sys import stdin
from functools import total_ordering
@total_ordering
class Customer:
    def __init__(self,num_of_people:int,num_of_money:int):
        self.num_of_people = num_of_people
        self.num_of_money = num_of_money
    def __eq__(self, other):
        return self.num_of_people == other.num_of_people
    def __lt__(self, other):
        return self.num_of_people < other.num_of_people
    def __str__(self):
        return 'people:{},money:{}'.format(self.num_of_people,self.num_of_money)
# def bin_search(customers:list,cap:int):
#     low,high = 0,len(customers) - 1
#     while low < high:
#         mid = low + ((high - low) >> 1)
#         if customers[mid].num_of_people <=
n,m = [int(ele) for ele in stdin.readline().strip().split(' ')]
cap = [int(ele) for ele in stdin.readline().strip().split(' ')]
cap.sort()
max_cap = cap[-1]
customers = []
for i in range(m):
    x,y = [int(ele) for ele in stdin.readline().strip().split(' ')]
    if x <= max_cap:
        customers.append(Customer(x,y))
if len(customers) == 0:
    print(0)
customers.sort(key=lambda customer:(-customer.num_of_money,customer.num_of_people))
if n >= len(customers) and min(cap) > customers[-1].num_of_people:
    print(sum(customer.num_of_money for customer in customers))
ans = 0
for v in cap:
    for i in range(len(customers)):
        if customers[i].num_of_people <= v:
            ans += customers[i].num_of_money
            customers.remove(customers[i])
            break
print(ans)
if __name__ == '__main__':
    pass
    