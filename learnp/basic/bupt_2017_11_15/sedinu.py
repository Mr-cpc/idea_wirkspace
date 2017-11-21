def sedinu(lower:int,upper:int) ->list:
    return [num for num in range(lower,upper+1) if ebi(num)]


def ebi(num:int) -> bool:
    cop = num
    while num > 0:
        x = num % 10
        if x % cop != 0:
            return False
        num = num // 10
    return True