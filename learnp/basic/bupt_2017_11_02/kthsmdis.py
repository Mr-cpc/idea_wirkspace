import heapq


def kthsmdis(nums:list,k:int) -> int:
    h = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            dis = abs(nums[j] - nums[i])
            if len(h) < k:
                heapq.heappush(h,dis)
            else:
                if dis < h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h,dis)
    return h[0]


def kthsmdis2(nums:list,k:int) ->int:
    h = [float("inf")] * k
    heapq.heapify(h)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            dis = abs(nums[j] - nums[i])
            if dis < h[0]:
                heapq.heappop(h)
                heapq.heappush(h,dis)
    return h[0]

def kthsm(nums:list,k:int):
    h = [float("-inf")] * k
    heapq.heapify(h)
    for num in nums:
        if num < -h[0]:
            heapq.heappop(h)
            heapq. heappush(h,-num)
    return -h[0]


def kthla(nums:list,k:int):
    h = [float("-inf")] * k
    heapq.heapify(h)
    for num in nums:
        if num > h[0]:
            heapq.heappop(h)
            heapq.heappush(h,num)
    return h[0]

nums = list(range(4))
heapq.heapify(nums)
# print(kthsmdis2(nums,1))
print(kthsm(nums,2))
