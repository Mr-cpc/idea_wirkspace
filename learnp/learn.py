import matplotlib.pyplot as plt
from math import *
import numpy as np

class Plot:
    def __init__(self,x_axes,y_axes,**kwargs):
        self.x = x_axes
        self.y = y_axes
        self.kwarg = kwargs
    def plot(self):
        plt.title(self.kwarg["tit"])
        plt.xlabel(self.kwarg["xlab"])
        plt.ylabel(self.kwarg["ylab"])
        plt.plot(self.x,self.y)

    def subplot(self,rep:str,kind = "line"):
        plt.subplot(int(rep))
        if kind == "line":
            plt.plot(self.x,self.y)
        elif kind == "pie":
            plt.pie(self.y)
        elif kind == "sca":
            plt.scatter(self.x,self.y)
        else:
            plt.bar(self.x,self.y)

    def show(self):
        plt.show()

    def save(self,path:str):
        plt.savefig(path)


def one_pic():
    logistic = lambda x:1/(1+e**-x)
    x = np.linspace(0,2*pi,5000)
    plot = Plot(x,list(map(sin,x)),**{"tit":"sin(x)","xlab":"x value","ylab":"y value"})
    plot.plot()
    plot.show()
def mul_pic():
    x = [1,2,3,4,5]
    y = [2.3,3.4,1.2,6.6,7.0]
    plot = Plot(x,y,**{"tit":"sin(x)","xlab":"x value","ylab":"y value"})
    plot.subplot("221")
    plot.subplot("222",kind="bar")
    plot.subplot("223",kind="sca")
    plot.subplot("224",kind="pie")
    plot.show()

mul_pic()
# savefig("a.png")


