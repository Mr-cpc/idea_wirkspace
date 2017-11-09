def negreel(nums1:list,nums2:list) ->list:
    ans = []
    for e1 in nums1:
        for idx,e2 in enumerate(nums2):
            if e1 == e2:
                for i in range(idx+1,len(nums2)):
                    if nums2[i] > e1:
                        ans.append(nums2[i])
                        break
                else:
                    ans.append(-1)

    return ans
