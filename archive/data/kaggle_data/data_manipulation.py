import numpy as np
import pandas as pd

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')
teams = pd.read_csv(ROOT + 'Teams.csv')
wins = pd.read_csv(ROOT + 'wins.csv')
# season2018 = pd.read_csv()

# teams['Team_Name'] = teams['Team_Name'].str.lower()
wins['Season'] = wins['Season'].astype(str)
wins['Team_Id'] = wins['Team_Id'].astype(str)

wins['team'] = wins['Season'] + '_' + wins['Team_Id']
print(wins)

teams_full = teams.join(wins, how='left', on='Team_Id')

print(teams_full)
