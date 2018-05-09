from sys import stdin
n = int(stdin.readline().strip())
max6 = n // 6
max8 = n // 8
ans = float('inf')
for i in range(1,max6+1):
    j = n - 6 * i
    if j < 0:
        continue
    elif j == 0:
        ans = min(ans,i)
    else:
        if j % 8 == 0:
            ans = min(ans,i + j // 8)
for i in range(1,max8+1):
    j = n - 8 * i
    if j < 0:
        continue
    elif j == 0:
        ans = min(ans,i)
    else:
        if j % 6 == 0:
            ans = min(ans,i + j // 6)
print(-1 if ans == float('inf') else ans)