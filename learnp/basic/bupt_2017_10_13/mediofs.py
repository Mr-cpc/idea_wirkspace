#no.4

#suppose and guarantee always len(nums1) <= len(nums2)
def me(nums1,nums2,k):
    if len(nums1) == 0:
        return nums2[k-1]
    elif k == 1:
        return nums1[0] if nums1[0] <= nums2[0] else nums2[0]
    else:
        mid = (k >> 1) - 1
        if len(nums1) <= mid:
            return nums2[k - len(nums1)]
        else:
            if nums1[mid] <= nums2[mid]:
                return me(nums1[mid+1:],nums2,k-(k >> 1))
            else:
                new_len = len(nums2) - (k >> 1)
                return me(nums2[mid+1:],nums1,k - (k >> 1)) if new_len <= len(nums1) else me(nums1,nums2[mid+1:],k - (k >> 1))

def findme(nums1,nums2):
    length = len(nums1) + len(nums2)
    nums1,nums2 = (nums2,nums1) if len(nums2) <= len(nums1) else (nums1,nums2)
    if length & 0x1 == 1:
        return me(nums1,nums2,length // 2 + 1)
    else:
        return (me(nums1,nums2,length//2) + me(nums1,nums2,length//2 + 1)) / 2

# print(me([3,5],[1,2,4],3))
print(findme([3,5,6],[1,2,4]))