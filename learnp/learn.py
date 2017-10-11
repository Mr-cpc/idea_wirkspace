from matplotlib.pyplot import *
from math import *
import numpy as np
p1 = []
p2 = []
start = 0
p1 = np.linspace(0,pi,5000)
# while start <= 2:
#     p1.append(start)
#     start += 0.001
print(list(map(sin,p1)))
plot(p1,list(map(sin,p1)))
title("sin(x)")
xlabel("x value")
ylabel("y value")
savefig("a.png")
show()