def f(n:int):
    for i in range(1,n):
        yield i


def find(idx, i):
    start = 10 ** i
    quo = idx // (i+1)
    rem = idx % (i+1)
    if rem == 0:
        return int(str(start + quo-1)[-1])
    else:
        return int(str(start + quo)[rem])

'''
对于每一个i位数，共有9 * 10**(i-1)*i个数字，这个公式是数数的核心
'''
def f(n:int) -> int:
    i,count = 0,0
    while True:
        cur = 9 * (10**i) * (i+1)
        count += cur
        if count >= n:
            idx = cur - (count - n) #figure out cur th
            return find(idx,i)
        i += 1

print(f(5))