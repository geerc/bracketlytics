import statsmodels.api as sm
import numpy as np
import pandas as pd
import csv

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/data/kaggle_data/'

# Import data
df = pd.read_csv(ROOT + 'final_data.csv')

# define the data/predictors as the pre-set feature names
df = pd.DataFrame(df.data, columns=df.feature_names)

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=["MEDV"])


with open('employee_birthday.txt') as csv_file:
    
