def check(mt, i_st, j_st, i_en, j_en):
    for i in range(i_st, i_en + 1):
        if mt[i][j_en] == 0:
            return False
    for j in range(j_st, j_en + 1):
        if mt[i_en][j] == 0:
            return False
    return True


def mxsqa(mt: list) -> int:
    ans = 0
    for i in range(len(mt)):
        for j in range(len(mt[0])):
            if mt[i][j] == 0:
                continue
            else:
                x, y = 0, 0
                while i + x < len(mt) and j + y < len(mt[0]) and mt[i + x][j] == mt[i][j + y] == 1:
                    if check(mt, i, j, i + x, j + y):
                        ans = max(ans, (x + 1) * (x + 1))
                    x += 1
                    y += 1
    return ans


# print(mxsqa([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,1],]))
print(mxsqa([[]]))
