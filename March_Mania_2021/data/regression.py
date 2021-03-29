import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

bbref = pd.read_csv(root + 'data/bbref.csv')
tourney = pd.read_csv(root + 'data/tourney_data.csv')

# Drop weird column
bbref = bbref.drop(columns=['Unnamed: 0'], axis=1)
tourney = tourney.drop(columns=['Unnamed: 0'], axis=1)

# Merge the data on the school name
data = bbref.merge(tourney, on='School')
data

# drop columns that I don't need
data = data.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FTA','FT%'])
data = data.dropna()

result = data.copy()
for feature_name in data.columns:
        max_value = data[feature_name].max()
        min_value = data[feature_name].min()
        result[feature_name] = (data[feature_name] - min_value) / (max_value - min_value)
result['Wins'].round(3)
# feature and target sets
y = data['Wins']
X = data.drop(columns=['School','Wins','Seed'])

model = sm.OLS(y, X).fit()

predictions = model.predict(X)

model.summary()

# Sci kit model prediction

# Create and then fit the model
lm = linear_model.LinearRegression()
model = lm.fit(X,y)

#
predictions = lm.predict(X)
# print(predictions)[0:5]
print(predictions)

print(lm.score(X,y))



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
