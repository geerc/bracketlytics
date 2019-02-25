import pandas as pd
import numpy as np

ROOT = '/Users/Christian/Documents/GitHub/bracketlytics/data/kaggle_data/'

tourney_data = pd.read_csv(ROOT + 'TourneyDetailedResults.csv')
teams = pd.read_csv(ROOT + 'Teams.csv')
season_2003 = pd.read_csv(ROOT + '/season_stats/2003.csv')
season_2004 = pd.read_csv(ROOT + '/season_stats/2004.csv')
season_2005 = pd.read_csv(ROOT + '/season_stats/2005.csv')
season_2006 = pd.read_csv(ROOT + '/season_stats/2006.csv')
season_2007 = pd.read_csv(ROOT + '/season_stats/2007.csv')
season_2008 = pd.read_csv(ROOT + '/season_stats/2008.csv')
season_2009 = pd.read_csv(ROOT + '/season_stats/2009.csv')
season_2010 = pd.read_csv(ROOT + '/season_stats/2010.csv')
season_2011 = pd.read_csv(ROOT + '/season_stats/2011.csv')
season_2012 = pd.read_csv(ROOT + '/season_stats/2012.csv')
season_2013 = pd.read_csv(ROOT + '/season_stats/2013.csv')
season_2014 = pd.read_csv(ROOT + '/season_stats/2014.csv')
season_2015 = pd.read_csv(ROOT + '/season_stats/2015.csv')
season_2016 = pd.read_csv(ROOT + '/season_stats/2016.csv')
opp_2016 = pd.read_csv(ROOT + '/season_stats/opp_2016.csv')
opp_2015 = pd.read_csv(ROOT + '/season_stats/opp_2015.csv')
opp_2014 = pd.read_csv(ROOT + '/season_stats/opp_2014.csv')
opp_2013 = pd.read_csv(ROOT + '/season_stats/opp_2013.csv')
opp_2012 = pd.read_csv(ROOT + '/season_stats/opp_2012.csv')
opp_2011 = pd.read_csv(ROOT + '/season_stats/opp_2011.csv')
opp_2010 = pd.read_csv(ROOT + '/season_stats/opp_2010.csv')
full_data = pd.read_csv(ROOT + 'full_season_data.csv')
wins = pd.read_csv(ROOT + 'wins.csv')
wins_cleaned = pd.read_csv(ROOT + 'wins_cleaned.csv')
final_data = pd.read_csv(ROOT + 'final_data.csv')

# Remove teams that did not make the tournament
season_2003 = season_2003[season_2003.School.str.contains("NCAA")]
season_2004 = season_2004[season_2004.School.str.contains("NCAA")]
season_2005 = season_2005[season_2005.School.str.contains("NCAA")]
season_2006 = season_2006[season_2006.School.str.contains("NCAA")]
season_2007 = season_2007[season_2007.School.str.contains("NCAA")]
season_2008 = season_2008[season_2008.School.str.contains("NCAA")]
season_2009 = season_2009[season_2009.School.str.contains("NCAA")]
season_2010 = season_2010[season_2010.School.str.contains("NCAA")]
opp_2010 = opp_2010[opp_2010.School.str.contains("NCAA")]
season_2011 = season_2011[season_2011.School.str.contains("NCAA")]
opp_2011 = opp_2011[opp_2011.School.str.contains("NCAA")]
season_2012 = season_2012[season_2012.School.str.contains("NCAA")]
opp_2012 = opp_2012[opp_2012.School.str.contains("NCAA")]
season_2013 = season_2013[season_2013.School.str.contains("NCAA")]
opp_2013 = opp_2013[opp_2013.School.str.contains("NCAA")]
season_2014 = season_2014[season_2014.School.str.contains("NCAA")]
opp_2014 = opp_2014[opp_2014.School.str.contains("NCAA")]
season_2015 = season_2015[season_2015.School.str.contains("NCAA")]
opp_2015 = opp_2015[opp_2015.School.str.contains("NCAA")]
season_2016 = season_2016[season_2016.School.str.contains("NCAA")]
opp_2016 = opp_2016[opp_2016.School.str.contains("NCAA")]

