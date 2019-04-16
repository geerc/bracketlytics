import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/new_model/data/'

season_2010 = pd.read_csv(ROOT + '/2010.csv')
season_2011 = pd.read_csv(ROOT + '/2011.csv')
season_2012 = pd.read_csv(ROOT + '/2012.csv')
season_2013 = pd.read_csv(ROOT + '/2013.csv')
season_2014 = pd.read_csv(ROOT + '/2014.csv')
season_2015 = pd.read_csv(ROOT + '/2015.csv')
season_2016 = pd.read_csv(ROOT + '/2016.csv')
opp_2016 = pd.read_csv(ROOT + '/opp_2016.csv')
opp_2015 = pd.read_csv(ROOT + '/opp_2015.csv')
opp_2014 = pd.read_csv(ROOT + '/opp_2014.csv')
opp_2013 = pd.read_csv(ROOT + '/opp_2013.csv')
opp_2012 = pd.read_csv(ROOT + '/opp_2012.csv')
opp_2011 = pd.read_csv(ROOT + '/opp_2011.csv')
opp_2010 = pd.read_csv(ROOT + '/opp_2010.csv')
wins_cleaned = pd.read_csv(ROOT + 'wins_cleaned.csv')

# Remove teams that did not make the tournament
opp_2010 = opp_2010[opp_2010.School.str.contains("NCAA")]
opp_2011 = opp_2011[opp_2011.School.str.contains("NCAA")]
opp_2012 = opp_2012[opp_2012.School.str.contains("NCAA")]
opp_2013 = opp_2013[opp_2013.School.str.contains("NCAA")]
opp_2014 = opp_2014[opp_2014.School.str.contains("NCAA")]
opp_2015 = opp_2015[opp_2015.School.str.contains("NCAA")]
opp_2016 = opp_2016[opp_2016.School.str.contains("NCAA")]

# Remove NCAA suffix
season_2010['School'] = season_2010['School'].replace("NCAA$", "2010", regex=True)
opp_2010['School'] = opp_2010['School'].replace("NCAA$", "2010", regex=True)
season_2011['School'] = season_2011['School'].replace("NCAA$", "2011", regex=True)
opp_2011['School'] = opp_2011['School'].replace("NCAA$", "2011", regex=True)
season_2012['School'] = season_2012['School'].replace("NCAA$", "2012", regex=True)
opp_2012['School'] = opp_2012['School'].replace("NCAA$", "2012", regex=True)
season_2013['School'] = season_2013['School'].replace("NCAA$", "2013", regex=True)
opp_2013['School'] = opp_2013['School'].replace("NCAA$", "2013", regex=True)
season_2014['School'] = season_2014['School'].replace("NCAA$", "2014", regex=True)
opp_2014['School'] = opp_2014['School'].replace("NCAA$", "2014", regex=True)
season_2015['School'] = season_2015['School'].replace("NCAA$", "2015", regex=True)
opp_2015['School'] = opp_2015['School'].replace("NCAA$", "2015", regex=True)
season_2016['School'] = season_2016['School'].replace("NCAA$", "2016", regex=True)
opp_2016['School'] = opp_2016['School'].replace("NCAA$", "2016", regex=True)

# Add DRB column and remove TRB
opp_2016['opp_DRB'] = opp_2016['opp_TRB'] - opp_2016['opp_ORB']
opp_2016.drop(opp_2016[['opp_TRB']], inplace=True, axis=1)

opp_2015['opp_DRB'] = opp_2015['opp_TRB'] - opp_2015['opp_ORB']
opp_2015.drop(opp_2015[['opp_TRB']], inplace=True, axis=1)

opp_2014['opp_DRB'] = opp_2014['opp_TRB'] - opp_2014['opp_ORB']
opp_2014.drop(opp_2014[['opp_TRB']], inplace=True, axis=1)

opp_2013['opp_DRB'] = opp_2013['opp_TRB'] - opp_2013['opp_ORB']
opp_2013.drop(opp_2013[['opp_TRB']], inplace=True, axis=1)

