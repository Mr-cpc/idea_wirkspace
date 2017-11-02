from math import sqrt
import heapq
from basic.bupt_2017_10_19.Vec import Vec


class kn:
    def __init__(self,datas:list,k:int):
        self.datas = [Vec(data[:-1]) for data in datas]
        Vec.sta(self.datas)
        self.lab = {self.datas[i]:datas[i][-1] for i in range(len(datas))}
        self.k = int(sqrt(len(datas))) if k > sqrt(len(datas)) else k

    def predict(self,sam:list):
        sam = Vec(sam)
        dis_dict = {}
        for data in self.datas:
            dis = sam.distance(data)
            if dis not in dis_dict:
                dis_dict[dis] = [data]
            else :
                dis_dict[dis].append(data)
        largest_dis = heapq.nlargest(self.k,dis_dict.keys())
        kn_datas = []
        for dis in largest_dis:
            kn_datas.extend(dis_dict[dis])
            if len(kn_datas) >= self.k:
                break
        fre = {}
        for data in kn_datas:
            fre[self.lab[data]] = fre.get(self.lab[data],0)+1
        lab,max_fre = None,0
        for k in fre:
            if fre[k] > max_fre:
                lab,max_fre = k,fre[k]
        return lab



