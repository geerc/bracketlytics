import pandas as pd
import numpy as np

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

tourny_data = pd.read_csv(ROOT + 'tourny_games_clean.csv')

tourny_data['win'] = int(tourny_data['win'])

tourny_data['win'] = tourny_data['win'].astype(int)

tourny_data.to_csv(ROOT + 'tourny_data_10')
