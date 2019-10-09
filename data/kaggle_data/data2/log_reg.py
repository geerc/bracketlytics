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

# Cast wins as int
data['win'] = data['win'].astype(int)

print(data['win'])
