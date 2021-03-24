import pandas as pd
import numpy as np

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'
results = pd.read_csv(root + 'data/MNCAATourneyCompactResults.csv')

# results.groupby(['Season']).mean()
results_grouped = pd.MultiIndex.from_frame(results)

results_grouped = results.groupby(['Season',"WTeamID"]).nunique()

print(results_grouped)
