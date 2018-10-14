import pandas as pd
import numpy as np

csv_path = '/Users/Christian/Documents/Bracketlytics/data/2018TeamStats_Final.csv'
sos_path = '/Users/Christian/Documents/Bracketlytics/data/bf.csv'
df = pd.read_csv(csv_path)
sos = pd.read_csv(bf_path)

# Drop uncessary columns
df = df.drop(['FG%', '3P%', '2P', '2PA', '2P%', 'TRB', 'AST'], axis = 1)
df = df.drop(['STL', 'BLK', 'PF', 'PTS', 'Opp FG%', 'Opp 2P', 'Opp 2PA'], axis = 1)
df = df.drop(['Opp 2P%', 'Opp TRB', 'Opp AST', 'Opp STL', 'Opp BLK', 'Opp PF', 'Opp PTS'], axis = 1)
df = df.drop(['FT%', 'Opp FT%', 'Opp 3P%', 'MP', 'Win?', 'gameid', '3PA'], axis = 1)
df = df.drop(['Opp 3PA'], axis = 1)
df[0:5]

# Convert data from objects to floats
df[['FG']] = df[['FG']].apply(pd.to_numeric, errors = 'corerce')
df[['FGA']] = df[['FGA']].apply(pd.to_numeric, errors = 'corerce')
df[['3P']] = df[['3P']].apply(pd.to_numeric, errors = 'corerce')
df[['FT']] = df[['FT']].apply(pd.to_numeric, errors = 'corerce')
df[['ORB']] = df[['ORB']].apply(pd.to_numeric, errors = 'corerce')
df[['DRB']] = df[['DRB']].apply(pd.to_numeric, errors = 'corerce')
df[['TOV']] = df[['TOV']].apply(pd.to_numeric, errors = 'corerce')
df[['FTA']] = df[['FTA']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp FG']] = df[['Opp FG']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp FGA']] = df[['Opp FGA']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp 3P']] = df[['Opp 3P']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp FT']] = df[['Opp FT']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp ORB']] = df[['Opp ORB']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp DRB']] = df[['Opp DRB']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp TOV']] = df[['Opp TOV']].apply(pd.to_numeric, errors = 'corerce')
df[['Opp FTA']] = df[['Opp FTA']].apply(pd.to_numeric, errors = 'corerce')

# Create effective field goal percentage for offense and defense
df['eFG'] = (df['FG'] + float(0.5) * df['3P']) / df['FGA']
df['oEFG']= (df['Opp FG'] + 0.5 * df['Opp 3P']) / df['Opp FGA']
df[['eFG', 'oEFG']] = df[['eFG', 'oEFG']].round(3)

# Create offensive and defensive turnover percentage
df['TOVp'] = df['TOV'] / (df['FGA'] + 0.44 + df['FTA'] + df['TOV'])
df['oTOVp'] = df['Opp TOV'] / (df['Opp FGA'] + 0.44 + df['Opp FTA'] + df['Opp TOV'])
df[['TOVp', 'oTOVp']] = df[['TOVp', 'oTOVp']].round(3)

# Create offensive and defensive rebounding percentage
df['ORBp'] = df['ORB'] / (df['ORB'] + df['Opp DRB'])
df['DRBp'] = df['DRB'] / (df['DRB'] + df['Opp DRB'])
df[['ORBp', 'DRBp']] = df[['ORBp', 'DRBp']].round(3)

# Create offensive and defensive free throw percentage
df['FTp'] = df['FT'] / df['FGA']
df['oFTp'] = df['Opp FT'] / df['Opp FGA']
df[['FTp', 'oFTp']] = df[['FTp', 'oFTp']].round(3)
bf[0:5]

# Create column for team score
bf['score'] = 0

# Determine team eFGp points
bf = df.sort_values('eFG%')
bf = df.reset_index(drop = True)
bf['Rank'] = df.index + 1

bf['score'] = bf['score'] + (bf['Rank'] * 0.4 * bf[''])
bf[:5]
