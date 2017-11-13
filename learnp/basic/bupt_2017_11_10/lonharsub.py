import collections


def lonharsu(nums:list) -> list:
    d = {}
    ans = 0
    for num in nums:
        d[num] = d.get(num,0) + 1
    for num in nums:
        plus1 = d.get(num + 1,0)
        minus1 = d.get(num - 1,0)
        ans = max(ans,max(0 if plus1 == 0 else plus1 + d[num],0 if minus1 == 0 else minus1 + d[num]))
    return ans
