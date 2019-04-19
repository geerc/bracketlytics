import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/new_model/data/'

wins_cleaned = pd.read_csv(ROOT + 'wins_cleaned.csv')
data = pd.read_csv(ROOT + 'model_data.csv')

for i, j in wins_cleaned.iterrows():
    wins_cleaned_school = (j['School'])
    if data['School'].str.contains(wins_cleaned_school).any():
        pass
    else:
        # Pass the row elements as key value pairs to append() function
        modDfObj = wins_cleaned.append({'Team_Id': 0, 'School' : wins_cleaned_school , 'wins' : 0} , ignore_inex=True)

print(modDfObj)
modDfObj = wins_cleaned.append({'School' : "Nova 2020" , 'wins' : 0} , ignore_index=True)
