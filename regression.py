import pandas as pd
import numpy as np

csv_path = '/Users/Christian/Documents/Bracketlytics/data/model_data/Off_2017-18.csv'
data_2017_2018 = pd.read_csv(csv_path)
del data_2017_2018['SOS']

data_2017_2018
