import pandas as pd
from sklearn.model_selection import train_test_split

from basic.bupt_2017_11_28.type_deco import *
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
prt(df_te.info())