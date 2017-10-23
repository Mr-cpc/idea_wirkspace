from basic.bupt_2017_10_19.mat import Mat
from basic.bupt_2017_10_20.ColVec import ColVec
from basic.bupt_2017_10_20.RowVec import RowVec
from basic.bupt_2017_10_20.Vec import Vec

u = Mat("u.txt")
v = Mat("v.txt")
s = Mat("E.txt")

vecs = [vec.norm() for vec in  Vec.orthogonal(Mat("mat.txt").rows())]
print(vecs[2])