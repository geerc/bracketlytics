import pandas as pd
import numpy as np

# Loading data
game_data_2017 = pd.read_csv("/Users/Christian/Documents/Bracketlytics/data/game_data_2017.csv")
game_data_2018 = pd.read_csv("/Users/Christian/Documents/Bracketlytics/data/game_data_2018.csv")

game_data['Team'] = game_data['Team'].astype(str)
