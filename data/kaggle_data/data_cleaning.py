import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/Bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')

# Calculate advanced statistics
#### Create effective field goal percentage for offense and defense
tourney_data['Wefg%'] = (tourney_data['Wfgm'] + float(0.5) * tourney_data['Wfgm3']) / tourney_data['Wfga']
tourney_data['Lefg%'] = (tourney_data['Lfgm'] + float(0.5) * tourney_data['Lfgm3']) / tourney_data['Lfga']
tourney_data[['Wefg%', 'Lefg']] = tourney_data[['Wefg%', 'Lefg%']].round(3)

#### Create offensive and defensive turnover percentage
tourney_data['Wtov%'] = tourney_data['Wto'] / (tourney_data['Wfga'] + 0.44 + tourney_data['Wfta'] + tourney_data['Wto'])
tourney_data['Ltov%'] = tourney_data['Lto'] / (tourney_data['Lfga'] + 0.44 + tourney_data['Lfta'] + tourney_data['Lto'])
tourney_data[['Wtov%', 'Ltov%']] = tourney_data[['Wtov%', 'Ltov%']].round(3)

#### Create offensive and defensive rebounding percentage
tourney_data['ORBp'] = tourney_data['ORB'] / (tourney_data['ORB'] + tourney_data['Opp DRB'])
tourney_data['DRBp'] = tourney_data['DRB'] / (tourney_data['DRB'] + tourney_data['Opp DRB'])
tourney_data[['ORBp', 'DRBp']] = tourney_data[['ORBp', 'DRBp']].round(3)

#### Create offensive and defensive free throw percentage
tourney_data['FTp'] = tourney_data['FT'] / tourney_data['FGA']
tourney_data['Opp FTp'] = tourney_data['Opp FT'] / tourney_data['Opp FGA']
tourney_data[['FTp', 'Opp FTp']] = tourney_data[['FTp', 'Opp FTp']].round(3)
