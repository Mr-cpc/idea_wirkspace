import heapq


def kthsmdis(nums:list,k:int) -> int:
    h = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            dis = abs(nums[j] - nums[i])
            if len(h) < k:
                heapq.heappush(h,-dis)
            else:
                if dis < -h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h,-dis)
    return -h[0]


def kthsmdis2(nums:list,k:int) ->int:
    h = [float("-inf")] * k
    heapq.heapify(h)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            dis = abs(nums[j] - nums[i])
            if dis < -h[0]:
                heapq.heappop(h)
                heapq.heappush(h,-dis)
    return h[0]

'''
:param nums a sorted list
:param tar target
return the num of pairs that dif two numbers in the list
'''
def search(nums:list, tar:int) -> int:
    res,l,r = 0,0,1
    while r < len(nums):
        while l < r and nums[r] - nums[l] > tar:
            l += 1
        res += r - l
        r += 1
    return res


def kthsmdis3(nums:list,k:int) -> int:
    nums.sort()
    l,r = 0,nums[-1] - nums[0]
    while l < r:
        mid = l + ((r - l) >> 1)
        count = search(nums,mid)
        if count < k:
            l = mid + 1
        else:
            r = mid
    return l

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

nums = [1,3,1]
# heapq.heapify(nums)
print(kthsmdis3(nums,1))
