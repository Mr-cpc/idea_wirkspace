def condup2(nums:list,k:int) ->bool:
    for i in range(len(nums)-k):
        for j in range(i+1,i+k+1):
            if nums[i] == nums[j]:
                return True
    return False

