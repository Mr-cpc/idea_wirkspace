import joblib
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import *
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from basic.bupt_2017_11_28.type_deco import prt


def remove_fea(df: pd.DataFrame, fea_list: list):
    for fea in fea_list:
        df.pop(fea)


df = pd.read_csv("tr.csv")

# remove these three feas
remove_fea(df, ['PassengerId', 'Ticket', 'Name'])
# Process 'Cabin' fea,if null,set 1 else set 0 notice that must first process the notnull ,otherwis all the value are the notnull value
df.loc[df['Cabin'].notnull(), 'Cabin'] = 1
df.loc[df['Cabin'].isnull(), 'Cabin'] = 0
# process 'Age' fea,fill the null value with Age's median
df.loc[df['Age'].isnull(), 'Age'] = df['Age'].median()
# process 'Sex' fea,convert it from str to number
df.loc[df['Sex'] == 'male', 'Sex'] = 1
df.loc[df['Sex'] == 'female', 'Sex'] = 0
# process 'Embarked' convert it from str to number and fill the null value with Embarked's mod
df.loc[df['Embarked'] == 'Q', 'Embarked'] = 0
df.loc[df['Embarked'] == 'S', 'Embarked'] = 1
df.loc[df['Embarked'] == 'C', 'Embarked'] = 2
df.loc[df['Embarked'].isnull(), 'Embarked'] = df['Embarked'].value_counts().index[0]
# scale the continonous feas 'Age'、'SibSp'、'Parch'、'Fare'
df['Age'] = preprocessing.scale(df['Age'])
df['SibSp'] = preprocessing.scale(df['SibSp'])
df['Parch'] = preprocessing.scale(df['Parch'])
df['Fare'] = preprocessing.scale(df['Fare'])
clf = lr()
clf2 = KNeighborsClassifier(n_neighbors=10)
score1 = cross_val_score(clf,df.iloc[:,1:],df['Survived'],cv=25)
score2 = cross_val_score(clf2,df.iloc[:,1:],df['Survived'],cv=20)
prt(score1.mean())
prt(score2.std())
tr_X,te_X,tr_y,te_y = train_test_split(df.iloc[:,1:],df['Survived'],train_size=0.9)
clf.fit(tr_X, tr_y)
# best_ac,best_mod = 0 ,None
# f_prey = None
# real_y = None
# for i in range(1000):
#     tr_X,te_X,tr_y,te_y = train_test_split(df.iloc[:,1:],df['Survived'],train_size=0.2)
#     clf = lr()
#     clf.fit(tr_X,tr_y)
#     pre_y = clf.predict(te_X)
#     cur_ac = accuracy_score(te_y,pre_y)
#     if cur_ac > best_ac:
#         best_mod,best_ac = clf,cur_ac
#         f_prey = pre_y
#         real_y = te_y
# prt(classification_report(real_y.as_matrix(),f_prey,labels=[1,0]))
# joblib.dump(best_mod,"clf.m")
joblib.dump(clf,"clf.m")