# Remove NCAA suffix
season_2003['School'] = season_2003['School'].replace("NCAA$", "2003", regex=True)
season_2004['School'] = season_2004['School'].replace("NCAA$", "2004", regex=True)
season_2005['School'] = season_2005['School'].replace("NCAA$", "2005", regex=True)
season_2006['School'] = season_2006['School'].replace("NCAA$", "2006", regex=True)
season_2007['School'] = season_2007['School'].replace("NCAA$", "2007", regex=True)
season_2008['School'] = season_2008['School'].replace("NCAA$", "2008", regex=True)
season_2009['School'] = season_2009['School'].replace("NCAA$", "2009", regex=True)
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
opp_2016['opp_DRB'] = opp_2016['TRB'] - opp_2016['ORB']
opp_2016.drop(opp_2016[['TRB']], inplace=True, axis=1)
opp_2016.columns = ['School','opp_ORB','opp_DRB']

opp_2015['DRB'] = opp_2015['TRB'] - opp_2015['ORB']
opp_2015.drop(opp_2015[['TRB']], inplace=True, axis=1)
opp_2015.columns = ['School','opp_ORB','opp_DRB']

opp_2014['DRB'] = opp_2014['TRB'] - opp_2014['ORB']
opp_2014.drop(opp_2014[['TRB']], inplace=True, axis=1)
opp_2014.columns = ['School','opp_ORB','opp_DRB']

opp_2013['DRB'] = opp_2013['TRB'] - opp_2013['ORB']
opp_2013.drop(opp_2013[['TRB']], inplace=True, axis=1)
opp_2013.columns = ['School','opp_ORB','opp_DRB']

opp_2012['DRB'] = opp_2012['TRB'] - opp_2012['ORB']
opp_2012.drop(opp_2012[['TRB']], inplace=True, axis=1)
opp_2012.columns = ['School','opp_ORB','opp_DRB']

opp_2011['DRB'] = opp_2011['TRB'] - opp_2011['ORB']
opp_2011.drop(opp_2011[['TRB']], inplace=True, axis=1)
opp_2011.columns = ['School','opp_ORB','opp_DRB']

opp_2010['DRB'] = opp_2010['TRB'] - opp_2010['ORB']
opp_2010.drop(opp_2010[['TRB']], inplace=True, axis=1)
opp_2010.columns = ['School','opp_ORB','opp_DRB']

# Remove unnecssary columns
full_data.drop(full_data[['Table Names-1','Table Names']], inplace=True, axis=1)

# Added year suffix to wins.to_csv and remove unnecssary columns
wins['Season'] = wins['Season'].astype(str)

wins['team'] = wins['Team_Name'] + " " + wins['Season']

wins = wins.drop(wins[['Season','Team_Id-1','Team_Name']], axis=1)

# Convert team names to lower case
teams['Team_Name'] = teams['Team_Name'].str.lower()

# Calculate advanced statistics (tourney_data)
#### Create effective field goal percentage for offense and defense
tourney_data['Wefg%'] = (tourney_data['Wfgm'] + float(0.5) * tourney_data['Wfgm3']) / tourney_data['Wfga']
tourney_data['Lefg%'] = (tourney_data['Lfgm'] + float(0.5) * tourney_data['Lfgm3']) / tourney_data['Lfga']
tourney_data[['Wefg%', 'Lefg']] = tourney_data[['Wefg%', 'Lefg%']].round(3)


#### Create offensive and defensive turnover percentage
tourney_data['Wtov%'] = tourney_data['Wto'] / (tourney_data['Wfga'] + 0.44 + tourney_data['Wfta'] + tourney_data['Wto'])
tourney_data['Ltov%'] = tourney_data['Lto'] / (tourney_data['Lfga'] + 0.44 + tourney_data['Lfta'] + tourney_data['Lto'])
tourney_data[['Wtov%', 'Ltov%']] = tourney_data[['Wtov%', 'Ltov%']].round(3)

#### Create offensive and defensive rebounding percentage
tourney_data['Wor%'] = tourney_data['Wor'] / (tourney_data['Wor'] + tourney_data['Ldr'])
tourney_data['Wdr%'] = tourney_data['Wdr'] / (tourney_data['Wdr'] + tourney_data['Lor'])
tourney_data['Lor%'] = tourney_data['Lor'] / (tourney_data['Lor'] + tourney_data['Wdr'])
tourney_data['Ldr%'] = tourney_data['Ldr'] / (tourney_data['Ldr'] + tourney_data['Wor'])
tourney_data[['Wor%', 'Wdr%']] = tourney_data[['Wor%', 'Wdr%']].round(3)

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
