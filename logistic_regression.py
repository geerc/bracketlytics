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

round1 = Queue()
round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

ROOT = '/Users/Christian/Documents/cs310f2018/project-cmpsc-310-fall-2018-allegheny-college-craig-engels-fan-club'

game_data = pd.read_csv(ROOT + '/data/2018TeamStats_Final.csv')
season_stats = pd.read_csv(ROOT + '/data/season_data.csv')
sos = pd.read_csv(ROOT + '/data/sos.csv')

# Remove unnecassary columns
game_data.drop(labels=['gameid','Opp PTS','PF','Opp PF','Rank','MP','FG%','2P','2PA','2P%','3PA','3P%','FT%','TRB','AST','STL','BLK','PTS','Opp FG%','Opp 2P','Opp 2PA','Opp 2P%','Opp 3PA','Opp 3P%','Opp FT%','Opp TRB','Opp AST','Opp STL','Opp BLK'], inplace=True, axis=1)
season_stats.drop(labels=['X.11','X.10','X.9','X.8','X.7','X.6','X.5','X.4','X.3','X.2','X.1','X','Rank','SOS'], inplace=True, axis=1)
sos.drop(labels=['Unnamed: 0','X.11','X.10','X.9','X.8','X.7','X.6','X.5','X.4','X.3','X.2','X.1','X','Rank'], inplace=True, axis=1)
# print(sos)
# sos['SOS'] = sos['SOS'] + 12.48
# sos.sort_values(by=['SOS'])

# Set team as index
season_stats.set_index('Team', inplace=True)
sos.set_index('Team', inplace=True)

# Convert to lower case
sos.index = sos.index.str.lower()

# Convert stat variables to numeric
game_data['FG'] = game_data['FG'].apply(pd.to_numeric, errors='coerce')
game_data['FGA'] = game_data['FGA'].apply(pd.to_numeric, errors='corerce')
game_data['3P'] = game_data['3P'].apply(pd.to_numeric, errors='coerce')
game_data['FT'] = game_data['FT'].apply(pd.to_numeric, errors='coerce')
game_data['FTA'] = game_data['FTA'].apply(pd.to_numeric, errors='coerce')
game_data['ORB'] = game_data['ORB'].apply(pd.to_numeric, errors='coerce')
game_data['DRB'] = game_data['DRB'].apply(pd.to_numeric, errors='coerce')
game_data['TOV'] = game_data['TOV'].apply(pd.to_numeric, errors='coerce')
game_data['Win?'] = game_data['Win?'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FG'] = game_data['Opp FG'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FGA'] = game_data['Opp FGA'].apply(pd.to_numeric, errors='corerce')
game_data['Opp 3P'] = game_data['Opp 3P'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FT'] = game_data['Opp FT'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FTA'] = game_data['Opp FTA'].apply(pd.to_numeric, errors='coerce')
game_data['Opp ORB'] = game_data['Opp ORB'].apply(pd.to_numeric, errors='coerce')
game_data['Opp DRB'] = game_data['Opp DRB'].apply(pd.to_numeric, errors='coerce')
game_data['Opp TOV'] = game_data['Opp TOV'].apply(pd.to_numeric, errors='coerce')

functions.create_stats(game_data)
functions.create_stats(season_stats)

# Drop unnecassary columns
game_data.drop(labels=['FG','FGA','3P','FT','FTA','ORB','DRB','TOV','Opp FG','Opp FGA','Opp 3P','Opp FT','Opp FTA','Opp ORB','Opp DRB','Opp TOV'], inplace=True, axis=1)
season_stats.drop(labels=['Unnamed: 0','FG','FGA','3P','FT','FTA','ORB','DRB','TOV','Opp FG','Opp FGA','Opp 3P','Opp FT','Opp FTA','Opp ORB','Opp DRB','Opp TOV'], inplace=True, axis=1)

X = game_data.iloc[:,2:10].values
y = game_data.iloc[:,1].values

# Create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state=25)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)

# Remove na values
X_train = X_train.dropna(axis=0, how='all')
y_train = y_train.drop(y_train.index[5282])

# Create and fit the regression
LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

# from sklearn.metrics import confusion_matrix
# confusion_matrix = confusion_matrix(y_test, y_pred)
# print('Confusion Matrix: \n', confusion_matrix)
#
# print(classification_report(y_test, y_pred))

# function predict the probabilites of each team winning, and return the higher team
def predict_game(high_seed, low_seed):
    if high_seed != 1 and low_seed != 1:
        # Get stats for two teams playing
        team1a = season_stats.loc[high_seed]
        team1a = team1a.loc[['eFG%','TOVp','ORBp','FTp']]

        team2a = season_stats.loc[low_seed]
        team2a = team2a.loc[['eFG%','TOVp','ORBp','FTp']]
        team2a = team2a.rename({'eFG%':'Opp_eFG%', 'TOVp':'Opp_TOVp', 'ORBp':'Opp_ORBp', 'FTp':'Opp_FTp'})

        team1b = season_stats.loc[low_seed]
        team1b = team1b.loc[['eFG%','TOVp','ORBp','FTp']]

        team2b = season_stats.loc[high_seed]
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

