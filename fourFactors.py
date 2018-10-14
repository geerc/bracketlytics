import pandas as pd
import numpy as np

csv_path = '/Users/Christian/Documents/Bracketlytics/data/2018TeamStats_Final.csv'
df = pd.read_csv(csv_path)

# Convert data from objects to floats
df = df.apply(pd.to_numeric, errors='coerce')
df[['Team']] = df[['Team']].astype("str")
df.dtypes

# Create effective field goal percentage for offense and defense
df['eFG'] = (df['FG'] + float(0.5) * df['3P']) / df['FGA']
df['oEFG']= (df['Opp FG'] + 0.5 * df['Opp 3P']) / df['Opp FGA']
df[['eFG', 'OeFG']] = df[['eFG', 'OeFG']].round(3)

# Create offensive and defensive turnover percentage
df['TOVp'] = df['TOV'] / (df['FGA'] + 0.44 + df['FTA'] + df['TOV'])
df['oTOVp'] = df['Opp TOV'] / (df['Opp FGA'] + 0.44 + df['Opp FTA'] + df['Opp TOV'])
df[['TOVp', 'oTOVp']] = df[['TOVp', 'oTOVp']].round(3)

# Create offensive and defensive rebounding percentage
df['ORBp'] = df['ORB'] / (df['ORB'] + df['Opp DRB'])
df['DRBp'] = df['DRB'] / (df['DRB'] + df['Opp DRB'])
df[['ORBp', 'DRBP']] = df[['ORBp', 'DRBP']].round(3)

# Create offensive and defensive free throw percentage
df['FTp'] = df['FT'] / df['FGA']
df['oFTp'] = df['Opp FT'] / df['Opp FGA']
df[['FTp', 'oFTp']] = df[['FTp', 'oFTp']].round(3)

df[0:5]
