import numpy as np
import pandas as pd
import seaborn as sb
import functions
from queue import *

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'new_tourney_data.csv')
teams = pd.read_csv(ROOT + 'Teams.csv')

# Convert Season and team columns to strings so they can be commbined
tourney_data['Season'] = tourney_data['Season'].astype(str)
tourney_data['Wteam'] = tourney_data['Wteam'].astype(str)

# Set team as index
tourney_data.set_index('Wteam', inplace=True)

round1 = Queue()
round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

def create_bracket(round1):
    round1.put('1438')
    round1.put('1420')
    round1.put('1166')
    round1.put('1243')
    round1.put('1246')
    round1.put('1172')
    round1.put('1112')
    round1.put('1138')
    round1.put('1274')
    round1.put('1260')
    round1.put('1397')
    round1.put('1460')
    round1.put('1305')
    round1.put('1400')
    round1.put('1153')
    round1.put('1209')
    round1.put('1462')
    round1.put('1411')
    round1.put('1281')
    round1.put('1199')
    round1.put('1326')
    round1.put('1355')
    round1.put('1211')
    round1.put('1422')
    round1.put('1222')
    round1.put('1361')
    round1.put('1276')
    round1.put('1285')
    round1.put('1401')
    round1.put('1344')
    round1.put('1314')
    round1.put('1252')
    round1.put('1432')
    round1.put('1347')
    round1.put('1439')
    round1.put('1104')
    round1.put('1452')
    round1.put('1293')
    round1.put('1455')
    round1.put('1267')
    round1.put('1196')
    round1.put('1382')
    round1.put('1403')
    round1.put('1372')
    round1.put('1116')
    round1.put('1139')
    round1.put('1345')
    round1.put('1168')
    round1.put('1242')
    round1.put('1335')
    round1.put('1371')
    round1.put('1301')
    round1.put('1155')
    round1.put('1308')
    round1.put('1120')
    round1.put('1158')
    round1.put('1395')
    round1.put('1393')
    round1.put('1277')
    round1.put('1137')
    round1.put('1348')
    round1.put('1328')
    round1.put('1181')
    round1.put('1233')
    return round1

# function predict the probabilites of each team winning, and return the higher team
def predict_game(high_seed, low_seed):
    if high_seed != 1 and low_seed != 1:
        # Get stats for two teams playing
        team1a = tourney_data.loc[high_seed]
        team1a = team1a.loc[['eFG%','TOVp','ORBp','FTp']]

        team2a = tourney_data.loc[low_seed]
        team2a = team2a.loc[['eFG%','TOVp','ORBp','FTp']]
        team2a = team2a.rename({'eFG%':'Opp_eFG%', 'TOVp':'Opp_TOVp', 'ORBp':'Opp_ORBp', 'FTp':'Opp_FTp'})

        team1b = tourney_data.loc[low_seed]
        team1b = team1b.loc[['eFG%','TOVp','ORBp','FTp']]

        team2b = tourney_data.loc[high_seed]
        team2b = team2b.loc[['eFG%','TOVp','ORBp','FTp']]
        team2b = team2b.rename({'eFG%':'Opp_eFG%', 'TOVp':'Opp_TOVp', 'ORBp':'Opp_ORBp', 'FTp':'Opp_FTp'})

        # Create game from perspective of both teams
        game_a = team2a.append(team1a)
        game_b = team1b.append(team2b)

        # Change series to dataframe so that it can be fed into the model
        game = DataFrame(dict(s1 = game_a, s2 = game_b))

        # Transpose df and rename indices
        game = game.T
        game = game.rename({'s1': high_seed, 's2': low_seed}, axis='index')

        # Predict probablies of winning
        y_pred_prob = LogReg.predict_proba(game)

        # Select just each teams probabilites of winning
        team1 = y_pred_prob[0, 0]
        team2 = y_pred_prob[1, 0]

        # Create strength of schedule
        high_seed_sos = sos.loc[high_seed].item()
        low_seed_sos = sos.loc[low_seed].item()

        # Determine winner
        if team1 * high_seed_sos > team2 * low_seed_sos:
            winner = high_seed
        elif team2 * low_seed_sos > team1 * high_seed_sos:
            winner = low_seed

        return(winner)
    elif high_seed == 1:
        return low_seed
    elif low_seed == 1:
        return high_seed

# Function to move winning team to next round
def advance_team(winner, round):
    print(winner)
    round.put(winner)

# print(tourney_data)
X = tourney_data.iloc[:,2:11].values
y = tourney_data.iloc[:,12].values

# Create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state=25)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)

# # Remove na values
# X_train = X_train.dropna(axis=0, how='all')
# y_train = y_train.dropna(y_train.index[5282])

# Create and fit the regression
LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)
result = LogReg.score(X_test, y_test)
print("Accuracy: %.2f%%" % (result*100.0))

# from sklearn.metrics import confusion_matrix
# confusion_matrix = confusion_matrix(y_test, y_pred)
# print('Confusion Matrix: \n', confusion_matrix)
#
# print(classification_report(y_test, y_pred))
round1 = create_bracket(round1)

# Round 1 games
n = 0
print("\nAdvance to round of 32:")
while n < 32:
    high_seed = round1.get()
    low_seed = round1.get()
    advance_team(predict_game(high_seed, low_seed), round2)
    n += 1

# Round 2 games
n = 0
print("\nAdvance to Sweet 16:")
while n < 16:
    high_seed = round2.get()
    low_seed = round2.get()
    advance_team(predict_game(high_seed, low_seed), round3)
    n += 1

# Round 3 games
n = 0
print("\nAdvance to Elite 8:")
while n < 8:
    high_seed = round3.get()
    low_seed = round3.get()
    advance_team(predict_game(high_seed, low_seed), round4)
    n += 1

# Round 4 games
n = 0
print("\nAdvance to Final 4:")
while n < 4:
    high_seed = round4.get()
    low_seed = round4.get()
    advance_team(predict_game(high_seed, low_seed), round5)
    n += 1

# Round 5 games
n = 0
print("\nAdvance to Championship game:")
while n < 2:
    high_seed = round5.get()
    low_seed = round5.get()
    advance_team(predict_game(high_seed, low_seed), round6)
    n += 1

# Championship
n = 0
print("\nChampion:")
high_seed = round6.get()
low_seed = round6.get()
advance_team(predict_game(high_seed, low_seed), round7)
