import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import pandas as pd
import seaborn as sb
import functions
from queue import *

from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

class MyLogger(K.callbacks.Callback):
  def __init__(self, n):
    self.n = n   # print loss & acc every n epochs

  def on_epoch_end(self, epoch, logs={}):
    if epoch % self.n == 0:
      curr_loss =logs.get('loss')
      curr_acc = logs.get('acc') * 100
      print("epoch = %4d  loss = %0.6f  acc = %0.2f%%" % \
        (epoch, curr_loss, curr_acc))

round1 = Queue()
round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

ROOT = '/Users/Christian/Documents/cs310f2018/project-cmpsc-310-fall-2018-allegheny-college-craig-engels-fan-club'

game_data = pd.read_csv(ROOT + '/data/2018TeamStats_Final.csv')
season_stats = pd.read_csv(ROOT + '/data/season_data.csv')
sos = pd.read_csv(ROOT + '/data/sos.csv')

# Remove unnecassary columns
game_data.drop(labels=['gameid','Opp PTS','PF','Opp PF','Rank','MP','FG%','2P','2PA','2P%','3PA','3P%','FT%','TRB','AST','STL','BLK','PTS','Opp FG%','Opp 2P','Opp 2PA','Opp 2P%','Opp 3PA','Opp 3P%','Opp FT%','Opp TRB','Opp AST','Opp STL','Opp BLK'], inplace=True, axis=1)
season_stats.drop(labels=['X.11','X.10','X.9','X.8','X.7','X.6','X.5','X.4','X.3','X.2','X.1','X','Rank','SOS'], inplace=True, axis=1)
sos.drop(labels=['Unnamed: 0','X.11','X.10','X.9','X.8','X.7','X.6','X.5','X.4','X.3','X.2','X.1','X','Rank'], inplace=True, axis=1)
# print(sos)
# sos['SOS'] = sos['SOS'] + 12.48
# sos.sort_values(by=['SOS'])

# Set team as index
season_stats.set_index('Team', inplace=True)
sos.set_index('Team', inplace=True)

# Convert to lower case
sos.index = sos.index.str.lower()

# Convert stat variables to numeric
game_data['FG'] = game_data['FG'].apply(pd.to_numeric, errors='coerce')
game_data['FGA'] = game_data['FGA'].apply(pd.to_numeric, errors='corerce')
game_data['3P'] = game_data['3P'].apply(pd.to_numeric, errors='coerce')
game_data['FT'] = game_data['FT'].apply(pd.to_numeric, errors='coerce')
game_data['FTA'] = game_data['FTA'].apply(pd.to_numeric, errors='coerce')
game_data['ORB'] = game_data['ORB'].apply(pd.to_numeric, errors='coerce')
game_data['DRB'] = game_data['DRB'].apply(pd.to_numeric, errors='coerce')
game_data['TOV'] = game_data['TOV'].apply(pd.to_numeric, errors='coerce')
game_data['Win?'] = game_data['Win?'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FG'] = game_data['Opp FG'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FGA'] = game_data['Opp FGA'].apply(pd.to_numeric, errors='corerce')
game_data['Opp 3P'] = game_data['Opp 3P'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FT'] = game_data['Opp FT'].apply(pd.to_numeric, errors='coerce')
game_data['Opp FTA'] = game_data['Opp FTA'].apply(pd.to_numeric, errors='coerce')
game_data['Opp ORB'] = game_data['Opp ORB'].apply(pd.to_numeric, errors='coerce')
game_data['Opp DRB'] = game_data['Opp DRB'].apply(pd.to_numeric, errors='coerce')
game_data['Opp TOV'] = game_data['Opp TOV'].apply(pd.to_numeric, errors='coerce')

functions.create_stats(game_data)
functions.create_stats(season_stats)

# Drop unnecassary columns
game_data.drop(labels=['FG','FGA','3P','FT','FTA','ORB','DRB','TOV','Opp FG','Opp FGA','Opp 3P','Opp FT','Opp FTA','Opp ORB','Opp DRB','Opp TOV'], inplace=True, axis=1)
season_stats.drop(labels=['Unnamed: 0','FG','FGA','3P','FT','FTA','ORB','DRB','TOV','Opp FG','Opp FGA','Opp 3P','Opp FT','Opp FTA','Opp ORB','Opp DRB','Opp TOV'], inplace=True, axis=1)

X = game_data.iloc[:,2:10].values
y = game_data.iloc[:,1].values

# Create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state=25)

X_train = pd.DataFrame(X)
y_train = pd.DataFrame(y)

# Remove na values
X_train = X_train.dropna(axis=0, how='all')
y_train = y_train.drop(y_train.index[5282])

print(X_train)

# Configure model
my_init = keras.initializers.glorot_uniform(seed=1)
model = keras.models.Sequential()
model.add(keras.layers.Dense(units=8, input_dim=8, activation='tanh', kernel_initializer=my_init))
model.add(keras.layers.Dense(units=8, activation='tanh', kernel_initializer=my_init))
model.add(keras.layers.Dense(units=1, activation='sigmoid', kernel_initializer=my_init))

# Compiling the model
simple_sgd = keras.optimizers.SGD(lr=0.01)
model.compile(loss='binary_crossentropy', optimizer=simple_sgd, metrics=['accuracy'])

# Fitting the model
model.fit(X_train, y_train, epochs=5, batch_size=150)

max_epochs = 500
my_logger = MyLogger(n=50)
h = model.fit(train_x, train_y, batch_size=32, epochs=max_epochs, verbose=0, callbacks=[my_logger])

# Save the model
mp = ROOT + "/data/model.h5"
model.save(mp)

# Evaluating and uses trained model
np.set_printoptions(precision=4, suppress=True)
eval_results = model.evaluate(test_x, test_y, verbose=0)
print("\nLoss, accuracy on test data: ")
print("%0.4f %0.2f%%" % (eval_results[0], eval_results[1]*100))

# Evaluating the model on the test set
score = model.evaluate(X_test, y_test)

# Printing the accuracy score of the model over the test set
print('\nModel {}: {}'.format(model.metrics_names[1], score[1]))
