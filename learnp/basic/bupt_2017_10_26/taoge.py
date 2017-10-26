def search_(st:int,en:int,cur:list,res:list):
    if st > en:
        return
    elif st == en:
        cur_copy = cur[:]
        cur_copy.append(st)
        res.append(cur_copy)
    else:
        cur_copy = cur[:]
        cur_copy.append(st)
        search_(st+1,en,cur_copy,res)
        search_(st+2,en,cur_copy,res)

def search(st:int,en:int):
    res = []
    search_(st,en,[],res)
    return res

print(search(1,8))