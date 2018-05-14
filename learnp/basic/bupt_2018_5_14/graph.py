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
Date:2018-05-14
Time:14:39
'''
from sys import stdin
class DirectedGraph:
    def __init__(self):
        self.v_n = int(stdin.readline().strip())
        self.e_n = int(stdin.readline().strip())
        self.g = [[float('inf') for i in range(self.v_n)] for j in range(self.v_n)]

        for i in range(self.v_n):
            self.g[i][i] = 0
        for i in range(self.e_n):
            fr,to,weight = [int(ele) for ele in stdin.readline().strip().split(' ')]
            self.g[fr][to] = weight

    def dfs(self,start:int):
        visited = [False] * self.v_n
        self._dfs(start,visited)
    def shortest_path(self,i:int,j:int):
        return self.dijkstra(i)[j]

    def dijkstra(self,start:int):
        dist = [self.g[start][i] for i in range(self.v_n)]
        s = [start]
        u = [i for i in range(self.v_n) if i != start]
        while u:
            tmpv,min_path = None,float('inf')
            for v in u:
                if dist[v] <= min_path:
                    tmpv,min_path = v,dist[v]
            s.append(tmpv)
            u.remove(tmpv)
            self.modify_dist(dist,tmpv,start)
        print(dist)
        return dist

    def topological_sort(self):
        self.topo_serial = []
        self.dfs(0)

    def modify_dist(self, dist:list, tmpv:int,start:int):
        for i in range(self.v_n):
            cur_dist = self.g[start][tmpv] + self.g[tmpv][i]
            if cur_dist < dist[i]:
                dist[i] = cur_dist

    def _dfs(self, start:int,visied:list):
        if visied[start]:
            return
        self.visit(start)
        visied[start] = True
        for i in range(self.v_n):
            if i != start and self.g[start][i] != float('inf'):
                self._dfs(i,visied)

    def visit(self, start):
        self.topo_serial.append(start)
        print('visit {}'.format(start))


if __name__ == '__main__':
    graph = DirectedGraph()
    graph.topological_sort()
    print(graph.topo_serial[::-1])
    