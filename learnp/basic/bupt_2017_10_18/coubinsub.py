def coubinsub(s):
    prefix = [0] * (len(s)+1)
    for i in range(1,len(prefix)):
        prefix[i] += prefix[i-1] + (1 if s[i-1] == '1' else -1)
    res = 0
    # print(prefix)
    for i in range(len(prefix)):
        for j in range(i+1,len(prefix)):
            if prefix[j] - prefix[i] == 0 and prefix[i+(j-i)//2]-prefix[i] in ((j-i)//2,-(j-i)//2):
                print(s[i:j])
                res += 1
    return res


print(coubinsub("10"))