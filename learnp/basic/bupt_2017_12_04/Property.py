import re


'''
User:waiting
Date:2017-12-04
Time:14:20
'''


class Property:
    def __init__(self, path: str,sep: str = '='):
        self.d = {}
        with open(path) as f:
            key_vals = f.readlines()
            for key_val in key_vals:
                key_val = re.sub(r'\s+', '', key_val)
                if key_val != '':
                    key_val = key_val.split(sep)
                    self.d[key_val[0]] = key_val[1]

    def __getitem__(self, item):
        return self.d[item]

