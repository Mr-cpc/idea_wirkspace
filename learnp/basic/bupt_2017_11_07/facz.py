from basic.bupt_2017_11_07 import f


def facz(n:int) -> int:
    res,exp = 0,1
    while True:
        quo = n // (5 ** exp)
        if quo == 0 :
            break
        else:
            res += quo
            exp += 1
    return res

def x(n):
    print(f(n))
    print(facz(n))


x(0)