import pandas as pd
import numpy as np

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'
results = pd.read_csv(root + 'data/MNCAATourneyCompactResults.csv')

results_grouped = results.groupby(by='Season')
print(results_grouped)
