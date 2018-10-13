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
df['OeFG']= (df['Opp FG'] + 0.5 * df['Opp 3P']) / df['Opp FGA']
df[['eFG', 'OeFG']] = df[['eFG', 'OeFG']].round(3)
