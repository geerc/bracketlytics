import pandas as pd
import numpy as np

ROOT = ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

season_data = pd.read_csv(ROOT + 'advanced_stats.csv')
tourny_games = pd.read_csv(ROOT + 'tourny_data_10.csv')
