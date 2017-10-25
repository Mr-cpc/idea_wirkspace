import math
from functools import reduce


# def info(p:float) -> float:
#     return -p * math.log(p, 2)

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
            self.flag = True
            print(datas)
        else:
            print(datas)
            self.m = {}
            self.info = 0
            self.datas = datas[:]
            for d in datas:
                self.m[d[-1]] = self.m.get(d[-1],0)+1
            for key in self.m:
                self.info += cal_info(self.m[key]/len(datas))
            max_info,max_info_i = (float("-inf"),None),0
            for i in range(len(datas[0])-1):
                info_i = self.fea_info(i)
                gain = self.info - info_i[0]
                # print(gain)
                if gain > max_info[0]:
                    max_info,max_info_i = (gain,info_i[1]),i
            self.parti_fea = max_info_i
            for key in max_info[1]:
                max_info[1][key] = []
            for i in range(len(datas)):
                max_info[1][datas[i][max_info_i]].append(datas[i][:max_info_i]+datas[i][max_info_i+1:])
            # print(max_info_i)

            # print(max_info[0])
            self.sub = []
            for key in max_info[1]:
                # print(max_info[1][key])
                self.sub.append(Decis(max_info[1][key]))
            # max_info[1]

        #     self.l.append(m)
        # for m in self.l:
        #     sum_ = reduce(lambda x,y:x+y,m.itervalues())
        #     info = 0
        #     for key in m:
        #         info += info(m[key]/sum_)
        #     self.info.append(info)
    def train(self):
        pass

def read():
    with open("a.txt") as f:
        return [d[:-1].split(" ") for d in f.readlines()]

decs = Decis(read())
# print(decs.flag)

