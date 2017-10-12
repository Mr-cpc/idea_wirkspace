import math
import numpy
from matplotlib.pyplot import *
import random
from basic.lr.linear import Linear


class logis(Linear):
    logistic = lambda x:1/(1+math.e**(-x))
    def check_sam(self,points):
        for point in points:
            if point[-1] not in (0,1):
                raise Exception("标签必须是0或1")
    def __init__(self,params,points,learn_rate = 0.01):
        self.check_sam(points)
        self.params = params[:]
        self.points = points[:]
        self.learn_rate = learn_rate

    def gradient_desc(self,):
        for i in range(len(self.params)):
            change = 0
            for j in range(len(self.points)):
                change += self.logistic((self.mul(self.params,self.points[j][:len(self.points[j])-1]) - self.points[j][-1])) * self.points[j][i] // len(self.points)
            self.params[i] -= self.learn_rate * change

    def ran_gradient_desc(self):
        for i in range(len(self.params)):
            ran_point = self.points[random.randrange(0,len(self.points))]
            self.params[i] -= self.learn_rate * self.logistic(((self.mul(self.params,ran_point[:-1])-ran_point[-1])*ran_point[i]))

    def predict(self,point):
        return 1 if self.logistic(self.mul(self.params,point)) else 0

x = numpy.linspace(-5,-1,5)
print(x)
# logistic = lambda x:1/(1+math.e**(-x))
# y = map(logistic,x)
# plot(x,list(y))
# show()