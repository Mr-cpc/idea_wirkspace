import math

def gen(x):
    while x > 0:
        yield x
        x -= 1
def lapapro(n:int)->int:
    x = int(math.pow(10,n)) - 1
    for i in gen(x):
        for j in gen(x):
            num = str(i * j)
            if num==num[::-1]:
                return int(num) % 1337

print(lapapro(2))
