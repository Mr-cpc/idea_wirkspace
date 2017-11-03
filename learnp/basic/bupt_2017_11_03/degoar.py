def degoar(nums:list):
    m = {}
    for i in nums:
        m[i] = m.get(i,0)+1
    maxfrenum,maxfre = None,0
    for key in m:
        if m[key] > maxfre:
            maxfrenum,maxfre = key,m[key]
    candi = {key:[] for key in m if m[key] == maxfre}
    for i,num in enumerate(nums):
        if num in candi:
            candi[num].append(i)
    res = float("inf")
    for key in candi:
        res = min(res,candi[key][-1]-candi[key][0]+1)
    return res



nums =[1,2,2,3,1,4,2]
print(degoar(nums))

