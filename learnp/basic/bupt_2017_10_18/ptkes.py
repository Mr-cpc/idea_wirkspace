from functools import reduce

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


def canbe(nums, k, group,target):
    if group == target:
        return True
    elif len(nums) == 0:
        return False
    else:
        nums_copy = nums[:]
        pass


def print_secondstiring(filename,n):
    with open(filename,"w",encoding="utf-8") as f:
        for i in range(1,n+1):
            f.write("---------------------------------\n")
            f.write(str(i)+"'s all partition\n")
            f.write("----------------\n")
            for j in range(1,i+1):
                f.write(str(i)+"'s"+str(j)+"partition:"+str(count_k_parti(i,j)))
                f.write("\n")
            f.write("---------------------------------\n")
def canbekequparti(nums,k):
    nums_sum = reduce(lambda x,y:x+y,nums,0)
    if nums_sum % k != 0:
        return False
    else:
        return canbe(nums,k,[0]*k,[nums_sum // k]*k)

# res = contigious_k_parti([1,2,3,4],2)
# a = [[1,2],[1,2,3]]
# b = [1,2]
# print_secondstiring("second_stiring.txt",10)
# print(count_k_parti(25,10))
