def dfs(s:str, ans:list, cur:list):
    if len(s) == 0:
        if len(cur) == 4:
            ans.append(cur)
    elif len(s) == 1:
        cur.append(s)
        dfs(s[1:],ans,cur[:])
    elif len(s) == 2:
        if len(cur) == 2:
            copy = cur[:]
            copy.extend(s)
            ans.append(copy)
        elif len(cur) == 3:
            copy = cur[:]
            copy.append(s)
            ans.append(copy)
        else:
            pass
    else:
        copy1 = cur[:]
        copy1.append(s[0])
        dfs(s[1:],ans,copy1)
        copy1 = cur[:]
        copy1.append(s[:2])
        dfs(s[2:],ans,copy1)
        if s[0] != '0' and 0 < int(s[:3]) <= 255:
            copy1 = cur[:]
            copy1.append(s[:3])
            dfs(s[3:],ans,copy1)



def restoip(s:str) -> list:
    if len(s) > 12:
        return []
    ans = []
    dfs(s,ans,[])
    return ans

print(restoip("882456854658"))