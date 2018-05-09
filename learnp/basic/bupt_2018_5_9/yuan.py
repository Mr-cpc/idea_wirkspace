from sys import stdin
from math import sqrt
def is_perfect_sqrt(n:int) -> bool:
    sq = int(sqrt(n))
    return sq * sq == n
r2 = int(stdin.readline().strip())
r = int(sqrt(r2))
ans = 0
for i in range(r+1):
    j = r2 - i*i
    if is_perfect_sqrt(j):
        if i != 0 and j != 0:
            ans += 4
        else:
            ans += 2
print(ans)