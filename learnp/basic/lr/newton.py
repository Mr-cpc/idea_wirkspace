import math

def newton(n):
    fun = lambda x : x**2 - n
    x = 1
    y = fun(x)
    while True:
        pre = x
        x -= fun(x) / (2*x)
        if math.fabs(x- pre) < 1e-5:
            break
    return x
print(newton(9))