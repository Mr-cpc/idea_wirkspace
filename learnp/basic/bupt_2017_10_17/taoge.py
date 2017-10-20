def n_perm(res,source,cur,n):
    if n == 0:
        res.append(cur)
        return
    else:
        source_copy = source[:]
        for num in source:
            cur.append(num)
            source_copy.remove(num)
            n_perm(res,source_copy,cur[:],n-1)
            source_copy.append(num)
            cur.remove(num)

def perm_n(source,n):
    res = []
    n_perm(res,source,[],n)
    return res

def check(first_line,sec_line):
    for i in range(len(first_line)):
        if first_line[i] > sec_line[i]:
            return False
    return True

def is_asc(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

nums = list(range(1,13))
perms = perm_n(nums,6)
perms = [perm for perm in perms if is_asc(perm)]
ans = 0
set_nums = set(nums)
f = open("result.txt","w")
for perm in perms:
    sec_line = list(set_nums.difference(set(perm)))
    sec_line_perms = perm_n(sec_line,len(sec_line))
    for sec_lin in sec_line_perms:
        if not is_asc(sec_lin):
            continue
        if check(perm,sec_lin):
            f.write("----result-----")
            f.write("\n")
            f.write(str(perm))
            f.write("\n")
            f.write(str(sec_lin))
            f.write("\n")
            ans += 1
f.close()
print(ans)