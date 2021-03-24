import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn import linear_model

# Specify root folder
ROOT = '/Users/christiangeer/bracketlytics/new_model/'

# Read in csv file and remove unecessary F1 column
data = pd.read_csv(ROOT + 'data/joined_data.csv')
data = data.drop("F1", axis=1)

# Create dependent and independent variable dataframes
df = data.drop(["School", "wins"], axis=1)
target = data["wins"]

# Stats model linear regression
X = df
y = target

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

lm.score(X,y)
