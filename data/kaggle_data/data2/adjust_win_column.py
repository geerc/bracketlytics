import pandas as pd
import numpy as np

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

tourny_data = pd.read_csv(ROOT + 'tourney_games_wsuffix.csv')
print(tourny_data)

# tourny_data['win'] = tourny_data['win'].astype(int)

tourny_data.drop(tourny_data[['Unnamed: 0', 'Unnamed: 0.1','Year']], inplace=True, axis=1)

tourny_data.to_csv(ROOT + 'tourny_data_10.csv')
