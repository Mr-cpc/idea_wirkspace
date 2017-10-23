import re
from functools import reduce
from basic.bupt_2017_10_20.ColVec import ColVec
from basic.bupt_2017_10_20.RowVec import RowVec


class Mat:
    def __init__(self,filepath="",mat=None,ndarray=None):
        if filepath != "":
            self.init_by_file(filepath)
        elif mat != None:
            self.init_by_mat(mat)
        elif ndarray != None:
            self.init_by_ndarray(ndarray)
        else:
            self.mat = []

    def init_by_file(self,filepath):
        try:
            with open(filepath) as f:
                self.mat = [[float(num) for num in re.split("\\s+",line[:-1])] for line in f.readlines()]
        except FileNotFoundError:
            self.mat = []
    def init_by_mat(self, mat):
        self.mat = mat.mat[:]

    def init_by_ndarray(self, ndarray):
        self.mat = ndarray[:]

    def transpose(self):
        mat = Mat()
        mat.mat = [[self.mat[col][row] for col in range(len(self.mat[0]))] for row in range(len(self.mat))]
        return mat


    def generateE(n):
        mat =  Mat()
        mat.mat = [[1 if col == row else 0 for col in range(n)] for row in range(n)]
        return mat

    def leftMul(self,r_mat):
        if len(self.mat[0]) != len(r_mat.mat):
            raise Exception("the col not equals that row")
        mat = Mat()
        '''
        # mat.mat = [[0] * len(r_mat.mat[0])] * len(self.mat) !!!don't use this way to create a 2D Array
        '''
        mat.mat = [[0 for i in range(len(r_mat.mat[0]))] for j in range(len(self.mat)) ]
        # print(mat.mat)
        for i in range(len(self.mat)):
            for j in range(len(r_mat.mat[0])):
                for k in range(len(r_mat.mat)):
                    # print(str(k)+"mat["+str(i)+"]"+"["+str(j)+"]"+":"+str(mat.mat[i][j]))
                    mat.mat[i][j] += self.mat[i][k] * r_mat.mat[k][j]
        # mat.mat = [list(map(lambda x,y:x * y,self.mat[i],[mat[j][i] for j in len(mat)] )) for i in range(len(self.mat))]
        return mat

    def rightMul(self,l_mat):
        return l_mat.leftMul(self)

    def write(mat,filename):
        with open(filename,"w") as f:
            for row in mat:
                for col in row:
                    f.write(str(col))
                    f.write(" ")
                f.write("\n")

    def getRow(self,n):
        return RowVec(self.mat[n][:])


    def getCol(self,n):
        return ColVec([self.mat[row][n] for row in range(len(self.mat))])

    def dotprod(v1,v2):
        return reduce(lambda x,y:x+y,map(lambda x,y:x*y,v1,v2))

    def list_num_mul(v,num):
        return [ele * num for ele in v]
    def list_sub_list(v1,v2):
        for i in range(len(v1)):
            v1[i] -= v2[i]
    def orthogonal(self):
        ort = Mat()
        ort.mat = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for row in range(len(self.mat)):
            ort.mat[row] = self.mat[row][:]
            print(ort.mat[row])
            for i in range(row):
                Mat.list_sub_list(ort.mat[row],Mat.list_num_mul(ort.mat[i],Mat.dotprod(self.mat[row],ort.mat[i])/Mat.dotprod(ort.mat[i],ort.mat[i])))
            print(ort.mat[row])
        return ort
    def inv(self):
        if len(self.mat) == 0 or len(self.mat) != len(self.mat[0]):
            raise Exception("not a phalanx!")
        mat = Mat()
        E = Mat.generateE(len(self.mat)).mat
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
            argumented[i] = [argumented[i][j] / argumented[i][i] for j in range(len(argumented[i]))]
            ''' for i in range(len(argumented)):
                    for j in range(len(argumented[i])):
                        argumented[i][j] /= argumented[i][i]  this is wrong excepte argumented[i][0] is 1, argumented[i][1]~argumented[i][len]won't change
            '''
        Mat.write(argumented,"argu.txt")
        mat.mat = [[argumented[row][col] for col in range(len(self.mat),len(argumented[0]))] for row in range(len(argumented))]
        return mat

# with open("mat.txt","w") as f:
#     for i in range(3):
#         f.write("1 2 3\n")
mat = Mat("mat.txt")
# inv = mat.inv()
# Mat.write(inv.mat,"inv.txt")
# print(mat.rightMul(inv).mat)
print(mat.orthogonal().mat)