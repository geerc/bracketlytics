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

# Remove teams that did not make the tournament (aldready done for non opp stats)
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
def add_opp_DRB(data):
    data['opp_DRB'] = data['opp_TRB'] - data['opp_ORB']
    data.drop(data[['opp_TRB']], inplace=True, axis=1)

def add_DRB(data):
    data['DRB'] = data['TRB'] - data['ORB']
    data.drop(data[['TRB']], inplace=True, axis=1)

add_opp_DRB(opp_2010)
add_opp_DRB(opp_2011)
add_opp_DRB(opp_2012)
add_opp_DRB(opp_2013)
add_opp_DRB(opp_2014)
add_opp_DRB(opp_2015)
add_opp_DRB(opp_2016)

add_DRB(season_2010)
add_DRB(season_2011)
add_DRB(season_2012)
add_DRB(season_2013)
add_DRB(season_2014)
add_DRB(season_2015)
add_DRB(season_2016)

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

    # Offensive free throw percentage
    data['FT%'] = data['FT'] / data['FGA']
    data[['FT%']] = data[['FT%']].round(3)

    # Defensive free throw percentage
    data['opp_FT%'] = data['opp_FT'] / data['opp_FGA']
    data[['opp_FT%']] = data[['opp_FT%']].round(3)

    # Offensive turnover percentage
    data['TOV%'] = data['TOV'] / (data['FGA'] + .44 * data['FTA'] + data['TOV'])
    data[['TOV%']] = data[['TOV%']].round(3)

    # Defensive turnover percentage
    data['opp_TOV%'] = data['opp_TOV'] / (data['opp_FGA'] + 0.44 * data['opp_FTA'] + data['opp_TOV'])
    data[['opp_TOV%']] = data[['opp_TOV%']].round(3)

# Calculate the stats
calculate_stats(data)

print(data)

# Remove unnecssary columns
data = data.drop(data.loc[:,'FG':'opp_DRB'].head(0).columns, axis=1)

data.to_csv(ROOT + 'model_data.csv')
