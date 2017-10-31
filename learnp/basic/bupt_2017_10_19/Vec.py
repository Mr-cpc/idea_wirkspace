import abc
from functools import reduce

from math import sqrt



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

    def orthogonal(vecs):
        orths = []
        for i in range(len(vecs)):
            vec = Vec(vecs[i].data)
            for j in range(i):
                vec = vec.sub(orths[j].nump(vecs[i].dotp(orths[j])/orths[j].dotp(orths[j])))
            orths.append(vec)
        return [vec.norm() for vec in orths]
    def __str__(self):
        return str(self.data)
