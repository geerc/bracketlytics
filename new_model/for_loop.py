import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/new_model/data/'

wins_cleaned = pd.read_csv(ROOT + 'wins_cleaned.csv')
data = pd.read_csv(ROOT + 'model_data.csv')

for i, j in wins_cleaned.iterrows():
    wins_cleaned_school = (j['School'])
    if wins_cleaned_school in data.School == True:
        pass
    else:
        
