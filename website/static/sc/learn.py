import pandas as pd
from sklearn.tree import DecisionTreeClassifier



def predict(time,comp,date):
    date3 = {
        1: 35,
        2: 47,
        3: 47,
        4: 48,
        5: 40,
        6: 14,
        7 : 0,
    }

    date6 = {
        1: 20,
        2: 22,
        3: 18,
        4: 16,
        5: 16,
        6 : 0,
        7 : 0,
    }

    if comp==6:
        cafe = pd.read_csv('website/static/sc/6корпус.xlsx - Лист1 (2).csv')
        datefor=date6[date]
    elif comp==3:
        cafe = pd.read_csv('website/static/sc/dataset_-_dataset_6.csv')
        datefor = date3[date]
    X = cafe.drop(columns=['load'])
    Y = cafe['load']

    X = X.dropna()
    Y = Y.dropna()

    m = DecisionTreeClassifier()
    m.fit(X.values, Y.values)
    pred = m.predict([[datefor, time]])
    return pred