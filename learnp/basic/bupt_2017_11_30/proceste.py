import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression as lr

from basic.bupt_2017_11_28.type_deco import prt


def remove_fea(df:pd.DataFrame,fea_list:list):
    for fea in fea_list:
        df.pop(fea)

df = pd.read_csv("test.csv")

#remove these three feas
remove_fea(df,['PassengerId','Ticket','Name'])
#Process 'Cabin' fea,if null,set 1 else set 0 notice that must first process the notnull ,otherwis all the value are the notnull value
df.loc[df['Cabin'].notnull(),'Cabin'] = 1
df.loc[df['Cabin'].isnull(),'Cabin'] = 0
#process 'Age' fea,fill the null value with Age's median
df.loc[df['Age'].isnull(),'Age'] = df['Age'].median()
#process 'Sex' fea,convert it from str to number
df.loc[df['Sex'] == 'male','Sex'] = 1
df.loc[df['Sex'] == 'female','Sex'] = 0
#process 'Embarked' convert it from str to number and fill the null value with Embarked's mod
df.loc[df['Embarked'] == 'Q','Embarked'] = 0
df.loc[df['Embarked'] == 'S','Embarked'] = 1
df.loc[df['Embarked'] == 'C','Embarked'] = 2
df.loc[df['Embarked'].isnull(),'Embarked'] = df['Embarked'].value_counts().index[0]
#scale the fea 'Age'
df['Age'] = preprocessing.scale(df['Age'])
df['SibSp'] = preprocessing.scale(df['SibSp'])
df['Parch'] = preprocessing.scale(df['Parch'])
df.loc[df['Fare'].isnull(),'Fare'] = df['Fare'].median()
df['Fare'] = preprocessing.scale(df['Fare'])
df.info()

clf = joblib.load("clf.m")
y_pre = clf.predict(df.as_matrix())
with open("ans.txt","w") as f:
    for i in range(len(y_pre)):
        f.write("{},{}".format(i+892,y_pre[i]))
        f.write('\n')