def create_bracket(round1):
# South Region
    try:
        round1.put('virginia')
    except KeyError:
        round1.put(1)
    try:
        round1.put('maryland-baltimore-county')
    except KeyError:
        round1.put(1)
    try:
        round1.put('creighton')
    except KeyError:
        round1.put(1)
    try:
        round1.put('kansas-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('kentucky')
    except KeyError:
        round1.put(1)
    try:
        round1.put('davidson')
    except KeyError:
        round1.put(1)
    try:
        round1.put('arizona')
    except KeyError:
        round1.put(1)
    try:
        round1.put('buffalo')
    except KeyError:
        round1.put(1)
    try:
        round1.put('miami-fl')
    except KeyError:
        round1.put(1)
    try:
        round1.put('loyola-il')
    except KeyError:
        round1.put(1)
    try:
        round1.put('tennessee')
    except KeyError:
        round1.put(1)
    try:
        round1.put('wright-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('nevada')
    except KeyError:
        round1.put(1)
    try:
        round1.put('texas')
    except KeyError:
        round1.put(1)
    try:
        round1.put('cincinnati')
    except KeyError:
        round1.put(1)
    try:
        round1.put('georgia-state')
    except KeyError:
        round1.put(1)
# West Region
    try:
        round1.put('xavier')
    except KeyError:
        round1.put(1)
    try:
        round1.put('texas-southern')
    except KeyError:
        round1.put(1)
    try:
        round1.put('missouri')
    except KeyError:
        round1.put(1)
    try:
        round1.put('florida-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('ohio-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('south-dakota-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('gonzaga')
    except KeyError:
        round1.put(1)
    try:
        round1.put('north-carolina-greensboro')
    except KeyError:
        round1.put(1)
    try:
        round1.put('houston')
    except KeyError:
        round1.put(1)
    try:
        round1.put('san-diego-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('michigan')
    except KeyError:
        round1.put(1)
    try:
        round1.put('montana')
    except KeyError:
        round1.put(1)
    try:
        round1.put('texas-am')
    except KeyError:
        round1.put(1)
    try:
        round1.put('providence')
    except KeyError:
        round1.put(1)
    try:
        round1.put('north-carolina')
    except KeyError:
        round1.put(1)
    try:
        round1.put('lipscomb')
    except KeyError:
        round1.put(1)
# East region
    try:
        round1.put('villanova')
    except KeyError:
        round1.put(1)
    try:
        round1.put('radford')
    except KeyError:
        round1.put(1)
    try:
        round1.put('virginia-tech')
    except KeyError:
        round1.put(1)
    try:
        round1.put('alabama')
    except KeyError:
        round1.put(1)
    try:
        round1.put('west-virginia')
    except KeyError:
        round1.put(1)
    try:
        round1.put('murray-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('wichita-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('marshall')
    except KeyError:
        round1.put(1)
    try:
        round1.put('florida')
    except KeyError:
        round1.put(1)
    try:
        round1.put('st-bonaventure')
    except KeyError:
        round1.put(1)
    try:
        round1.put('texas-tech')
    except KeyError:
        round1.put(1)
    try:
        round1.put(1)
    except KeyError:
        round1.put(1)
    try:
        round1.put('arkansas')
    except KeyError:
        round1  .put(1)
    try:
        round1.put('butler')
    except KeyError:
        round1.put(1)
    try:
        round1.put('purdue')
    except KeyError:
        round1.put(1)
    try:
        round1.put('cal-state-fullerton')
    except KeyError:
        round1.put(1)
# Midwest region
    try:
        round1.put('kansas')
    except KeyError:
        round1.put(1)
    try:
        round1.put('pennsylvania')
    except KeyError:
        round1.put(1)
    try:
        round1.put('seton-hall')
    except KeyError:
        round1.put(1)
    try:
        round1.put('north-carolina-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('clemson')
    except KeyError:
        round1.put(1)
    try:
        round1.put('new-mexico-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('auburn')
    except KeyError:
        round1.put(1)
    try:
        round1.put('college-of-charleston')
    except KeyError:
        round1.put(1)
    try:
        round1.put('texas-christian')
    except KeyError:
        round1.put(1)
    try:
        round1.put('syracuse')
    except KeyError:
        round1.put(1)
    try:
        round1.put('michigan-state')
    except KeyError:
        round1.put(1)
    try:
        round1.put('bucknell')
    except KeyError:
        round1.put(1)
    try:
        round1.put('rhode-island')
    except KeyError:
        round1.put(1)
    try:
        round1.put('oklahoma')
    except KeyError:
        round1.put(1)
    try:
        round1.put('duke')
    except KeyError:
        round1.put(1)
    try:
        round1.put('iona')
    except KeyError:
        round1.put(1)
    return round1

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
