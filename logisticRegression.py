import pandas as pd
import numpy as np
from sklearn_model import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Loading data
game_data = pd.read_csv("/Users/Christian/Documents/Bracketlytics/data/game_data.csv")
game_data

game_data['Team'] = game_data['Team'].astype(str)

game_data = data_final.columns.values.tolist()
y=['Win']
X=[i for i in fame_data if i not in y]

logreg = LogisticRegression()
rfe = RFE(logreg, 20)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)
