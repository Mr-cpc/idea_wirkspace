#for previous line ith, the next line's i and i+1 are reachable


def triag(triangle:list) -> int:
    if not len(triangle):
        return 0
    candi = [float("inf")]
    dfs(triangle,0,0,candi,0)
    return candi[0]

def dfs(trg:list,row:int,col:int,candi:list,cur_sum:int):
        if row == len(trg):
            if cur_sum < candi[0]:
                candi[0] = cur_sum
        else:
            dfs(trg,row+1,col,candi,cur_sum+trg[row][col])
            dfs(trg,row+1,col+1,candi,cur_sum+trg[row][col])

def triag2(triangle:list)->int:
    dp = [[float('inf')] * (len(triangle[-1])) for i in range(len(triangle))]
    i = len(dp) - 1
    for j in range(len(dp[-1])):
        dp[i][j] = triangle[i][j]
    for i in range(len(dp)-2,-1,-1):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
    return dp[0][0]















print(triag2([[2],[3,4],[6,5,7],[4,1,3,8]]))

