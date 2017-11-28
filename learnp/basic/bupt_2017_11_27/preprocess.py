import pandas as pd
from matplotlib.pyplot import *
df = pd.read_csv("tr.csv")
# df = df.loc[:,["Survived","Pclass","Name","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]]
df.pop("PassengerId")
df.pop("Ticket")
df.loc[df.Embarked.isnull(),"Embarked"] = "S"
df.insert()

# print(df[df.Embarked == df.Embarked.value_counts().max()])
print(df.count().Age)
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
# df.boxplot(column='Fare', by = 'Pclass')
# hist(df['Fare'], bins = 10, range =(df['Fare'].min(),df['Fare'].max()))
# title('Fare >distribution')
# xlabel('Fare')
# ylabel('Count of Passengers')
#如果变量是categorical的，想看distribution，则可以：
# df.Survived.value_counts().plot(kind='bar', figsize=(8,10))
#status var one-hot encoding;continonus var stardandlization
# x = df.Age.value_counts()
# print(x)
# show()
# print(data[data.isnull().values == True])