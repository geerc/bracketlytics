import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn import datasets, linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

hist_bbref = pd.read_csv(root + 'data/hist_bbref.csv')
hist_tourn = pd.read_csv(root + 'data/hist_tourn.csv')
curr_tourn = pd.read_csv(root + 'data/curr_tourn.csv')

# Drop weird column
hist_bbref = hist_bbref.drop(columns=['Unnamed: 0'], axis=1)
hist_tourn = hist_tourn.drop(columns=['Unnamed: 0'], axis=1)
curr_tourn = curr_tourn.drop(columns=['Unnamed: 0'], axis=1)

# Merge the data on the school name
data = hist_bbref.merge(hist_tourn, on='School')

# drop columns that I don't need
data = data.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FTA','FT%'])
data = data.dropna()

curr_tourn = curr_tourn.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FTA','FT%'])

# feature and target sets
y = data['Wins']
X = data.drop(columns=['School','Wins','Seed'])

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state=25)

# standardize X data
scaler = preprocessing.StandardScaler().fit(X)
X_scaled = scaler.transform(X)

# scale curr tourn data the same as hist data
curr_tourn_sc = scaler.transform(curr_tourn.iloc[:,1:])
print(curr_tourn_sc)


## possible pipe for future
# pipe = make_pipeline(StandardScaler(), LinearRegression())
# pipe.fit(X, y)
#
# pipe.score(curr_tourn)

# Linear Regression
LinReg = LinearRegression()
LinReg.fit(X_train, y_train)
result = LinReg.score(X_test, y_test)
print("Accuracy: %.2f%%" % (result*100.0))



# model = sm.OLS(y, X).fit()
#
# predictions = model.predict(X)
#
# model.summary()
#
# # Sci kit model prediction
#
# # Create and then fit the model
# lm = linear_model.LinearRegression()
# model = lm.fit(X,y)
#
# #
# predictions = lm.predict(X)
# # print(predictions)[0:5]
# print(predictions)
#
# print(lm.score(X,y))



# x = x.dropna()
# y = y.dropna()

# linear regression object
# linear_regression = LinearRegression()
#
# # fit the linear_model
# linear_regression.fit(x,y)
#
# # predict with data
# y_pred = linear_regression.predict(x)
#
# y_pred
