import numpy as np
import pandas as pd
import seaborn as sb
from queue import *

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

data = pd.read_csv(ROOT + 'combined_data.csv')
# data_2018 = pd.read_csv(ROOT + 'combined_data_2018.csv')
# data_2019 = pd.read_csv(ROOT + 'combined_data_2019.csv')
season_stats = pd.read_csv(ROOT + 'advanced_stats.csv')

season_stats = season_stats.set_index('School')
season_stats = season_stats.drop("Unnamed: 0", axis=1)

X = data.iloc[:,3:21]
y = data.iloc[:,2]

# Create training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=25)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)

# Remove na values (there shouldn't be any, but just in case)
X_train = X_train.dropna(axis=1, how='all')
y_trian = y_train.dropna(axis=1, how='all')

# Create and fit LogisticRegression
LogReg = LogisticRegression(solver='lbfgs', max_iter=200) # Specify solver to satifsy future warning on default solver change
LogReg.fit(X_train, y_train.values.ravel())

def advance_team(winner, round):
    print(winner)
    round.put(winner)

def predict_game(high_seed, low_seed):

    # Get stats for each team, add suffix to columns for low_seed
    team = season_stats.loc[high_seed]
    team_1 = season_stats.loc[low_seed]
    team_1 = team_1.add_suffix('_1')

    # Put team stats into one series for regression analysis
    game = team.append(team_1)

    # Reshape so it fits into regression
    game = game.values.reshape(1,-1)

    # Predict the game
    pred = LogReg.predict(game)

    if pred == 1:
        winner = high_seed
    elif pred == 0:
        winner = low_seed

    return winner

# season_stats = season_stats.set_index('School')
# season_stats = season_stats.drop("Unnamed: 0", axis=1)
#
# X = data.iloc[:,3:21]
# y = data.iloc[:,2]
#
# # Create training and testing data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=25)
#
# X_train = pd.DataFrame(X)
# y_train = pd.DataFrame(y)
#
# # Remove na values (there shouldn't be any, but just in case)
# X_train = X_train.dropna(axis=1, how='all')
# y_trian = y_train.dropna(axis=1, how='all')
#
# # Create and fit LogisticRegression
# LogReg = LogisticRegression(solver='lbfgs', max_iter=200) # Specify solver to satifsy future warning on default solver change
# LogReg.fit(X_train, y_train.values.ravel())
#
# def predict_game(high_seed, low_seed):
#
#     # Get stats for each team, add suffix to columns for low_seed
#     team = season_stats.loc[high_seed]
#     team_1 = season_stats.loc[low_seed]
#     team_1 = team_1.add_suffix('_1')
#
#     # Put team stats into one series for regression analysis
#     game = team.append(team_1)
#
#     # Reshape so it fits into regression
#     game = game.values.reshape(1,-1)
#
#     # Predict the game
#     pred = LogReg.predict(game)
#
#     if pred == 1:
#         winner = high_seed
#     elif pred == 0:
#         winner = low_seed
#
#     return winner

def create_bracket():
    round1 = Queue()

    # East Region
    round1.put('Villanova_2018')
    round1.put('Radford_2018')
    round1.put('Virginia_Tech_2018')
    round1.put('Alabama_2018')
    round1.put('West_Virginia_2018')
    round1.put('Murray_State_2018')
    round1.put('Wichita_State_2018')
    round1.put('Marshall_2018')
    round1.put('Florida_2018')
    round1.put('St._Bonaventure_2018')
    round1.put('Texas_Tech_2018')
    round1.put('Stephen_F._Austin_2018')
    round1.put('Arkansas_2018')
    round1.put('Butler_2018')
    round1.put('Purdue_2018')
    round1.put('Cal_State_Fullerton_2018')
    # West region
    round1.put('Xavier_2018')
    round1.put('Texas_Southern_2018')
    round1.put('Missouri_2018')
    round1.put('Florida_State_2018')
    round1.put('Ohio_State_2018')
    round1.put('South_Dakota_State_2018')
    round1.put('Gonzaga_2018')
    round1.put('North_Carolina-Greensboro_2018')
    round1.put('Houston_2018')
    round1.put('San_Diego_State_2018')
    round1.put('Michigan_2018')
    round1.put('Montana_2018')
    round1.put('Texas_A&M_2018')
    round1.put('Providence_2018')
    round1.put('North_Carolina_2018')
    round1.put('Lipscomb_2018')
    # Midwest Region
    round1.put('Kansas_2018')
    round1.put('Pennsylvania_2018')
    round1.put('Seton_Hall_2018')
    round1.put('North_Carolina_State_2018')
    round1.put('Clemson_2018')
    round1.put('New_Mexico_State_2018')
    round1.put('Auburn_2018')
    round1.put('College_of_Charleston_2018')
    round1.put('Texas_Christian_2018')
    round1.put('Syracuse_2018')
    round1.put('Michigan_State_2018')
    round1.put('Bucknell_2018')
    round1.put('Rhode_Island_2018')
    round1.put('Oklahoma_2018')
    round1.put('Duke_2018')
    round1.put('Iona_2018')
    # South region
    round1.put('Virginia_2019')
    round1.put('Maryland-Baltimore_County_2018')
    round1.put('Creighton_2018')
    round1.put('Kansas_State_2018')
    round1.put('Kentucky_2018')
    round1.put('Davidson_2018')
    round1.put('Arizona_2018')
    round1.put('Buffalo_2018')
    round1.put('Miami_(FL)_2018')
    round1.put('Loyola_(IL)_2018')
    round1.put('Tennessee_2018')
    round1.put('Wright_State_2018')
    round1.put('Nevada_2018')
    round1.put('Texas_2018')
    round1.put('Cincinnati_2018')
    round1.put('Georgia_State_2018')

    return round1
