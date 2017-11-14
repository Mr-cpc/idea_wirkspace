import heapq
from functools import reduce


def maxproofthre(nums:list) -> int:
    mi = [float("-inf")]*3
    ma = [float("-inf")]*3
    for x in nums:
        if x > mi[0]:
            heapq.heappop(mi)
            heapq.heappush(mi,x)
        if x < -ma[0]:
            heapq.heappop(ma)
            heapq.heappush(ma,-x)
    max3 = [heapq.heappop(mi) for i in range(len(mi))]
    min3 = [-heapq.heappop(ma) for i in range(len(ma))]
    print(max3)
    print(min3)
    if min3[-1] >= 0:
        return reduce(max3,lambda x,y:x*y)
    else:
        if min3[-2] >= 0:
            return reduce(max3,lambda x,y:x*y)
        else:
            posi = max3[-1] * max3[-2]
            neg = min3[-1] * min3[-2]
            return neg * max3[2] if neg >= posi else posi * max3[0]

print(maxproofthre([1,2,3,4,5,-5,-4]))