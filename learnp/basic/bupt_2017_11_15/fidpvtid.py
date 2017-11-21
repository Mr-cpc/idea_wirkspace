def fidpvtid(nums:list)->int:
    prefix = [0] * (len(nums) + 1)
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i-1] + nums[i-1]
    print(prefix)
    for i in range(1,len(nums)-1):
        if prefix[i] == prefix[-1] - prefix[i+1]:
            return i
    else:
        return -1