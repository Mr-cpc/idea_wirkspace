import heapq


def rera(nums:list) ->list:
    sorted_nums = sorted(nums,key=lambda x:-x)
    print(sorted_nums)
    d = {}
    for idx,val in enumerate(sorted_nums):
        if idx == 0:
            d[val] = "Gold Medal"
        elif idx == 1:
            d[val] = "Silver Medal"
        elif idx == 2:
            d[val] = "Bronze Medal"
        else:
            d[val] = str(idx + 1)
    return [d[num] for num in nums]

print(rera(list(range(1,6))[::-1]))