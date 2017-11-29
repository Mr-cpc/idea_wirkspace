import pandas as pd
from sklearn.model_selection import train_test_split

from basic.bupt_2017_11_28.type_deco import *
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression as lr

df = pd.read_csv("tr.csv")
# df = df.loc[:,["Survived","Pclass","Name","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]]
df.pop("PassengerId")
df.pop("Ticket")
df.pop('Name')
# for i in range(len(df.columns)):
#     if df.iloc[:,i].count() != len(df.index):
#         x = df.iloc[:,[i]]
#         df.iloc[:,[i]] = x.median()
# prt(df)
# print(len(df.loc[(df['Sex'] == 'female')])) 314
# print(len(df.loc[(df['Sex'] == 'female') & (df['Survived'] == 1)])) 233
# print(len(df.loc[(df['Age'] >= 50) & (df['Sex'] == 'female')])) 22
# print(len(df.loc[(df['Age'] >= 50) & (df['Sex'] == 'female') & (df['Survived'] == 1)])) 20
df.loc[df['Cabin'].isnull(),'Cabin'] = 0
df.loc[-(df['Cabin'].isnull()),'Cabin'] = 1
df.loc[df['Age'].isnull(),'Age'] = df['Age'].median()
df.loc[df['Sex'] == 'male','Sex'] = 1
df.loc[df['Sex'] == 'female','Sex'] = 0
# x = df['Age'].value_counts().index
# for i in x:
#     prt(i)
df.loc[df['Embarked'] == 'Q','Embarked'] = 0
df.loc[df['Embarked'] == 'S','Embarked'] = 1
df.loc[df['Embarked'] == 'C','Embarked'] = 2
df.loc[df['Embarked'].isnull(),'Embarked'] = df['Embarked'].value_counts().index[0]
# prt(df)
# x = pd.get_dummies(df['Embarked'])
# prt(x.join(df['Embarked']))
df_te = pd.read_csv("test.csv")
df_te.pop("PassengerId")
df_te.pop("Ticket")
df_te.pop('Name')
df_te.loc[df_te['Cabin'].isnull(),'Cabin'] = 0
df_te.loc[-(df_te['Cabin'].isnull()),'Cabin'] = 1
df_te.loc[df_te['Age'].isnull(),'Age'] = df_te['Age'].median()
df_te.loc[df_te['Sex'] == 'male','Sex'] = 1
df_te.loc[df_te['Sex'] == 'female','Sex'] = 0
df_te.loc[df_te['Embarked'] == 'Q','Embarked'] = 0
df_te.loc[df_te['Embarked'] == 'S','Embarked'] = 1
df_te.loc[df_te['Embarked'] == 'C','Embarked'] = 2
df_te.loc[df_te['Embarked'].isnull(),'Embarked'] = df_te['Embarked'].value_counts().index[0]
df_te.loc[df_te['Fare'].isnull(),'Fare'] = df_te['Fare'].median()
x_tr,x_te,y_tr,y_te = train_test_split(df.iloc[:,1:],df['Survived'],random_state=1)
clf = lr()
clf.fit(x_tr,y_tr)
y_pre = clf.predict([df_te.loc[i] for i in range(len(df_te))])
with open("ans.txt","w") as f:
    for i in range(len(y_pre)):
        f.write("{},{}".format(i+892,y_pre[i]))
        f.write('\n')
# from sklearn import metrics
# prt("MSE:{}".format(metrics.mean_squared_error(y_te,y_pre)))
# clf.predict(x_te)
# a = df[df['Sex'] == 1]['Sex']
# prt(a)
# prt(len(ss))
# print(len(ss))
# print(df[df.Embarked == df.Embarked.value_counts().max()])
# prt(df.count().Age)
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