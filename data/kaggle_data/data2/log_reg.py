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
import functions

round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

data = pd.read_csv(ROOT + 'combined_data.csv')
data_2019 = pd.read_csv(ROOT + 'combined_data_2019.csv')
data_2018 = pd.read_csv(ROOT + 'combined_data_2018.csv')
season_stats = pd.read_csv(ROOT + 'advanced_stats.csv')

season_stats = season_stats.set_index('School')
season_stats = season_stats.drop("Unnamed: 0", axis=1)

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

# Create the initial braket
round1 = functions.create_bracket()

# Round 1
n = 0
print("\nAdvance to the round of 32:")
while n < 32:
    high_seed = round1.get()
    low_seed = round1.get()
    functions.advance_team(functions.predict_game(high_seed, low_seed), round2)
    n += 1

# Round 2
n = 0
print("\nAdvance to the Sweet 16:")
while n < 16:
    high_seed = round2.get()
    low_seed = round2.get()
    functions.advance_team(functions.predict_game(high_seed, low_seed), round3)
    n += 1

# Sweet 16
n = 0
print("\nAdvance to the Elite 8:")
while n < 8:
    high_seed = round3.get()
    low_seed = round3.get()
    functions.advance_team(functions.predict_game(high_seed, low_seed), round4)
    n += 1

# Elite 8
n = 0
print("\nAdvance to the Final Four:")
while n < 4:
    high_seed = round4.get()
    low_seed = round4.get()
    functions.advance_team(functions.predict_game(high_seed, low_seed), round5)
    n += 1

# Final Four
n = 0
print("\nAdvance to the Champioship:")
while n < 2:
    high_seed = round5.get()
    low_seed = round5.get()
    functions.advance_team(functions.predict_game(high_seed, low_seed), round6)
    n += 1

# Championship
n = 0
print("\nChampion")
igh_seed = round6.get()
low_seed = round6.get()
functions.advance_team(functions.predict_game(high_seed, low_seed), round7)
