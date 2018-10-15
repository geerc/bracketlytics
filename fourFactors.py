import pandas as pd
import numpy as np

csv_path = '/Users/Christian/Documents/Bracketlytics/data/season_data.csv'
sos_path = '/Users/Christian/Documents/Bracketlytics/data/sos.csv'
sos = pd.read_csv(sos_path)
df = pd.read_csv(csv_path)

# Create effective field goal percentage for offense and defense
df['eFG'] = (df['FG'] + float(0.5) * df['X3P']) / df['FGA']
df['oEFG']= (df['Opp.FG'] + 0.5 * df['Opp.3P']) / df['Opp.FGA']
df[['eFG', 'oEFG']] = df[['eFG', 'oEFG']].round(3)

df['Team'] = df['Team'].astype(str)
sos['Team'] = sos['Team'].astype(str)
# Create offensive and defensive turnover percentage
df['TOVp'] = df['TOV'] / (df['FGA'] + 0.44 + df['FTA'] + df['TOV'])
df['oTOVp'] = df['Opp.TOV'] / (df['Opp.FGA'] + 0.44 + df['Opp.FTA'] + df['Opp.TOV'])
df[['TOVp', 'oTOVp']] = df[['TOVp', 'oTOVp']].round(3)

# Create offensive and defensive rebounding percentage
df['ORBp'] = df['ORB'] / (df['ORB'] + df['Opp.DRB'])
df['DRBp'] = df['DRB'] / (df['DRB'] + df['Opp.DRB'])
df[['ORBp', 'DRBp']] = df[['ORBp', 'DRBp']].round(3)

# Create offensive and defensive free throw percentage
df['FTp'] = df['FT'] / df['FGA']
df['oFTp'] = df['Opp.FT'] / df['Opp.FGA']
df[['FTp', 'oFTp']] = df[['FTp', 'oFTp']].round(3)

# Create column for team score
df['score'] = 0

## Determine scores for Off eFG%
# Sort by eFG%, reset and renumber index/rank
df = df.sort_values('eFG')
df = df.reset_index(drop = True)
df['Rank'] = df.index + 1

# Create and add scores
df['Off eFG Score'] = df['Rank'] * 0.4 * df['SOS']
df['score'] += df['Rank'] * 0.4 * df['SOS']

## Determine scores for def eFG%
# Sort by OeFG%, reset and renumber index/rank
df = df.sort_values('oEFG')
df = df.reset_index(drop = True)
df['Rank'] = df.index + 1

# Create and add scores
df['Def eFG score'] = df['Rank'] * 0.4 * df['SOS']
df['score'] += df['Rank'] * 0.4 * df['SOS']

## Determine scores for offensive turnovers
# Sort by TOV, reset and renumber index/rank
df = df.sort_values('TOV')
df = df.reset_index(drop = True)
df['Rank'] = df.index + 1

# Create and add scores
df['Off TOV score'] = df['Rank'] * 0.25 * df['SOS']
df['score'] += df['Rank'] * 0.25 * df['SOS']

## Determine scores for defensive turnovers
df = df.sort_values('TOV')
df = df.reset_index(drop = True)
df['Rank'] = df.index + 1

# Create and add scores




df = df.sort_values('score', ascending = False)
df
