def conret(n:int) ->list:
    dif = float("inf")
    l,r = None,None
    for i in range(1,n+1):
        w = n // i
        cur_dif = i - w
        if n%i == 0  and 0 <= cur_dif < dif:
            l,r = i,w
            dif = cur_dif
    return [l,r]
print(conret(7))