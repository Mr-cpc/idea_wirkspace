def miidxsuoftwolis(list1:list,list2:list) ->list:
    d1 = {key:idx for idx,key in enumerate(list1)}
    d2 = {key:idx for idx,key in enumerate(list2)}
    d3 = {key:d1[key] + d2[key] for key in d1 if key in d2}
    min_v = len(list1) + len(list2)
    for key in d3:
        min_v = min(min_v,d3[key])
    return [key for key in d3 if d3[key] == min_v]