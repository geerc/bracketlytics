import pandas as pd
import numpy as np

ROOT = ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

season_data = pd.read_csv(ROOT + 'advanced_stats.csv')
tourny_games = pd.read_csv(ROOT + 'tourny_data_10.csv')

# print(season_data)
print(tourny_games)

# Cast year as string so it can be concatanated
tourny_games['Year'] = tourny_games['Year'].astype(str)

# Add year suffix to Team
tourny_games['Team'] = tourny_games['Team'].astype(str) + " " + tourny_games['Year']

# Add year suffix to Team 1
tourny_games['Team 1'] = tourny_games['Team 1'].astype(str) + " " + tourny_games['Year']
