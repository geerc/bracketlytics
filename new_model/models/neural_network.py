import numpy
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/new_model/'

# load dataset
dataframe = pd.read_csv(ROOT + 'data/joined_data.csv')
dataset = dataframe.values

# split into input (X) and output (Y) variables
X = dataset[:,1:9]
Y = dataset[:,10]

# define base model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal'))
	# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam')
	return model
