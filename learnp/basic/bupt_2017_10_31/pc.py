from basic.bupt_2017_10_19.mat import Mat
import copy
class Pc:
    def __init__(self,mat:Mat):
        self.mat = copy.deepcopy(mat.transpose())
        self.mat = Mat(ndarray=[[self.mat.mat[row][col] - sum(self.mat.mat[row]) / len(mat.mat) for col in range(len(self.mat.mat[0]))] for row in range(len(self.mat.mat))])
        self.cov_mat = self.mat * self.mat.transpose() / len(mat.mat)
        self.egi_val = self.cov_mat.egi_val()
        self.p = Mat.conconstruct_by_cols(self.cov_mat.egi_vecs())
data = Mat(filepath="pc.txt")
pc = Pc(data)
e = 5 * Mat.generateE(3)
# print(e/5)
print(pc.egi_val)
print(pc.p[:1]*data.transpose())