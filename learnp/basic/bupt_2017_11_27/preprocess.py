import pandas as pd
from matplotlib.pyplot import *
data = pd.read_csv("tr.csv")
# print(data.info())
# print(data.describe())
x = data.Survived.value_counts()
print(type(x))
x.plot(kind = "pie")
show()
# print(data[data.isnull().values == True])