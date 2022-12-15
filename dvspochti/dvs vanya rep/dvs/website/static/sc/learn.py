import pandas as pd
from sklearn.tree import DecisionTreeClassifier

cafe = pd.read_csv('W:/файлы с браузера/dvspochti/dvs vanya rep/dvs/website/static/sc/test.csv')

X = cafe.drop(columns=['load'])
Y = cafe['load']

X = X.dropna()
Y = Y.dropna()

m = DecisionTreeClassifier()
m.fit(X.values, Y.values)

def predict(time):
    pred = m.predict([[10, time, 3]])
    return pred

