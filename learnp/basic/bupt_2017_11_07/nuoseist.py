def numoseginstr(s:str) ->int:
    res = 1
    s = s.strip()
    i = 0
    while i < len(s):
        if s[i] != " ":
            i += 1
        else:
            res += 1
            while s[i] in (" ","\t"):
                i += 1
    return res
