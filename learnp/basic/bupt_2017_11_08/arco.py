import math


def arco(n:int) ->int:
    res = int(math.sqrt(2*n+0.25)-1/2)
    cur = res*(res+1)//2
    while cur < n:
        res += 1
        cur += res
        if cur > n:
            return res -1
        elif cur == n:
            return res
        res += 1
    return res

print(arco(8))
print(int(math.sqrt(2*6+0.25)-0.5))