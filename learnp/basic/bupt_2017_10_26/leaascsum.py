def leaascs(s1,s2):
    m1,m2 = {},{}
    l1,l2 = [],[]
    res = 0
    for ch in s1:
        if ch not in m1:
            l1.append(ch)
        m1[ch] = m1.get(ch,0)+1
    for ch in s2:
        if ch not in m2:
            l2.append(ch)
        m2[ch] = m2.get(ch,0)+1
    for key in m1:
        m1_val = m1[key]
        m2_val = m2.get(key)
        if m2_val == None:
            res += ord(key) * m1_val
            l1.remove(key)
    for key in m2:
        m2_val = m2[key]
        m1_val = m1.get(key)
        if m1_val == None:
            res += ord(key) * m2_val
            l2.remove(key)
    m1 = {key:m1[key] for key in l1}
    m2 = {key:m2[key] for key in l2}
    return res,m1,m2

res = leaascs("delete","leet")
print(res[1])

print(res[2])