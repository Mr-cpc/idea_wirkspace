from sys import stdin
# d = {i:str(i) for i in range(10)}
# ord_A = ord('A')
# for i in range(6):
#     d[i+10] = chr(ord_A + i)
d = "0123456789ABCDEF"
def transfer(M:int,N:int):
    if M == 0:
        print(0)
        return
    stk = []
    while M != 0:
        stk.append(M % N)
        M //= N
    ans = []
    print("".join(d[stk[i]] for i in range(len(stk)-1,-1,-1)))
M,N = [int(ele) for ele in stdin.readline().strip().split(' ')]
transfer(M,N)
