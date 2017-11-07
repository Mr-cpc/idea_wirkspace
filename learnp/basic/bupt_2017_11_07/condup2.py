def condup2(nums:list,k:int) ->bool:
    d = {}
    for idx,num in enumerate(nums):
        if num not in d:
            d[num] = idx
        else:
            if idx - d[num] <= k:
                return True
            else:
                d[num] = idx
    return False
