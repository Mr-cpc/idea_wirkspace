from basic.bupt_2017_10_19.mat import Mat
from basic.bupt_2017_10_20.ColVec import ColVec
from basic.bupt_2017_10_20.RowVec import RowVec

u = Mat("u.txt")
v = Mat("v.txt")
s = Mat("E.txt")

u_col = u.getCol(0)
v_col = v.getCol(0)
print(s.leftMul(Mat(v_col.data)))