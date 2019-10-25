import numpy as np
import pandas as pd
import seaborn as sb
import functions
from queue import *

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

round1 = Queue()
round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

data = pd.read_csv(ROOT + 'combined_data.csv')
data_2019 = pd.read_csv(ROOT + 'combined_data_2019.csv')
# print(data.to_string())

X = data.iloc[:,3:21]
y = data.iloc[:,2]

# Create training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=25)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)

# Remove na values (there shouldn't be any, but just in case)
X_train = X_train.dropna(axis=1, how='all')
y_trian = y_train.dropna(axis=1, how='all')

# Create and fit LogisticRegression
LogReg = LogisticRegression(solver='lbfgs', max_iter=200) # Specify solver to satifsy future warning on default solver change
LogReg.fit(X_train, y_train.values.ravel())

predictions_2019 = LogReg.predict(data_2019.iloc[[1],3:21])
print(predictions_2019)

# iterate over rows with iterrows()
# for index in predictions_2019:
#      # access data using column names
#      print(data['Team'] + " VS. " + data['Team_1'] + " \n \t " + index.astype(str))


# for x in range(len(predictions_2019)):
#     data_2019['prediction'] = predictions_2019[x]

# def predict_game(Team, Team_1):
#     data_2019.set_index('Team', inplace=True)
#
#     team = data_2019.loc[Team]
#     print(team)
#     team = team.iloc[:,3:]
#
#     team1 = data_2019.loc[Team_1]
#     team1 = team1.iloc[:,3:]
#
#     print(team + " " + team1)





print(data_2019.to_string())
