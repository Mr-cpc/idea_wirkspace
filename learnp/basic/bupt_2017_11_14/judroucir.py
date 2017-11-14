def judroucir(moves:str) ->bool:
    d = {'L':0,'R':0,'U':0,'D':0}
    for ch in moves:
        if ch in d:
            d[ch] += 1
    return d['L'] == d['R'] and d['U'] == d['D']