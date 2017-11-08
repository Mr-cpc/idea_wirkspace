def arco(n:int) ->int:
    res,cur = 0,0
    while cur < n:
        cur += res
        if cur > n:
            return res -1
        elif cur == n:
            return res
        res += 1
    return res

print(arco(8))