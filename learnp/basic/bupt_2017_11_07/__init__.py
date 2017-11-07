def f(n):
    if n in (0,1):
        return  1
    else:
        return n *f(n-1)