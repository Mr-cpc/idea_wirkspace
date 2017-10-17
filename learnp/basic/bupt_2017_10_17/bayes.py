import re

class Bayes:
    def __init__(self,points):
        self.points = points[:] #samples like [x1,x2,x3,...,xn,y]
        self.freq = {} #class's frequence
        self.cls_lists = {} #y coresponding x like {y1:[sample_1,sample_2],y2:[sample_1,..sample_n],...,yn:[...]}
        for point in points:
            self.freq[point[-1]] = self.freq.get(point[-1],0)+1
            list = self.cls_lists.get(point[-1],[])
            list.append(point[:-1])
            self.cls_lists[point[-1]] = list

    def train(self):
        self.p_y = {key:self.freq[key]/len(self.points) for key in self.freq}
        self.y_xpery = {}
        for key ,val in self.cls_lists.items():
            xfreq_per_y = {}
            for sample in val:
                for x in sample:
                    xfreq_per_y[x] = xfreq_per_y.get(x,0)+1
            self.y_xpery[key] = {k:xfreq_per_y[k]/len(val) for k in xfreq_per_y}

    def predict(self,sample):
        mx = ("1",0)
        for point in self.points:
            p = self.p_y[point[-1]]
            for x in sample:
                p *= self.y_xpery[point[-1]].get(x,0)
            if p > mx[1]:
                mx = (point[-1],p)
        return mx
#例题网址 http://www.ruanyifeng.com/blog/2013/12/naive_bayes_classifier.html
with open("result.txt",encoding="utf-8") as f:
    datas = [re.split("\\s+",data[:-1]) for data in f.readlines()]
    bayes = Bayes(datas)
# print(datas)
bayes.train()
# print(str(bayes.p_y))
# print(bayes.cls_lists)
print(bayes.y_xpery)
print(bayes.predict(["打喷嚏","建筑工人"]))