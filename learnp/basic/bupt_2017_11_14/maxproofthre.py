import heapq
from functools import reduce


def maxproofthre(nums: list):
    mi = [float("-inf")] * 3
    ma = [float("-inf")] * 3
    for x in nums:
        if x > mi[0]:
            heapq.heappop(mi)
            heapq.heappush(mi, x)
        if x < -ma[0]:
            heapq.heappop(ma)
            heapq.heappush(ma, -x)
    max3 = [heapq.heappop(mi) for i in range(len(mi))]
    min3 = [-heapq.heappop(ma) for i in range(len(ma))]
    if min3[-1] >= 0:
        return reduce(lambda x, y: x * y, max3)
    else:
        if min3[-2] >= 0:
            return reduce(lambda x, y: x * y, max3)
        else:
            return max(min3[-1] * min3[-2] * max3[2],max3[-1] * max3[-2] * max3[0])


print(maxproofthre([722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786]
                   ))
