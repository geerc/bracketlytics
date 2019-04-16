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
dataframe = pd.read_csv(ROOT + 'data/model_data')
dataset = dataframe.values

# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]
