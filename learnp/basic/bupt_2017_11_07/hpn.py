def ishpn(n:int) ->bool:
    s = set()
    while True:
        nums = [int(x) for x in str(n)]
        last_n = n
        s.add(n)
        n = sum(num ** 2 for num in nums)
        if n == 1:
            break
        elif n == last_n:
            return False
        elif n in s:
            return False
    return True

print(ishpn(2))