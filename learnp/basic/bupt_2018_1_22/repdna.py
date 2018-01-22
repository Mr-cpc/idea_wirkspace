from basic.bupt_2017_10_30.deco import time_statistic


@time_statistic
def repdna2(s:str):
    from collections import defaultdict
    d = defaultdict(int)
    ans = []
    for i in range(len(s)-9):
        x = s[i:i+10]
        d[x] += 1
        if d[x] == 2:
            ans.append(x)
        else:
            continue
    return ans
def repdna(s:str):
    return [s[i:i+10] for i in range(len(s)-9) if s[i:i+10] in s[i+10:]]
def encode(s:str) -> int:
    enc = 0
    d = {'A':0,'C':1,'G':2,'T':3}
    i = 0
    for ch in s:
        enc += (d[ch] << i)
        i += 2
        enc <<= i
    return enc
def repdna3(s:str):
    from collections import defaultdict
    d = defaultdict(int)
    ans = []
    for i in range(len(s)-9):
        x = s[i:i+10]
        y = encode(x)
        d[y] += 1
        if d[y] == 2:
            ans.append(x)
        else:
            continue
    return ans

print(repdna3("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))