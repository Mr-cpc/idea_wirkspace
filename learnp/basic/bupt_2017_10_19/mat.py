import re


class Mat:
    def __init__(self,filepath=""):
            try:
                with open(filepath) as f:
                    self.mat = [[int(num) for num in re.split("\\s+",line[:-1])] for line in f.readlines()]
            except FileNotFoundError:
                self.mat = []

    def transpose(self):
        mat = Mat()
        mat.mat = [[self.mat[col][row] for col in range(len(self.mat[0]))] for row in range(len(self.mat))]
        return mat


    def generateE(n):
        return [[1 if col == row else 0 for col in range(n)] for row in range(n)]


    def inv(self):
        if len(self.mat) == 0 or len(self.mat) != len(self.mat[0]):
            raise Exception("not a phalanx!")
        mat = Mat()
        E = Mat.generateE(len(self.mat))
        argumented = [self.mat[row]+E[row] for row in range(len(self.mat))]
        for i in range(len(self.mat[0])-1):
            for j in range(1,len(argumented)):
                argumented[j] = [argumented[j][i] -  self.mat[i][j]/self.mat[i][i] * argumented[j][i] for i in range(len(argumented[j]))]
        return [[argumented[row][col] for col in range(len(self.mat),len(argumented[0]))] for row in range(len(argumented))]

mat = Mat("mat.txt")
print(mat.mat)
print(mat.inv())