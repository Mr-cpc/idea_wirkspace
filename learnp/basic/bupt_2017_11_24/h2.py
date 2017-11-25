def h2(citations:list) -> int:
    if [0] * len(citations) == citations: #下面的二分解决不了全0的情况，这里单独判断
        return 0
    l,r = 0 ,len(citations)-1
    while l < r:
        mid = l + ((r-l) >> 1)
        if citations[mid] == len(citations) - mid:
            return len(citations) - mid
        elif citations[mid] < len(citations) - mid:
            l = mid + 1
        else:
            r = mid #为什么不是r = mid-1,是为了像[1,2,4,9,10]这样的输入mid不被跳过
    return len(citations) - l

print(h2([0,0]))
