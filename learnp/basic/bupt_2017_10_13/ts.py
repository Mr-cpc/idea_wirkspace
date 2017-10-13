#no.1
class s:
    def ts(self,nums,target):
        nums.sort()
        i,j = 0,len(nums) -1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]
            elif sum > target:
                j -= 1
            else:
                i+=1

    def ts2(self,nums,target):
        m = {}
        for idx,num in enumerate(nums) :
            if target - num in m:
                return [m.get(target - num),idx]
            else:
                m[num] = idx
print(s().ts2([2,11,7,15],9))
a = {1:3,2:4}
