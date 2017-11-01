import random
from matplotlib.pyplot import *

from basic.bupt_2017_10_19.mat import Mat


class Linear(object):
    def __init__(self,params,points,learn_rate = 0.01):
        self.params = params[:]
        self.points = points[:]
        self.learn_rate = learn_rate
        # x = Mat(ndarray = [point[:-1] for point in points])
        # trans_x = x.transpose()
        # b = Mat(ndarray = [[point[-1]] for point in points])
        # self.params =  (trans_x * x).inv() * trans_x * b

    def set_learnrate(self, learn_rate):
        self.learn_rate = learn_rate

    def mul(self,a,b):
        res = 0.0
        if len(a) != len(b):
            pass
        else:
            for i in range(len(a)):
                res += a[i] * b[i]
        return res

    def compute_error(self):
        error = 0
        for i in range(len(self.points)):
            feature = self.points[i][:len(self.points[i])-1]
            error += (self.mul(self.params,feature) - self.points[i][-1]) ** 2
        return error / (2 * len(points))

    def gradient_desc(self):
        for i in range(len(self.params)):
            change = 0
            for j in range(len(self.points)):
                change += (self.mul(self.params,self.points[j][:len(self.points[j])-1]) - self.points[j][-1]) * self.points[j][i] / len(self.points)
            self.params[i] -= self.learn_rate * change

    def ran_gradient_desc(self):
        for i in range(len(self.params)):
            ran_point = self.points[random.randrange(0,len(self.points))]
            self.params[i] -= self.learn_rate * ((self.mul(self.params,ran_point[:-1])-ran_point[-1])*ran_point[i])

    def predict(self,point):
        return self.mul(self.params,point)
params = [1,7]
points = [[1,2,5],[1,3,8],[1,4,10]]
linear = Linear(params,points)
print(linear.params)
linear.set_learnrate(0.01)
x = [i[1] for i in points]
y = [i[2] for i in points]
plot(x,y,"g^")
for i in range(5000):
    print(linear.params)
    print(linear.compute_error())
    x = [ i[1] for i in linear.points]
    y = [linear.mul(linear.params,linear.points[i][:len(linear.points[i])-1]) for i in range(len(linear.points))]
    plot(x,y)
    linear.gradient_desc()
savefig("re.png")
