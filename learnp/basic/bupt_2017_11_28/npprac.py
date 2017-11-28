import numpy as np
import pandas as pd
''',index=list("asc")'''
# s = pd.Series([1,2,3])
# print(s[1:]+s[:-1])
# print(s.cov(s))
# d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
#      'two' : pd.Series([1., 2., 3., 4.], index=['e', 'f', 'g', 'd'])}
# df = pd.DataFrame(d)
# print(df.index.value_counts())
# print(df.columns)
d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}
df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'],columns=["one","two","three"])
df2 = df.loc['a']
print(type(df2))