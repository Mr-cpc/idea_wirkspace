def lgessub(s1,s2):
    sho,lo = (s1, s2) if len(s1) <= len(s2) else s2,s1
    res = 0
    for i in range(len(sho)):
        for j in range(i+1,len(sho)+1):
            if sho[i:j] in lo:
                res = max(res,j - i)
    return res

def lgessub2(s1,s2):
    p = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    for i in range(1,len(p)):
        for j in range(1,len(p[0])):
            p[i][j] = p[i-1][j-1] + 1 if s2[i-1] == s1[j-1] else max(p[i-1][j],p[i][j-1])
    return p[len(s2)][len(s1)]

s1 = "12321047a"
s2 = "321047a"
print(lgessub(s1,s2))