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

    def leftMul(self,mat):
        if len(self.mat[0]) != len(mat.mat):
            raise Exception("the col not equals that row")
        # for i in range(len())
    def write(mat,filename):
        with open(filename,"w") as f:
            for row in mat:
                for col in row:
                    f.write(str(col))
                    f.write(" ")
                f.write("\n")

    def inv(self):
        if len(self.mat) == 0 or len(self.mat) != len(self.mat[0]):
            raise Exception("not a phalanx!")
        mat = Mat()
        E = Mat.generateE(len(self.mat))
        argumented = [self.mat[row]+E[row] for row in range(len(self.mat))]
        for i in range(len(self.mat)):
            for j in range(i+1,len(self.mat)):
                # for k in range(len(argumented[j])):
                #     argumented[j][k] -= argumented[j][i] * argumented[i][k] /argumented[i][i]
                argumented[j] = [(argumented[j][k] - argumented[j][i] * argumented[i][k] / argumented[i][i]) for k in range(len(argumented[j]))]
        for i in list(range(len(self.mat)))[::-1]:
            for j in list(range(i))[::-1]:
                argumented[j] = [(argumented[j][k] - argumented[j][i] * argumented[i][k] / argumented[i][i]) for k in range(len(argumented[j]))]
        for i in range(len(argumented)):
            for j in range(len(argumented[i])):
                argumented[i][j] /= argumented[i][i]
        Mat.write(argumented,"argu.txt")
        mat.mat = [[argumented[row][col] for col in range(len(self.mat),len(argumented[0]))] for row in range(len(argumented))]
        return mat

# with open("mat.txt","w") as f:
#     for i in range(3):
#         f.write("1 2 3\n")
mat = Mat("mat.txt")
print(mat.inv().mat)