opp_2012['opp_DRB'] = opp_2012['opp_TRB'] - opp_2012['opp_ORB']
opp_2012.drop(opp_2012[['opp_TRB']], inplace=True, axis=1)

opp_2011['opp_DRB'] = opp_2011['opp_TRB'] - opp_2011['opp_ORB']
opp_2011.drop(opp_2011[['opp_TRB']], inplace=True, axis=1)

opp_2010['opp_DRB'] = opp_2010['opp_TRB'] - opp_2010['opp_ORB']
opp_2010.drop(opp_2010[['opp_TRB']], inplace=True, axis=1)

# write csv files to be joined in tableu prep, then brought back for calculations
season_2010.to_csv(ROOT + '2010_new.csv')
season_2011.to_csv(ROOT + '2011_new.csv')
season_2012.to_csv(ROOT + '2012_new.csv')
season_2013.to_csv(ROOT + '2013_new.csv')
season_2014.to_csv(ROOT + '2014_new.csv')
season_2015.to_csv(ROOT + '2015_new.csv')
season_2016.to_csv(ROOT + '2016_new.csv')

opp_2010.to_csv(ROOT + 'opp_2010_new.csv')
opp_2011.to_csv(ROOT + 'opp_2011_new.csv')
opp_2012.to_csv(ROOT + 'opp_2012_new.csv')
opp_2013.to_csv(ROOT + 'opp_2013_new.csv')
opp_2014.to_csv(ROOT + 'opp_2014_new.csv')
opp_2015.to_csv(ROOT + 'opp_2015_new.csv')
opp_2016.to_csv(ROOT + 'opp_2016_new.csv')

data = pd.read_csv(ROOT + 'pre_calc_data.csv')

print(data)

# Calculate advanced statistics to be used for regression
def calculate_stats(data):
    # Effective field goal percentage
    data['EFG%'] = (data['FG'] + float(0.5) * data['3P']) / data['FGA']
    data[['EFG%']] = data[['EFG%']].round(3)

    # Opponet effective field goal percentage
    data['opp_EFG%'] = (data['opp_FG'] + float(0.5) * data['opp_3P']) / data['opp_FGA']
    data[['opp_EFG%']] = data[['opp_EFG%']].round(3)

    # Offensive rebounding percentage
    data['ORB%'] = data['ORB'] / (data['ORB'] + data['opp_DRB'])
    data[['ORB%']] = data[['ORB%']].round(3)

    # Defensive rebounding percentage
    data['DRB%'] = data['DRB'] / (data['DRB'] + data['opp_ORB'])
    data[['DRB%']] = data[['DRB%']].round(3)

    #

efg_pct(data)
opp_efg_pct(data)

#### Create offensive and defensive free throw percentage
tourney_data['Wft%'] = tourney_data['Wftm'] / tourney_data['Wfga']
tourney_data['Lft%'] = tourney_data['Lftm'] / tourney_data['Lfga']
tourney_data[['Wft%', 'Lft%']] = tourney_data[['Wft%', 'Lft%']].round(3)

tourney_data.drop(tourney_data[['Lteam','Daynum','Wscore','Lscore','Wloc','Numot','Wfgm','Wfga','Wfgm3','Wfga3','Wftm','Wfta','Wor','Wdr','Wast','Wto','Wstl','Wblk','Wpf','Lfgm','Lfga','Lfgm3','Lfga3','Lftm','Lfta','Lor','Ldr','Last','Lto','Lstl','Lblk','Lpf']], inplace=True, axis=1)

# Get number of wins in tournament for each team, convert that series to a dataframe
team_wins = tourney_data.groupby(['Season','Wteam']).size()
print(team_wins)
print(teams)
team_wins.columns = ['wins']
team_wins = team_wins.to_frame()
teams_and_wins = team_wins.join(teams, how='left')


# Isolate each team from each season
tourney_data = tourney_data.groupby(['Season','Wteam']).mean()
print(teams)

