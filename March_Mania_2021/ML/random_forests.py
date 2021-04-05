import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from tabulate import tabulate
import FF

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

opp_stats = pd.read_csv(root + 'data/opp_stats_2010_2020.csv')
team_stats = pd.read_csv(root + 'data/team_stats_2010_2020.csv')
tourn_stats = pd.read_csv(root + 'data/tourn_stats_2021.csv')
tourn_opp_stats = pd.read_csv(root + 'data/tourn_opp_stats_2021.csv')
wins = pd.read_csv(root + 'data/wins_2010_2020.csv')

stats = FF.four_factor(team_stats, opp_stats)
tourn_stats = FF.four_factor(tourn_stats, tourn_opp_stats)

# remove weird column
stats = stats.drop(columns=['Unnamed: 0'], axis=1)
tourn_stats = tourn_stats.drop(columns=['Unnamed: 0'], axis=1)

# merge the wins and stats
stats = stats.merge(wins, on='School')

# feature and target sets
y = stats['Wins']

X = stats.drop(columns=['School','Wins','Seed','Unnamed: 0'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

print('Training Features Shape:', X_train.shape)
print('Training Labels Shape:', y_train.shape)
print('Testing Features Shape:', X_test.shape)
print('Testing Labels Shape:', y_test.shape)

# standardize X data
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_sc = scaler.transform(X_train)
X_test_sc = scaler.transform(X_test)

# scale curr tourn data the same as hist data
tourn_stats_sc = scaler.transform(tourn_stats.iloc[:,1:])

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(X_train_sc, y_train)

# Use the forest's predict method on the test data
predictions = rf.predict(X_test_sc)
# Calculate the absolute errors
errors = abs(predictions - y_test)
# Print out the mean absolute error (mae)
result = rf.score(X_test, y_test)
print("Accuracy: %.2f%%" % (result*100.0), "\n")

# predict curr tournament
tourn_stats2 = tourn_stats.iloc[:,1:]
tourn_pred = rf.predict(tourn_stats_sc)

tourn_stats['pred wins'] = tourn_pred

print(tabulate(tourn_stats[['School','pred wins']].sort_values(by='pred wins', ascending=False),headers='tourn_stats.columns'))
tourn_stats.to_csv(root + 'Predictions/2021_RandomForests.csv')
