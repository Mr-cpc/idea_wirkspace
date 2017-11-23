def check(matrix, i_st, j_st, i_en, j_en):
    for i in range(i_st, i_en + 1):
        if matrix[i][j_en] == "0":
            return False
    for j in range(j_st, j_en + 1):
        if matrix[i_en][j] == "0":
            return False
    return True


def mxsqa(matrix: list) -> int:
    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            else:
                x, y = 0, 0
                while i + x < len(matrix) and j + y < len(matrix[0]) and matrix[i + x][j] == matrix[i][j + y] == "1":
                    if check(matrix, i, j, i + x, j + y):
                        ans = max(ans, (x + 1) * (x + 1))
                        x += 1
                        y += 1
                    else:
                        break
    return ans


print(mxsqa([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]))
print(mxsqa([[]]))
