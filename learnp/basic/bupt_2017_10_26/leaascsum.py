def leaascs(s1:str,s2:str):
    com = set(s1) & set(s2)
    res = sum(map(lambda x:0 if x in com else ord(x),s1))
    res += sum(map(lambda x:0 if x in com else ord(x),s2))
    s1_com = [item for item in s1 if item in com]
    s2_com = [item for item in s2 if item in com]
    return s1_com,s2_com


def backt(l, i, j, cur, res, s1,s2):
    if 0 in (i,j):
        res.append(cur[::-1])
        return
    if s1[j-1] == s2[i-1]:#here can't use l[i][j] == l[i-1][j-1] + 1 to judge,for l[i-1][j] or l[i][j-1] may ==l[i][j] but s1[i-1] != s2[j-1]
        cur.append(s1[j-1])
        print("s1[{}]:{}".format(j-1,s1[j-1]))
        backt(l,i-1,j-1,cur,res,s1,s2)
    else :
        if l[i-1][j] > l[i][j-1]:
            backt(l,i-1,j,cur[:],res,s1,s2)
        elif l[i][j] == l[i-1][j]:
            backt(l,i-1,j,cur[:],res,s1,s2)
            backt(l,i,j-1,cur[:],res,s1,s2)
        else :
            backt(l,i,j-1,cur[:],res,s1,s2)


def finccom(s1:str,s2:str):
    l = [[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            l[i][j] = l[i-1][j-1] + 1 if s1[j-1] == s2[i-1] else max(l[i-1][j],l[i][j-1])
    i , j = len(s2), len(s1)
    res = []
    backt(l,i,j,[],res,s1,s2)
    print(l)
    return res
    # m1,m2 = {},{}
    # l1,l2 = [],[]
    # res = 0
    # for ch in s1:
    #     if ch not in m1:
    #         l1.append(ch)
    #     m1[ch] = m1.get(ch,0)+1
    # for ch in s2:
    #     if ch not in m2:
    #         l2.append(ch)
    #     m2[ch] = m2.get(ch,0)+1
    # for key in m1:
    #     m1_val = m1[key]
    #     m2_val = m2.get(key)
    #     if m2_val == None:
    #         res += ord(key) * m1_val
    #         l1.remove(key)
    # for key in m2:
    #     m2_val = m2[key]
    #     m1_val = m1.get(key)
    #     if m1_val == None:
    #         res += ord(key) * m2_val
    #         l2.remove(key)
    # m1 = {key:m1[key] for key in l1}
    # m2 = {key:m2[key] for key in l2}
    # return res,m1,m2

res = leaascs("delete","leet")
print(res)
print(finccom("delete","leet"))