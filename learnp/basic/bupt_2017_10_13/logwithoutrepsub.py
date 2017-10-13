#no.3
import math
def logwithoutrepsub(s):
    ans,local_max = 0,0
    ch_set = set()
    for ch in s:
        if ch not in ch_set:
            local_max += 1
            ch_set.add(ch)
        else:
            ans = max(ans,local_max)
            local_max  = 1
            ch_set.clear()
            ch_set.add(ch)

    ans = max(ans,local_max)
    return ans

print(logwithoutrepsub("pwwkew"))