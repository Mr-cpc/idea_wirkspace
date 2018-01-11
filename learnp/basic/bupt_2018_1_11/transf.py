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
Date:2018-01-11
Time:16:54
'''
def transf(query_str:str):
    import re
    query_str =  re.sub(r'&',r',',query_str)
    query_str =  re.sub(r'=',r':',query_str)
    query_str = re.sub(r'([a-zA-Z0-9%_]*)(:)([a-zA-Z0-9%_.\-]*)',r'"\1"\2"\3"',query_str)
    return query_str

print(transf('orderby=selling_time%20DESC&act=super_query&search_type=overall_lingshi_search&equip_level_min=80&equip_level_max=100&kindid=61&damage=1&added_attr_logic=and&added_attr=2&added_attr_repeat_num=2&server_type=3&page=8&platform=ios&app_version=2.3.2&device_name=My%20iPhone&os_name=iPhone%20OS&os_version=9.3.3&device_id=10272229-E368-4457-95B9-427D8EEDA461'))
a = 'http://xyq-ios2.cbg.163.com/app2-cgi-bin//xyq_search.py?orderby=selling_time%2520DESC&act=super_query&search_type=overall_lingshi_search&equip_level_min=80&equip_level_max=100&kindid=61&damage=1&added_attr_logic=and&added_attr=2&added_attr_repeat_num=2&server_type=3&page=8&platform=ios&app_version=2.3.2&device_name=My%2520iPhone&os_name=iPhone%2520OS&os_version=9.3.3&device_id=10272229-E368-4457-95B9-427D8EEDA461'
b = 'http://xyq-ios2.cbg.163.com/app2-cgi-bin//xyq_search.py?orderby=selling_time%20DESC&act=super_query&search_type=overall_lingshi_search&equip_level_min=80&equip_level_max=100&kindid=61&damage=1&added_attr_logic=and&added_attr=2&added_attr_repeat_num=2&server_type=3&page=8&platform=ios&app_version=2.3.2&device_name=My%20iPhone&os_name=iPhone%20OS&os_version=9.3.3&device_id=10272229-E368-4457-95B9-427D8EEDA461'
print(a == b )