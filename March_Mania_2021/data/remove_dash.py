import pandas as pd
import numpy as np

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'
data = pd.read_csv(root + 'data/season_data.csv')

# Replace dashes with spaces to make easier joining
data['Team'] = data.Team.str.replace('-', ' ')
