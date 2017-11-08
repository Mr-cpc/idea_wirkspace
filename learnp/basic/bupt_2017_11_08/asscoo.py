import heapq


def asco(g:list,s:list) -> int:
    ans = 0
    heapq.heapify(g)
    s.sort()
    for i in s:
        if g[0] <= i:
            ans += 1
            heapq.heappop(g)
    return ans


g = [1,2,3]
s = []
print(asco(g,s))