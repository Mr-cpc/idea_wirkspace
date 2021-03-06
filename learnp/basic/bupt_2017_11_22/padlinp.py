from basic.bupt_2017_10_18.ptkes import n_comb
from basic.bupt_2017_10_30.deco import time_statistic


@time_statistic
def padlinp(s:str):
    if len(s) == 1:
        return [[s]]
    ans = []
    if s == s[:][::-1]:
        ans.append([s])
    for i in range(1,len(s)):
        candis = n_comb(list(range(1,len(s))),i)
        for parti in candis:
            st = 0
            candi = []
            parti.append(len(s))
            for x in parti:
                cur = s[st:x]
                if cur == cur[:][::-1]:
                    candi.append(cur)
                    st = x
                else:
                    break
            else:
                ans.append(candi)
    return ans

print(padlinp("amanaplanacanalpanama"))
