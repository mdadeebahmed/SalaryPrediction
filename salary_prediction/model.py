import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('hiring.csv')



x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]



regressor = LinearRegression()


regressor.fit(x.values, y.values)


pickle.dump(regressor, open('model.pkl','wb'))


model = pickle.load(open('model.pkl','rb'))

print(model.predict([[2, 9, 6]]))




