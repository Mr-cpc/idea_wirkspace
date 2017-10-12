import math
import numpy
from matplotlib.pyplot import *

x = numpy.linspace(-100,100,500000)
logistic = lambda x:1/(1+math.e**(-x))
y = map(logistic,x)
plot(x,list(y))
show()