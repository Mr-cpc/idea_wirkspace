import re
from functools import reduce

from basic.bupt_2017_10_19.Vec import Vec
from basic.bupt_2017_10_24 import egi


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
        self.mat = [[mat.mat[row][col] for col in range(len(mat.mat[0]))] for row in range(len(mat.mat))]

    def init_by_ndarray(self, ndarray):
        self.mat = ndarray[:]

    def rows(self):
        l = []
        for row in self.mat:
            l.append(Vec(row))
        return l
    def cols(self):
        # l = []
        # for col in range(len(self.mat[0])):
        #     l.append( ColVec( [self.mat[y][col] for y in range(len(self.mat))] ) )
        return self.transpose().rows()
    def construct_by_rows(rows):
        mat = Mat()
        for row in rows:
            mat.mat.append([x for x in row.data])
        return mat

    def conconstruct_by_cols(cols):
        return Mat.construct_by_rows(cols).transpose()

    def det(self):
        mat = self.lower_tri()
        res = 1
        for i in range(len(mat.mat)):
            res *= mat.mat[i][i]
        return res
    def upper_tri(self):
        mat = Mat()
        mat.mat = [[self.mat[row][col] for col in range(len(self.mat[0]))] for row in range(len(self.mat))]
        for i in range(len(self.mat[0])):
            self.check_pivot(i)
            for j in range(i+1,len(self.mat)):
                mat.mat[j] = [(mat.mat[j][k] - mat.mat[j][i] * mat.mat[i][k] / mat.mat[i][i]) for k in range(len(mat.mat[j]))]
        return mat

    def lower_tri(self):
        mat = Mat(ndarray=self.mat[:])
        for i in list(range(len(self.mat)))[::-1]:
            self.check_pivot(i,False)
            print(self.mat[i])
            for j in list(range(i))[::-1]:
                mat.mat[j] = [( mat.mat[j][k] -  mat.mat[j][i] *  mat.mat[i][k] /  mat.mat[i][i]) for k in range(len( mat.mat[j]))]
        return mat
    def transpose(self):
        mat = Mat()
        mat.mat = [[self.mat[col][row] for col in range(len(self.mat[0]))] for row in range(len(self.mat))]
        return mat


    def generateE(n):
        mat =  Mat()
        mat.mat = [[1 if col == row else 0 for col in range(n)] for row in range(n)]
        return mat

    def _leftMul(self,r_mat):
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

    def __mul__(self, other):
        if isinstance(other,Mat):
            return self._leftMul(other)
        elif isinstance(other,(int,float)):
            return Mat(ndarray=[[other * self.mat[row][col] for col in range(len(self.mat[0]))] for row in range(len(self.mat))])

    def __rmul__(self, other):
        if isinstance(other,Mat):
            return self._rightMul(other)
        elif isinstance(other,(int,float)):
            return Mat(ndarray=[[other * self.mat[row][col] for col in range(len(self.mat[0]))] for row in range(len(self.mat))])

    def __neg__(self):
        return Mat(ndarray=[[-self.mat[row][col] for col in range(len(self.mat[0]))] for row in range(len(self.mat))])

    def __add__(self, other):
        res = Mat(ndarray=[[self.mat[row][col] + other.mat[row][col] for col in range(len(self.mat[0]))] for row in range(len(self.mat))])
        return res
    def __sub__(self, other):
        return self + (-other)

    def _rightMul(self,l_mat):
        return l_mat.leftMul(self)

    def write(mat,filename):
        with open(filename,"w") as f:
            for row in mat:
                for col in row:
                    f.write(str(col))
                    f.write(" ")
                f.write("\n")

    def getRow(self,n):
        return Vec(self.mat[n][:])


    def getCol(self,n):
        return Vec([self.mat[row][n] for row in range(len(self.mat))])

    def dotprod(v1,v2):
        return reduce(lambda x,y:x+y,map(lambda x,y:x*y,v1,v2))

    def list_num_mul(v,num):
        return [ele * num for ele in v]
    def list_sub_list(v1,v2):
        for i in range(len(v1)):
            v1[i] -= v2[i]
    '''
    def orthogonal(self):
        ort = Mat()
        ort.mat = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for row in range(len(self.mat)):
            ort.mat[row] = self.mat[row][:]
            for i in range(row):
                Mat.list_sub_list(ort.mat[row],Mat.list_num_mul(ort.mat[i],Mat.dotprod(self.mat[row],ort.mat[i])/Mat.dotprod(ort.mat[i],ort.mat[i])))
        return ort
    '''
    def orth_by_col(self):
        col_vecs =self.cols()
        return Mat.conconstruct_by_cols(Vec.orthogonal(col_vecs))

    def orth_by_row(self):
        row_vecs =self.rows()
        return Mat.construct_by_rows(Vec.orthogonal(row_vecs))

    def egi_val(self):
        url = "http://www.yunsuanzi.com/cgi-bin/eigen_decomp.py"
        text = egi.send_to_ysz(self.mat,url)
        return egi.parse_egi_result(text)[0]

    def egi_vecs(self):
        url = "http://www.yunsuanzi.com/cgi-bin/eigen_decomp.py"
        text = egi.send_to_ysz(self.mat,url)
        return [Vec(vec) for vec in egi.parse_egi_result(text)[1]]
    def diagonal(self):
        vecs = self.egi_vecs()
        egi_mat = Mat(ndarray = [vec.data for vec in vecs]).transpose()
        return egi_mat.inv().leftMul(self).leftMul(egi_mat)
    def inv(self):
        if len(self.mat) == 0 or len(self.mat) != len(self.mat[0]):
            raise Exception("not a phalanx!")
        mat = Mat()
        E = Mat.generateE(len(self.mat)).mat
        argumented = [self.mat[row]+E[row] for row in range(len(self.mat))]
        for i in range(len(self.mat)):
            self.check_pivot(i)
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

    def __str__(self):
        str_self = ""
        for row in self.mat:
            str_self += " ".join([str(num) for num in row])
            str_self += "\n"
        return str_self

    def check_pivot(self,i,dire=True):
        if self.mat[i][i] != 0:
            return
        else :
            print("pivot == 0")
            j = 0
            for j in range(i+1,len(self.mat)) if dire else list(range(i))[::-1]:
                if(self.mat[j][i] != 0):
                    self.mat[i],self.mat[j] = self.mat[j],self.mat[i]
                    break
            if j == len(self.mat) if dire else j == -1:
                raise Exception("can't be inv")


# with open("mat.txt","w") as f:
#     for i in range(3):
#         f.write("1 2 3\n")
# mat = Mat("mat.txt")
# inv = mat.inv()
# Mat.write(inv.mat,"inv.txt")
# print(mat.rightMul(inv).mat)
# print(mat.diagonal())