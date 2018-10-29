import pandas as pd
import numpy as np


# Loading data
game_data = pd.read_csv("/Users/Christian/Documents/Bracketlytics/data/game_data.csv")
game_data

game_data['Team'] = game_data['Team'].astype(str)
