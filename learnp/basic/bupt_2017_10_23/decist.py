import math
from functools import reduce

cal_info = lambda p:-p * math.log(p, 2)

class Decis:
    def fea_info(self,i: int) -> (float,dict):
        m = {}
        datas = self.datas
        for data in datas:
            m[data[i]] = m.get(data[i],0)+1
        sum_info = 0
        for key in m:
            x = {}
            for data in datas:
                if data[i] == key:
                    x[data[-1]] = x.get(data[-1],0)+1
            sum_ = reduce(lambda x,y:x+y,x.values())
            inf = 0
            for k in x:
                inf += m[key]/len(datas)*cal_info(x[k]/sum_)
            sum_info += inf
        return sum_info,m
    def __init__(self,datas:list):
        if len(datas[0]) == 1:
            mm = {}
            for data in datas:
                # print(data[0])
                # a = mm.get(data[0],0)+1
                # mm[data[0]] = a
                mm[data[0]] = mm.get(data[0],0)+1
            max_cls,max_num = None,float("-inf")
            for key in mm:
                if mm[key] > max_num:
                    max_cls,max_num = key,mm[key]
            self.cls = max_cls
            # print(datas)
        else:
            # print(datas)
            self.m = {}
            self.info = 0
            self.datas = datas[:]
            for d in datas:
                self.m[d[-1]] = self.m.get(d[-1],0)+1
            if len(self.m) == 1:
                self.cls = list(self.m.keys())[0]
                return
            for key in self.m:
                self.info += cal_info(self.m[key]/len(datas))
            max_info,max_info_i = (float("-inf"),None),0
            for i in range(len(datas[0])-1):
                info_i = self.fea_info(i)
                gain = self.info - info_i[0]
                if gain > max_info[0]:
                    max_info,max_info_i = (gain,info_i[1]),i
            self.parti_fea = max_info_i
            for key in max_info[1]:
                max_info[1][key] = []
            for i in range(len(datas)):
                max_info[1][datas[i][max_info_i]].append(datas[i][:max_info_i]+datas[i][max_info_i+1:])

            self.sub = []
            self.fea_map = {}
            for key in max_info[1]:
                self.sub.append(Decis(max_info[1][key]))
                self.fea_map[key] = self.sub[-1]
    def predict(self,sam):
        if hasattr(self,"cls"):
            return self.cls
        else:
            return self.fea_map[sam[self.parti_fea]].predict(sam[:self.parti_fea]+sam[self.parti_fea+1:])

def read():
    with open("a.txt") as f:
        return [d[:-1].split(" ") for d in f.readlines()]


def flat(decs:Decis,res:list):
    if hasattr(decs,"sub"):
        res.append(decs.datas)
        for d in decs.sub:
            flat(d,res)


def read_labels():
    with open("l.txt") as f:
        return [d for d in f.readline().split(" ")]


decs = Decis(read())
print( decs.predict(read_labels()))
# read_labels()

