import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from basic.bupt_2017_11_28.type_deco import prt
import joblib
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from basic.bupt_2017_11_28.type_deco import prt
import seaborn as sns

'''
User:waiting
Date:2017-12-29
Time:15:00
'''
def shocomwo(licensePlate:str,words:list) -> str:
    from collections import Counter
    count_lic = Counter([ch.lower() for ch in licensePlate if ch.isalpha()])
    ans,least_time = None,float('inf')
    for word in words:
        cur_count = Counter(word.lower())
        for key,value in count_lic.items():
            if key not in cur_count:
                break
            elif cur_count[key] < value:
                break
            else:
                pass
        else:
            if len(word) < least_time:
                ans,least_time = word,len(word)
    return ans

print(shocomwo(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))
