import pandas as pd
import numpy as np

root = "/Users/christiangeer/bracketlytics/March_Mania_2021/"
seeds = pd.read_csv(root + "data/MNCAATourneySeeds.csv")
teams = pd.read_csv(root + "data/MTeams.csv")
