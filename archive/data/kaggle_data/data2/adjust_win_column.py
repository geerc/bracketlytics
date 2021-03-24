import pandas as pd
import numpy as np

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

tourny_data = pd.read_csv(ROOT + 'tourny_games_clean.csv')
# print(tourny_data)

tourny_data['win'] = tourny_data['win'].astype(int)

# tourny_data.drop(tourny_data[['Unnamed: 0', 'Unnamed: 0.1','Year']], inplace=True, axis=1)

# Add year suffix
tourny_data['Year'] = tourny_data['Year'].astype(str)
tourny_data['Team'] = tourny_data['Team'] + "_" + tourny_data['Year']
tourny_data['Team 1'] = tourny_data['Team 1'] + "_" + tourny_data['Year']


tourny_data.to_csv(ROOT + 'tourny_data_10.csv')