# Add wins to tourney_data and rename the newly added column
tourney_data = tourney_data.join(teams, how = 'left')
tourney_data.columns = ['Wefg%','Lefg%','Lefg','Wtov%','Ltov%','Wor%','Wdr%','Lor%','Ldr%','Wft%','Lft%','wins']

# rename wins columns to 'wins'teams.columns = ['wins']
print(teams)


# Create advanced stats for final_data.csv
#### Create effective field goal percentage for offense and defense
final_data['efg%'] = (final_data['FG'] + float(0.5) * final_data['3P']) / final_data['Wfga']
final_data[['efg%']] = final_data[['Wefg%']].round(3)


#### Create offensive and defensive turnover percentage
final_data['tov%'] = final_data['TOV'] / (final_data['FGA'] + 0.44 + final_data['FTA'] + final_data['TOV'])
final_data[['tov%']] = final_data[['tov%']].round(3)

#### Create offensive and defensive rebounding percentage
final_data['or%'] = final_data['ORB'] / (final_data['ORB'] + final_data['DRB'])
final_data['dr%'] = final_data['DRB'] / (final_data['DRB'] + final_data['ORD'])
final_data[['or%', 'dr%']] = final_data[['or%', 'dr%']].round(3)

#### Create offensive and defensive free throw percentage
final_data['Wft%'] = final_data['Wftm'] / final_data['Wfga']
final_data['Lft%'] = final_data['Lftm'] / final_data['Lfga']
final_data[['Wft%', 'Lft%']] = final_data[['Wft%', 'Lft%']].round(3)

final_data.drop(final_data[['Lteam','Daynum','Wscore','Lscore','Wloc','Numot','Wfgm','Wfga','Wfgm3','Wfga3','Wftm','Wfta','Wor','Wdr','Wast','Wto','Wstl','Wblk','Wpf','Lfgm','Lfga','Lfgm3','Lfga3','Lftm','Lfta','Lor','Ldr','Last','Lto','Lstl','Lblk','Lpf']], inplace=True, axis=1)


# Write new data to csv
tourney_data.to_csv(ROOT + 'new_tourney_data.csv')
teams.to_csv(ROOT + 'wins.csv')
season_2003.to_csv(ROOT + 'season_stats/2003.csv')
season_2004.to_csv(ROOT + 'season_stats/2004.csv')
season_2005.to_csv(ROOT + 'season_stats/2005.csv')
season_2006.to_csv(ROOT + 'season_stats/2006.csv')
season_2007.to_csv(ROOT + 'season_stats/2007.csv')
season_2008.to_csv(ROOT + 'season_stats/2008.csv')
season_2009.to_csv(ROOT + 'season_stats/2009.csv')
season_2010.to_csv(ROOT + 'season_stats/2010.csv')
opp_2010.to_csv(ROOT + 'season_stats/opp_2010.csv')
season_2011.to_csv(ROOT + 'season_stats/2011.csv')
opp_2011.to_csv(ROOT + 'season_stats/opp_2011.csv')
season_2012.to_csv(ROOT + 'season_stats/2012.csv')
opp_2012.to_csv(ROOT + 'season_stats/opp_2012.csv')
season_2013.to_csv(ROOT + 'season_stats/2013.csv')
opp_2013.to_csv(ROOT + 'season_stats/opp_2013.csv')
season_2014.to_csv(ROOT + 'season_stats/2014.csv')
opp_2014.to_csv(ROOT + 'season_stats/opp_2014.csv')
season_2015.to_csv(ROOT + 'season_stats/2015.csv')
opp_2015.to_csv(ROOT + 'season_stats/opp_2015.csv')
season_2016.to_csv(ROOT + 'season_stats/2016.csv')
opp_2016.to_csv(ROOT + 'season_stats/opp_2016.csv')
full_data.to_csv(ROOT + 'full_season_data_cleaned.csv')
wins.to_csv(ROOT + 'wins_cleaned.csv')
