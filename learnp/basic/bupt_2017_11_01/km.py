import random

from basic.bupt_2017_10_19.Vec import Vec


class Km:
    '''
    1.初始化centroid
    2.对dataset中每个sample求到各个centroid的距离，将距离最小的那个centroid作为该sample的类别
    3.更新每个类别的centroid(通过求该类别所有sample的算术平均)，若质心几乎无变化，则完成;否则，返回2
    '''
    def __init__(self,k,datas):
        self.datas = [Vec(data[:-1]) for data in datas]
        self.lab = {self.datas[i]:datas[i][-1] for i in range(len(datas))}
        Vec.sta(self.datas)
        # ini_centers = [self.datas[random.randint(0,len(self.datas)-1)] for i in range(k)]
        ini_centers = random.sample(self.datas,k)
        while 1:
            ini_cls = {cent:[] for cent in ini_centers}
            for data in self.datas:
                sho_dis, cls = float("inf"),None
                for cent in ini_centers:
                    dis = data.distance(cent)
                    if dis < sho_dis:
                        sho_dis,cls = dis,cent
                ini_cls[cls].append(data)

            new_centers = [Vec.get_clustercenter(ini_cls[key]) for key in ini_cls]
            if Vec.is_converg(ini_centers,new_centers,1e-5):
                self.cls = ini_cls
                break
            else:
                ini_centers = new_centers


