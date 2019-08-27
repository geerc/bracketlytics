#import required packages
import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from math import sqrt
import matplotlib.pyplot as plt

# Specify root folder
ROOT = '/Users/christiangeer/bracketlytics/new_model/'

# Read in csv file and remove unecessary F1 column
data = pd.read_csv(ROOT + 'data/joined_data.csv')
data = data.drop("F1", axis=1)

# Split data into attributes and lables
X = data.iloc[:,1:9].values
y = data.iloc[:, 9].values

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Feature sclaing
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


rmse_val = [] #to store rmse values for different k
for K in range(100):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)

    model.fit(X_train, y_train)  #fit the model
    pred=model.predict(X_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)


#plotting the rmse values against k values
curve = pd.DataFrame(rmse_val) #elbow curve
curve.plot()

predict = model.predict(test)
submission['Item_Outlet_Sales'] = predict
submission.to_csv('submit_file.csv',index=False)
