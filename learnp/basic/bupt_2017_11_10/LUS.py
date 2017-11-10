def lus(a:str,b:str)->int:
    if "" in (a,b):
        return max(len(a),len(b))
    p = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1,len(p)):
        for j in range(1,len(p[0])):
            if a[i-1] == b[j-1]:
                p[i][j] = max(p[i-1][j],p[i][j-1],p[i-1][j-1])#大概推理出这一步是比较重要的,在LCS中有所不同，if a[i-1] != b[j-1]，max(p[i-1][j],p[i][j-1]）
            else:
                p[i][j] = p[i-1][j-1] + 1#这个应该是最容易理解的,就是LCS的 if a[i-1]==b[j-1],p[i][j] = p[i-1][j-1] + 1
    return p[len(a)][len(b)]

print(lus("abc",""))