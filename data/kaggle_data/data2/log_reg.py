import numpy as np
import pandas as pd
import seaborn as sb

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from functions2 import *

round2 = Queue()
round3 = Queue()
round4 = Queue()
round5 = Queue()
round6 = Queue()
round7 = Queue()

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

data = pd.read_csv(ROOT + 'combined_data.csv')
data_2019 = pd.read_csv(ROOT + 'combined_data_2019.csv')
season_stats = pd.read_csv(ROOT + 'advanced_stats.csv')

round1 = functions.create_bracket()

# Round 1
