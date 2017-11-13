def ranadd1(m:int,n:int,ops:list) -> int:
    d = {}
    for pair in ops:
        for i in range(pair[0]):
            for j in range(pair[1]):
                d[(i,j)] = d.get((i,j),0) + 1
    k,max_v = 0,0
    for key in d:
        if d[key] >= max_v:
            max_v = d[key]
    for key in d:
        if d[key] == max_v:
            k += 1
    return k



