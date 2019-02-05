import numpy as np
import pandas as pd

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')
teams = pd.read_csv(ROOT + 'Teams.csv')
season2018 = pd.read_csv()

teams['Team_Name'] = teams['Team_Name'].str.lower()


# Get number of wins in tournament for each team, convert that series to a dataframe
teams = tourney_data.groupby(['Season','Wteam']).size()
teams = teams.to_frame()

# rename wins columns to 'wins'
teams.columns = ['wins']

# teams.to_csv(ROOT + 'teams.csv')
