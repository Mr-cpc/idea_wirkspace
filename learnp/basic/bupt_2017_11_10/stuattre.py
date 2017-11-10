def stuattre(s:str) ->bool:
    d = {'A':0,'L':0}
    for idx,rec in enumerate(s):
        if rec == 'P':
            d['L'] = 0
            continue
        elif rec == 'A':
            d[rec] += 1
            if d[rec] > 1:
                return False
            d['L'] = 0
        else:
            d[rec] += 1
            if d[rec] > 2:
                return False
    return True


