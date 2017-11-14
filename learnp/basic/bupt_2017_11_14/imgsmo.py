def imgsmo(M:list) ->list:
    ans = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            sum,count = 0,0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= i+x < len(M) and 0 <= j+y < len(M[0]):
                        sum += M[i+x][j+y]
                        count += 1
            ans[i][j] = sum // count
    return ans
print(imgsmo([[1,1,1],[1,0,1],[1,1,1]]))