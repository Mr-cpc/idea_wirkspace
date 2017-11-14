import heapq

a = range(10)
mi = [float("-inf")]*3
ma = [float("-inf")]*3

for x in a:
    if x > mi[0]:
        heapq.heappop(mi)
        heapq.heappush(mi,x)
    if x < -ma[0]:
        heapq.heappop(ma)
        heapq.heappush(ma,-x)
print(mi)
print(ma)