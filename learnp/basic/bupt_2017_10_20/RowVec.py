from functools import reduce

from basic.bupt_2017_10_20.Vec import Vec


class RowVec(Vec):
    def mul(self,vec):
        return reduce(lambda x,y:x+y,list(map(lambda x,y:x*y,self.data,vec.data)))