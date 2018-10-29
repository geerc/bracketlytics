import pandas as pd
import numpy as np


# Loading data
game_data = pd.read_csv("/Users/Christian/Documents/Bracketlytics/data/2018TeamStats_Final.csv")

game_data['Team'] = game_data['Team'].astype(str)

game_data.dtypes

# Create offensive and defensive turnover percentage
game_data['TOVp'] = game_data['TOV'] / (game_data['FGA'] + 0.44 + game_data['FTA'] + game_data['TOV'])
game_data['oTOVp'] = game_data['Opp.TOV'] / (game_data['Opp.FGA'] + 0.44 + game_data['Opp.FTA'] + game_data['Opp.TOV'])
game_data[['TOVp', 'oTOVp']] = game_data[['TOVp', 'oTOVp']].round(3)

# Create offensive and defensive rebounding percentage
game_data['ORBp'] = game_data['ORB'] / (game_data['ORB'] + game_data['Opp.DRB'])
game_data['DRBp'] = game_data['DRB'] / (game_data['DRB'] + game_data['Opp.DRB'])
game_data[['ORBp', 'DRBp']] = game_data[['ORBp', 'DRBp']].round(3)

# Create offensive and defensive free throw percentage
game_data['FTp'] = game_data['FT'] / game_data['FGA']
game_data['oFTp'] = game_data['Opp.FT'] / game_data['Opp.FGA']
game_data[['FTp', 'oFTp']] = game_data[['FTp', 'oFTp']].round(3)
