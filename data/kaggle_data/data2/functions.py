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
data_2018 = pd.read_csv(ROOT + 'combined_data_2018')
data_2019 = pd.read_csv(ROOT + 'combined_data_2019.csv')
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
    round1.put('Duke_2019')
    round1.put('North_Dakota_State_2019')
    round1.put('Virginia_Commonwealth_2019')
    round1.put('Central_Florida_2019')
    round1.put('Mississippi_State_2019')
    round1.put('Liberty_2019')
    round1.put('Virginia_Tech_2019')
    round1.put('Saint_Louis_2019')
    round1.put('Maryland_2019')
    round1.put('Belmont_2019')
    round1.put('Louisiana_State_2019')
    round1.put('Yale_2019')
    round1.put('Louisville_2019')
    round1.put('Minnesota_2019')
    round1.put('Michigan_State_2019')
    round1.put('Bradley_2019')
    # West region
    round1.put('Gonzaga_2019')
    round1.put('Fairleigh_Dickinson_2019')
    round1.put('Syracuse_2019')
    round1.put('Baylor_2019')
    round1.put('Marquette_2019')
    round1.put('Murray_State_2019')
    round1.put('Florida_State_2019')
    round1.put('Vermont_2019')
    round1.put('Buffalo_2019')
    round1.put('Arizona_State_2019')
    round1.put('Texas_Tech_2019')
    round1.put('Northern_Kentucky_2019')
    round1.put('Nevada_2019')
    round1.put('Florida_2019')
    round1.put('Michigan_2019')
    round1.put('Montana_2019')
    # Midwest Region
    round1.put('North_Carolina_2019')
    round1.put('Iona_2019')
    round1.put('Utah_State_2019')
    round1.put('Washington_2019')
    round1.put('Auburn_2019')
    round1.put('New_Mexico_State_2019')
    round1.put('Kansas_2019')
    round1.put('Northeastern_2019')
    round1.put('Iowa_State_2019')
    round1.put('Ohio_State_2019')
    round1.put('Houston_2019')
    round1.put('Georgia_State_2019')
    round1.put('Wofford_2019')
    round1.put('Seton_Hall_2019')
    round1.put('Kentucky_2019')
    round1.put('Abilene_Christian_2019')
    # South region
    round1.put('Virginia_2019')
    round1.put('Gardner-Webb_2019')
    round1.put('Mississippi_2019')
    round1.put('Oklahoma_2019')
    round1.put('Wisconsin_2019')
    round1.put('Oregon_2019')
    round1.put('Kansas_State_2019')
    round1.put('UC-Irvine_2019')
    round1.put('Villanova_2019')
    round1.put('Saint_Marys_(CA)_2019')
    round1.put('Purdue_2019')
    round1.put('Old_Dominion_2019')
    round1.put('Cincinnati_2019')
    round1.put('Iowa_2019')
    round1.put('Tennessee_2019')
    round1.put('Colgate_2019')

    return round1
