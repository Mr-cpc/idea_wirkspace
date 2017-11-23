def dfs(grid,pos,cur, visits):
    if pos in visits:
        return
    elif not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
        return
    elif grid[pos[0]][pos[1]] == 0:
        return
    else:
        cur.append(pos)
        visits.add(pos)
        for i in (-1,1):
            dfs(grid,(pos[0]+i,pos[1]),cur,visits)
            dfs(grid,(pos[0],pos[1]+i),cur,visits)


def nuofis(grid:list):
    isls = []
    visits = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in visits:
                continue
            elif grid[i][j] == 0:
                continue
            else:
                cur = []
                dfs(grid,(i,j),cur,visits)
                isls.append(cur)
    return len(isls)


print(nuofis([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))