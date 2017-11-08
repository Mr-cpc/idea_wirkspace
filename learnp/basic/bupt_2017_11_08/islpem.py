def dfs(grid:list, pos:tuple, s:set):
    if not (0 <= pos[0] <len(grid) and 0 <= pos[1] < len(grid[0])):
        return
    elif pos in s:
        return
    elif grid[pos[0]][pos[1]] == 1:
        s.add(pos)
        for i in (-1,1):
            dfs(grid,(pos[0]+i,pos[1]),s)
        for i in (-1,1):
            dfs(grid,(pos[0],pos[1]+i),s)

def islpem(grid:list) ->int:
    if len(grid) == 0:
        return 0
    s = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                dfs(grid,(i,j),s)
                break
    return len(s) * 2 + 2

g = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(len(islpem(g)))