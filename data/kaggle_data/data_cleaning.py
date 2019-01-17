import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/Bracketlytics/data/kaggle_data/'

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

# Replace change Wteam to team_id to allow for join
tourney_data = tourney_data.rename(columns={'Wteam':'Team_Id'})
print(tourney_data)

tourney_data.join(teams, on='Team_Id')


tourney_data = tourney_data.join(teams, on=)
