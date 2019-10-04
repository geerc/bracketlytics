import pandas as pd
import numpy as np

tourney_data = pd.read_csv('/Users/christiangeer/bracketlytics/data/kaggle_data/data2/Big_Dance_CSV.csv')

tourney_data

# Append the year to the team names
tourney_data['Year'] = tourney_data['Year'].astype(str)
tourney_data['Team'] = tourney_data['Team'] + "_" + tourney_data['Year']
tourney_data['Team.1'] = tourney_data['Team.1'] + "_" + tourney_data['Year']

# Create win column based on score, and convert to int (1=team won, 0=team.1 won)
tourney_data = tourney_data.rename(columns={'Score.1':'Score_1', 'Team.1':'Team_1'})
tourney_data.loc[tourney_data.Score > tourney_data.Score_1, 'Win'] = 1
tourney_data.loc[tourney_data.Score < tourney_data.Score_1, 'Win'] = 0
tourney_data['Win'] = tourney_data['Win'].astype(int)

# Remove unnecssary columns
tourney_data.drop(tourney_data[['Year', 'Round', 'Region Number', 'Region Name', 'Seed', 'Score', 'Score_1','Seed.1']], inplace=True, axis=1)
