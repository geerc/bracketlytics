import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/Bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')

# Calculate advanced statistics
#### Create effective field goal percentage for offense and defense
tourney_data['WeFG%'] = (tourney_data['Wfgm'] + float(0.5) * tourney_data['Wfgm3']) / tourney_data['Wfga']
tourney_data['Opp eFG%'] = (tourney_data['Opp FG'] + 0.5 * tourney_data['Opp 3P']) / tourney_data['Opp FGA']
tourney_data[['eFG%', 'Opp eFG%']] = tourney_data[['eFG%', 'Opp eFG%']].round(3)

#### Create offensive and defensive turnover percentage
tourney_data['TOVp'] = tourney_data['TOV'] / (tourney_data['FGA'] + 0.44 + tourney_data['FTA'] + tourney_data['TOV'])
tourney_data['Opp TOVp'] = tourney_data['Opp TOV'] / (tourney_data['Opp FGA'] + 0.44 + tourney_data['Opp FTA'] + tourney_data['Opp TOV'])
tourney_data[['TOVp', 'Opp TOVp']] = tourney_data[['TOVp', 'Opp TOVp']].round(3)

#### Create offensive and defensive rebounding percentage
tourney_data['ORBp'] = tourney_data['ORB'] / (tourney_data['ORB'] + tourney_data['Opp DRB'])
tourney_data['DRBp'] = tourney_data['DRB'] / (tourney_data['DRB'] + tourney_data['Opp DRB'])
tourney_data[['ORBp', 'DRBp']] = tourney_data[['ORBp', 'DRBp']].round(3)

#### Create offensive and defensive free throw percentage
tourney_data['FTp'] = tourney_data['FT'] / tourney_data['FGA']
tourney_data['Opp FTp'] = tourney_data['Opp FT'] / tourney_data['Opp FGA']
tourney_data[['FTp', 'Opp FTp']] = tourney_data[['FTp', 'Opp FTp']].round(3)
