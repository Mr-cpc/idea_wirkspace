import abc
from functools import reduce

from math import sqrt

import math


class Vec:
    def __init__(self,data):
        self.data = data[:]

    @abc.abstractmethod
    def mul(self,vec):pass

    def dotp(self,vec):
        return reduce(lambda x,y:x+y,map(lambda x,y:x*y,self.data,vec.data))

    def nump(self,num):
        return Vec([num * data for data in self.data])

    def sub(self,vec):
        return Vec([self.data[i]-vec.data[i] for i in range(len(vec.data))])
    def __add__(self, other):
        return Vec([self.data[i] + other.data[i] for i in range(len(self.data))])

    def __mul__(self, other):
        if isinstance(other,Vec):
            return self.dotp(other)
        elif isinstance(other,(int,float)):
            return self.nump(other)

    def mol(self):
        return sqrt(reduce(lambda x,y:x+y,map(lambda x:x**2,self.data)))

    def norm(self):
        mold = self.mol()
        vec = Vec([x/mold for x in self.data])
        return vec

    def orthogonal(vecs:list):
        orths = []
        for i in range(len(vecs)):
            vec = Vec(vecs[i].data)
            for j in range(i):
                vec = vec.sub(orths[j].nump(vecs[i].dotp(orths[j])/orths[j].dotp(orths[j])))
            orths.append(vec)
        return [vec.norm() for vec in orths]

    def distance(self,vec):
        if len(self.data) != len(vec.data):
            raise Exception("dim not equals")
        return sqrt(sum([(vec.data[i] - self.data[i])**2 for i in range(len(self.data))]))
    '''
    use xi-min(x) / max(x)-min(x) to standard vecs
    '''
    def sta(vecs:list) -> None:
        maxes = [max([vecs[j].data[i] for j in range(len(vecs))]) for i in range(len(vecs[0].data))]
        mines = [min([vecs[j].data[i] for j in range(len(vecs))]) for i in range(len(vecs[0].data))]
        for i in range(len(vecs)):
            for j in range(len(vecs[i].data)):
                vecs[i].data[j] = (vecs[i].data[j] - mines[j]) / (maxes[j] - mines[j])

    def get_clustercenter(vecs:list):
        return Vec([sum([vecs[j].data[i] for j in range(len(vecs))])/len(vecs) for i in range(len(vecs[0].data))])

    def is_converg(v1:list,v2:list,error:float):
        for i in range(len(v1)):
            if v1[i].distance(v2[i]) > error:
                return False
        return True

    def __str__(self):
        return str(self.data)


a = [[i+j for i in range(3)] for j in range(3)]
print(a)
vecs = [Vec(row) for row in a]
c = Vec.get_clustercenter(vecs)
print(c)