import re

'''
User:waiting
Date:2017-12-04
Time:14:20
'''


class Property:
    def __init__(self, path: str, sep: str = '='):
        self.d = {}
        with open(path,encoding='utf-8') as f:
            key_vals = map(lambda x: re.sub(r'\s+', '', x), f.readlines())
            self.d = {key_val.split(sep,1)[0]: key_val.split(sep,1)[1] for key_val in key_vals if key_val != ''}

    def __getitem__(self, item):
        return self.d[item]

    def __iter__(self):
        return iter(self.d)

    def items(self):
        return self.d.items()
if __name__ == '__main__':
    ppt = Property(r'G:\idea_wirkspace\learnp\basic\bupt_2018_1_17\serverid.properties')
    for x in ppt:
        print(x)