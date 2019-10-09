import pandas as pd
import numpy as np

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/data2/'

season_data = pd.read_csv(ROOT + 'season_data.csv')
advanced_stats = pd.concat([season_data['School'], season_data['SOS']], axis=1)

# print(season_data)
# print(advanced_stats.to_string())

# Effective field goal percetenge (off and def)
advanced_stats['efg%'] = (season_data['FG'] + float(0.5) * season_data['3P']) / season_data['FGA']
advanced_stats['def_efg%'] = (season_data['opp_FG'] + float(0.5) * season_data['opp_3P']) / season_data['opp_FGA']
advanced_stats[['efg%', 'def_efg%']] = advanced_stats[['efg%', 'def_efg%']].round(3)

# Turnover percentage (off and def)
advanced_stats['tov%'] = season_data['TOV'] / (season_data['FGA'] + 0.44 + season_data['FTA'] + season_data['TOV'])
advanced_stats['def_tov%'] = season_data['opp_TOV'] / (season_data['opp_FGA'] + 0.44 + season_data['opp_FTA'] + season_data['opp_TOV'])
advanced_stats[['tov%', 'def_tov%']] = advanced_stats[['tov%', 'def_tov%']].round(3)

# Rebounding percenteage (off and def)
advanced_stats['orb%'] = season_data['ORB'] / (season_data['ORB'] + season_data['DRB'])
advanced_stats['drb%'] = season_data['DRB'] / (season_data['ORB'] + season_data['ORB'])
advanced_stats[['orb%', 'drb%']] = advanced_stats[['orb%', 'drb%']].round(3)

# Free throw percentage (off and def)
advanced_stats['ft%'] = season_data['FT'] / season_data['FGA']
advanced_stats['def_ft%'] = season_data['opp_FT'] / season_data['opp_FTA']
advanced_stats[['ft%', 'def_ft%']] = advanced_stats[['ft%', 'def_ft%']].round(3)

# Write advanced_stats to file
advanced_stats.to_csv(ROOT + 'advanced_stats.csv')
