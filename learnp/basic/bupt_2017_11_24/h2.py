def h2(citations:list) -> int:
    l,r = 0 ,len(citations)-1
    while l < r:
        mid = l + ((r-l) >> 1)
        if citations[mid] >= len(citations) - mid:
            if mid - 1 >= 0 and citations[mid - 1] < citations[mid]:
                return len(citations) - mid
            else:
                r = mid - 1
        else:
            l = mid + 1
    return len(citations) - l

print(h2([8]))