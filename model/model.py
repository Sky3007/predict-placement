import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib as plt
data=pd.read_csv("Placement_Data_Full_Class.csv")
data.head(20)
data.isnull().any()
data['status'] = data['status'].map({'Placed': 1, 'Not Placed': 0})
sn.countplot(x="status",hue="degree_t",data=data)
sn.countplot(x="status",hue="gender",data=data)
sn.countplot(x='status' , hue = 'specialisation' , data =data)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
cat_cols=["gender","ssc_b","hsc_b","hsc_s","degree_t","workex","specialisation","status"]
for i in cat_cols:
    data[i]=le.fit_transform(data[i]) 
sn.countplot(x='status' , hue = 'mba_p' , data =data)
sn.countplot(x='status' , hue = 'hsc_s' , data =data)
sn.countplot(x='status' , hue = 'ssc_p' , data =data)
data.status.value_counts()#unbalanced data
y=data.status
x=data.drop(['status','salary'],axis=1)
x_dummy=pd.get_dummies(x)
x_dummy.head(5)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(x_dummy, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
reg=LogisticRegression()
reg.fit(X_train,y_train)
predict = reg.predict(X_test)
print(accuracy_score(y_test, predict))
from sklearn.ensemble import RandomForestClassifier
cla=RandomForestClassifier()
cla.fit(X_train,y_train)
cla.score(X_test,y_test)
y_pred = cla.predict(X_test)
print(y_pred)
accuracy_score(y_test,y_pred)
from keras import regularizers
from sklearn import metrics
#scores
print("Accuracy Neural Net:",metrics.accuracy_score(y_test, predict))
print("Precision Neural Net:",metrics.precision_score(y_test, predict))
print("Recall Neural Net:",metrics.recall_score(y_test, predict))
print("F1 Score Neural Net:",metrics.f1_score(y_test, predict))


import joblib
filename='final_model.sav'
joblib.dump(cla,filename)