import heapq


def asco(g:list,s:list) -> int:
    ans = 0
    heapq.heapify(g)
    s.sort()
    for i in s:
        if not len(g):
            break
        elif g[0] <= i:
            ans += 1
            heapq.heappop(g)
    return ans


g=[10,9,8,7]
s=[5,6,7,8]
print(asco(g,s))