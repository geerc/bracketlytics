import pandas as pd

# load Data
total_2017_2018 = pd.read_csv('/Users/Christian/Documents/Bracketlytics/data/model_data/total_2017_2018.csv')

# Add year to school name
total_2017_2018['School'].add_suffix('_2018')

total_2017_2018
