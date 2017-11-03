def subaprodlek(nums,k):
    prefix = [1]*(len(nums) +1)
    res = []
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i-1] * nums[i-1]
    res = [nums[i:j] for i in range(len(prefix)) for j in range(i+1,len(prefix)) if prefix[j] / prefix[i] < k]
    return res

def slide(nums,k):

    # i, j = 0, 0
    pro ,l,r= 1,0,0
    res = 0
    while r < len(nums):
        pro *= nums[r]
        while pro >= k:
            pro /= nums[l]
            l+=1
        res += r - l +1
        r+=1
    return res
    #
    # pass
res = subaprodlek([10,5,2,6],50)
print(slide([10,5,2,6],50))
print(len(res))