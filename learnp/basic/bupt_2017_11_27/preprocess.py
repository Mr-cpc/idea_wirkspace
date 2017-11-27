import pandas as pd
from matplotlib.pyplot import *
df = pd.read_csv("tr.csv")
# print(data.info())
# print(data.describe())
# 看有多少取值
# x = data.SibSp.unique()
# 看有哪些空值
# x = data.loc[data.Cabin.isnull(),"Cabin"]
# print(x)
# print(type(x))
# 查看feature之间的关联
# temp = pd.crosstab([df.Pclass, df.Sex], df.Survived.astype(bool))
# temp.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)
df.boxplot(column='Fare', by = 'Pclass')
plt.hist(df['Fare'], bins = 10, range =(df['Fare'].min(),df['Fare'].max()))
plt.title('Fare >distribution')
plt.xlabel('Fare')
plt.ylabel('Count of Passengers')
#如果变量是categorical的，想看distribution，则可以：
df.PdDistrict.value_counts().plot(kind='bar', figsize=(8,10))

show()
# print(data[data.isnull().values == True])