import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from tabulate import tabulate


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
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_sc = scaler.transform(X_train)
X_test_sc = scaler.transform(X_test)

# scale curr tourn data the same as hist data
curr_tourn_sc = scaler.transform(curr_tourn.iloc[:,1:])

## possible pipe for future
# pipe = make_pipeline(StandardScaler(), LinearRegression())
# pipe.fit(X, y)
#
# pipe.score(curr_tourn)

# Linear Regression
LinReg = LinearRegression().fit(X_train_sc, y_train)
result = LinReg.score(X_test_sc, y_test)
print("Accuracy: %.2f%%" % (result*100.0), "\n")

# predict curr tournament
pred = LinReg.predict(curr_tourn_sc)

curr_tourn['pred wins'] = pred
print(tabulate(curr_tourn.sort_values(by='pred wins', ascending=False),headers=curr_tourn.columns))

# FOUR FACTOR REGRESSION
FF_hist_bbref = pd.read_csv(root + 'data/FF_hist_bbref.csv')
FF_hist_opp = pd.read_csv(root + 'data/FF_hist_bbref_opp.csv')
FF_hist_tourn = pd.read_csv(root + 'data/FF_hist_tourney.csv')

FF_hist_bbref = FF_hist_bbref.drop(columns=['Unnamed: 0'], axis=1)
FF_hist_opp = FF_hist_opp.drop(columns=['Unnamed: 0'], axis=1)
FF_hist_tourn = FF_hist_tourn.drop(columns=['Unnamed: 0'], axis=1)

FF_hist_bbref = FF_hist_bbref.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
FF_hist_opp = FF_hist_opp.drop(FF_hist_opp.iloc[:,1:21], axis=1)
FF_hist_tourn =

# Create DRB
FF_hist_bbref['DRB'] = FF_hist_bbref['TRB'] - FF_hist_bbref['ORB']
FF_hist_opp['DRB'] = FF_hist_opp['TRB'] - FF_hist_opp['ORB']

# Create FF stats

# EFG%
FF_hist_bbref['oEFG'] = ((FF_hist_bbref['FG'] + (0.5 * FF_hist_bbref['3P'])) / FF_hist_bbref['FGA']).round(3)
FF_hist_bbref['dEFG'] = ((FF_hist_opp['FG'] + (0.5 * FF_hist_opp['3P'])) / FF_hist_opp['FGA']).round(3)

# Turnovers
FF_hist_bbref['oTOV'] = (FF_hist_bbref['TOV'] / ((FF_hist_bbref['TOV']) + (0.44 + FF_hist_bbref['FTA']) + FF_hist_bbref['TOV'])).round(3)
FF_hist_bbref['dTOV'] = (FF_hist_opp['TOV'] / ((FF_hist_opp['TOV']) + (0.44 + FF_hist_opp['FTA']) + FF_hist_opp['TOV'])).round(3)

# Rebounding
FF_hist_bbref['oREB'] = (FF_hist_bbref['ORB'] / (FF_hist_bbref['ORB'] + FF_hist_opp['DRB'])).round(3)
FF_hist_bbref['dREB'] = (FF_hist_bbref['DRB'] / (FF_hist_opp['ORB'] + FF_hist_bbref['DRB'])).round(3)

# Free Throws
FF_hist_bbref['oFT'] = (FF_hist_bbref['FT'] / FF_hist_bbref['FGA']).round(3)
FF_hist_bbref['dFT'] = (FF_hist_opp['FT'] / FF_hist_opp['FGA']).round(3)

FF_hist_bbref
FF_hist_tourn

data = hist_bbref.merge(hist_tourn, on='School')
