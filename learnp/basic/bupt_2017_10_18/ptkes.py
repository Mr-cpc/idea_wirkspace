def comb_n(res,nums,cur,n):
    if n == 0:
        res.append(cur)
    else :
        num_copy = nums[:]
        for num in nums:
            cur.append(num)
            num_copy.remove(num)
            comb_n(res,num_copy,cur[:],n-1)
            cur.remove(num)



def n_comb(nums,n):
    res = []
    comb_n(res,nums,[],n)
    return res

def count_k_parti(n,k):
    if k == 1 or n == k:
        return 1
    elif k < 0 or n < k:
        return 0
    else:
        return k * count_k_parti(n-1,k) + count_k_parti(n-1,k-1)


def contigious_parti_k(res,cur,nums,k):
    if k == 1:
        cur.append(nums)
        res.append(cur)
        return
    elif len(nums) < k:
        return
    else:
        for i in range(len(nums)-1):
            cur.append(nums[:i+1])
            contigious_parti_k(res,cur[:],nums[i+1:],k-1)
            cur.remove(nums[:i+1])
    pass

def contigious_k_parti(nums,k):
    res = []
    contigious_parti_k(res,[],nums,k)
    return res

def k_parti(nums,k):
    if k == 1:
        return [nums]

    elif len(nums) == k:
        return [[num] for num in nums]

    else:
        choose = nums[0]
        part1 = k_parti(nums[1:],k-1)
        res1 = map(lambda l:l.append(choose),part1)


res = contigious_k_parti([1,2,3,4],2)
a = [[1,2],[1,2,3]]
b = [1,2]
print(count_k_parti(4,2))
