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
# print(tabulate(curr_tourn.sort_values(by='pred wins', ascending=False),headers=curr_tourn.columns))
curr_tourn.to_csv(root + 'Predictions/2021_LinReg.csv')


# FOUR FACTOR REGRESSION
FF_hist_bbref = pd.read_csv(root + 'data/FF_hist_bbref.csv')
FF_hist_opp = pd.read_csv(root + 'data/FF_hist_bbref_opp.csv')
FF_hist_tourn = pd.read_csv(root + 'data/FF_hist_tourney.csv')
FF_curr_tourn = pd.read_csv(root + 'data/curr_tourn.csv')
FF_curr_tourn_opp = pd.read_csv(root + 'data/curr_tourn.csv')

FF_hist_bbref = FF_hist_bbref.drop(columns=['Unnamed: 0'], axis=1)
FF_hist_opp = FF_hist_opp.drop(columns=['Unnamed: 0'], axis=1)
FF_hist_tourn = FF_hist_tourn.drop(columns=['Unnamed: 0'], axis=1)
FF_curr_tourn = FF_curr_tourn.drop(columns=['Unnamed: 0'], axis=1)
FF_curr_tourn_opp = FF_curr_tourn_opp.drop(columns=['Unnamed: 0'], axis=1)

FF_hist_bbref = FF_hist_bbref.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
FF_curr_tourn = FF_curr_tourn.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
FF_hist_opp = FF_hist_opp.drop(FF_hist_opp.iloc[:,1:21], axis=1)
FF_curr_tourn_opp = FF_curr_tourn_opp.drop(FF_curr_tourn_opp.iloc[:,1:21], axis=1)

# Create DRB
FF_hist_bbref['DRB'] = FF_hist_bbref['TRB'] - FF_hist_bbref['ORB']
FF_hist_opp['DRB'] = FF_hist_opp['TRB'] - FF_hist_opp['ORB']

FF_curr_tourn['DRB'] = FF_curr_tourn['TRB'] - FF_curr_tourn['ORB']
FF_curr_tourn_opp['DRB'] = FF_curr_tourn_opp['TRB'] - FF_curr_tourn_opp['ORB']

# Create FF stats

# EFG%
FF_hist_bbref['oEFG'] = ((FF_hist_bbref['FG'] + (0.5 * FF_hist_bbref['3P'])) / FF_hist_bbref['FGA']).round(3)
FF_hist_bbref['dEFG'] = ((FF_hist_opp['FG'] + (0.5 * FF_hist_opp['3P'])) / FF_hist_opp['FGA']).round(3)

FF_curr_tourn['oEFG'] = ((FF_curr_tourn['FG'] + (0.5 * FF_curr_tourn['3P'])) / FF_curr_tourn['FGA']).round(3)
FF_curr_tourn['dEFG'] = ((FF_curr_tourn_opp['FG'] + (0.5 * FF_curr_tourn_opp['3P'])) / FF_curr_tourn_opp['FGA']).round(3)

# Turnovers
FF_hist_bbref['oTOV'] = (FF_hist_bbref['TOV'] / ((FF_hist_bbref['TOV']) + (0.44 + FF_hist_bbref['FTA']) + FF_hist_bbref['TOV'])).round(3)
FF_hist_bbref['dTOV'] = (FF_hist_opp['TOV'] / ((FF_hist_opp['TOV']) + (0.44 + FF_hist_opp['FTA']) + FF_hist_opp['TOV'])).round(3)

FF_curr_tourn['oTOV'] = (FF_curr_tourn['TOV'] / ((FF_curr_tourn['TOV']) + (0.44 + FF_curr_tourn['FTA']) + FF_curr_tourn['TOV'])).round(3)
FF_curr_tourn['dTOV'] = (FF_curr_tourn_opp['TOV'] / ((FF_curr_tourn_opp['TOV']) + (0.44 + FF_curr_tourn_opp['FTA']) + FF_curr_tourn_opp['TOV'])).round(3)

# Rebounding
FF_hist_bbref['oREB'] = (FF_hist_bbref['ORB'] / (FF_hist_bbref['ORB'] + FF_hist_opp['DRB'])).round(3)
FF_hist_bbref['dREB'] = (FF_hist_bbref['DRB'] / (FF_hist_opp['ORB'] + FF_hist_bbref['DRB'])).round(3)

FF_curr_tourn['oREB'] = (FF_curr_tourn['ORB'] / (FF_curr_tourn['ORB'] + FF_curr_tourn_opp['DRB'])).round(3)
FF_curr_tourn['dREB'] = (FF_curr_tourn['DRB'] / (FF_curr_tourn_opp['ORB'] + FF_curr_tourn['DRB'])).round(3)

# Free Throws
FF_hist_bbref['oFT'] = (FF_hist_bbref['FT'] / FF_hist_bbref['FGA']).round(3)
FF_hist_bbref['dFT'] = (FF_hist_opp['FT'] / FF_hist_opp['FGA']).round(3)

FF_curr_tourn['oFT'] = (FF_curr_tourn['FT'] / FF_curr_tourn['FGA']).round(3)
FF_curr_tourn['dFT'] = (FF_curr_tourn_opp['FT'] / FF_curr_tourn_opp['FGA']).round(3)

# remove old columns
FF_hist_bbref = FF_hist_bbref.drop(FF_hist_bbref.iloc[:,3:13], axis=1)
FF_curr_tourn = FF_curr_tourn.drop(FF_curr_tourn.iloc[:,3:13], axis=1)

# merge the wins and stats
FF_data = FF_hist_bbref.merge(FF_hist_tourn, on='School')

# feature and target sets
FF_y = FF_data['Wins']

FF_X = FF_data.drop(columns=['School','Wins','Seed'])

# train test split
FF_X_train, FF_X_test, FF_y_train, FF_y_test = train_test_split(FF_X, FF_y, test_size = .3, random_state=25)

# standardize X data
FF_scaler = preprocessing.StandardScaler().fit(FF_X_train)
FF_X_train_sc = FF_scaler.transform(FF_X_train)
FF_X_test_sc = FF_scaler.transform(FF_X_test)

# scale curr tourn data the same as hist data
FF_curr_tourn_sc = FF_scaler.transform(FF_curr_tourn.iloc[:,1:])

## possible pipe for future
# pipe = make_pipeline(StandardScaler(), LinearRegression())
# pipe.fit(X, y)
#
# pipe.score(curr_tourn)

# Linear Regression
FF_LinReg = LinearRegression().fit(FF_X_train_sc, FF_y_train)
FF_result = FF_LinReg.score(FF_X_test_sc, FF_y_test)
print("Accuracy: %.2f%%" % (FF_result*100.0), "\n")

# predict curr tournament
FF_pred = FF_LinReg.predict(FF_curr_tourn_sc)

FF_curr_tourn['pred wins'] = FF_pred
# print(tabulate(FF_curr_tourn.sort_values(by='pred wins', ascending=False),headers=FF_curr_tourn.columns))
FF_curr_tourn.to_csv(root + 'Predictions/2021_FFLinReg.csv')
