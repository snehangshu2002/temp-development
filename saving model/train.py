
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

url ="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres","skin", "test", "mass", "pedi", "age","class"]

df= pd.read_csv(url, names= names)
# print(df.head)

x=df.iloc[:,0:8]
y=df.iloc[:,8]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

print(f"[INFO] model has been trained")

result = model.score(x_test,y_test)

print(f"[INFO] model score : {result}")


joblib.dump(model,"saving model/diabetes.pkl")