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

print(triag([[2],[3,4],[6,5,7],[4,1,3,8]]))

