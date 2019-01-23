import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')
teams = pd.read_csv(ROOT + 'Teams.csv')

teams['Team_Name'] = teams['Team_Name'].str.lower()

# Calculate advanced statistics
#### Create effective field goal percentage for offense and defense
tourney_data['Wefg%'] = (tourney_data['Wfgm'] + float(0.5) * tourney_data['Wfgm3']) / tourney_data['Wfga']
tourney_data['Lefg%'] = (tourney_data['Lfgm'] + float(0.5) * tourney_data['Lfgm3']) / tourney_data['Lfga']
tourney_data[['Wefg%', 'Lefg']] = tourney_data[['Wefg%', 'Lefg%']].round(3)

#### Create offensive and defensive turnover percentage
tourney_data['Wtov%'] = tourney_data['Wto'] / (tourney_data['Wfga'] + 0.44 + tourney_data['Wfta'] + tourney_data['Wto'])
tourney_data['Ltov%'] = tourney_data['Lto'] / (tourney_data['Lfga'] + 0.44 + tourney_data['Lfta'] + tourney_data['Lto'])
tourney_data[['Wtov%', 'Ltov%']] = tourney_data[['Wtov%', 'Ltov%']].round(3)

#### Create offensive and defensive rebounding percentage
tourney_data['Wor%'] = tourney_data['Wor'] / (tourney_data['Wor'] + tourney_data['Ldr'])
tourney_data['Wdr%'] = tourney_data['Wdr'] / (tourney_data['Wdr'] + tourney_data['Lor'])
tourney_data['Lor%'] = tourney_data['Lor'] / (tourney_data['Lor'] + tourney_data['Wdr'])
tourney_data['Ldr%'] = tourney_data['Ldr'] / (tourney_data['Ldr'] + tourney_data['Wor'])
tourney_data[['Wor%', 'Wdr%']] = tourney_data[['Wor%', 'Wdr%']].round(3)

#### Create offensive and defensive free throw percentage
tourney_data['Wft%'] = tourney_data['Wftm'] / tourney_data['Wfga']
tourney_data['Lft%'] = tourney_data['Lftm'] / tourney_data['Lfga']
tourney_data[['Wft%', 'Lft%']] = tourney_data[['Wft%', 'Lft%']].round(3)

tourney_data.drop(tourney_data[['Lteam','Daynum','Wscore','Lscore','Wloc','Numot','Wfgm','Wfga','Wfgm3','Wfga3','Wftm','Wfta','Wor','Wdr','Wast','Wto','Wstl','Wblk','Wpf','Lfgm','Lfga','Lfgm3','Lfga3','Lftm','Lfta','Lor','Ldr','Last','Lto','Lstl','Lblk','Lpf']], inplace=True, axis=1)

# Get number of wins in tournament for each team, convert that series to a dataframe
teams = tourney_data.groupby(['Season','Wteam']).size()
teams = teams.to_frame()

# Isolate each team from each season
tourney_data = tourney_data.groupby(['Season','Wteam']).mean()

# Add wins to tourney_data and rename the newly added column
tourney_data = tourney_data.join(teams, how = 'left')
tourney_data.columns = ['Wefg%','Lefg%','Lefg','Wtov%','Ltov%','Wor%','Wdr%','Lor%','Ldr%','Wft%','Lft%','wins']

# rename wins columns t0 'wins'
teams.columns = ['wins']

# Write new data to csv
tourney_data.to_csv(ROOT + 'new_tourney_data.csv')
teams.to_csv(ROOT + 'wins.csv')
