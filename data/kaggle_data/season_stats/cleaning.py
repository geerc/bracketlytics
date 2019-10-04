import pandas as pd
import numpy as np

ROOT = '/Users/christiangeer/bracketlytics/data/kaggle_data/season_stats/'

# Read in team data as dataframes
team_2010 = pd.read_csv(ROOT + '2010.csv')
team_2011 = pd.read_csv(ROOT + '2011.csv')
team_2012 = pd.read_csv(ROOT + '2012.csv')
team_2013 = pd.read_csv(ROOT + '2013.csv')
team_2014 = pd.read_csv(ROOT + '2014.csv')
team_2015 = pd.read_csv(ROOT + '2015.csv')
team_2016 = pd.read_csv(ROOT + '2016.csv')
team_2017 = pd.read_csv(ROOT + '2017.csv')
team_2018 = pd.read_csv(ROOT + '2018.csv')
team_2019 = pd.read_csv(ROOT + '2019.csv')

# Read in opposing team data as dataframes
opp_2010 = pd.read_csv(ROOT + 'opp_2010.csv')
opp_2011 = pd.read_csv(ROOT + 'opp_2011.csv')
opp_2012 = pd.read_csv(ROOT + 'opp_2012.csv')
opp_2013 = pd.read_csv(ROOT + 'opp_2013.csv')
opp_2014 = pd.read_csv(ROOT + 'opp_2014.csv')
opp_2015 = pd.read_csv(ROOT + 'opp_2015.csv')
opp_2016 = pd.read_csv(ROOT + 'opp_2016.csv')
opp_2017 = pd.read_csv(ROOT + 'opp_2017.csv')
opp_2018 = pd.read_csv(ROOT + 'opp_2018.csv')
opp_2019 = pd.read_csv(ROOT + 'opp_2019.csv')

# Remove the teams that did not make the tournament
team_2010 = team_2010[team_2010.School.str.contains("NCAA")]
team_2011 = team_2011[team_2011.School.str.contains("NCAA")]
team_2012 = team_2012[team_2012.School.str.contains("NCAA")]
team_2013 = team_2013[team_2013.School.str.contains("NCAA")]
team_2014 = team_2014[team_2014.School.str.contains("NCAA")]
team_2015 = team_2015[team_2015.School.str.contains("NCAA")]
team_2016 = team_2016[team_2016.School.str.contains("NCAA")]
team_2017 = team_2017[team_2017.School.str.contains("NCAA")]
team_2018 = team_2018[team_2018.School.str.contains("NCAA")]
team_2019 = team_2019[team_2019.School.str.contains("NCAA")]
opp_2010 = opp_2010[opp_2010.School.str.contains("NCAA")]
opp_2011 = opp_2011[opp_2011.School.str.contains("NCAA")]
opp_2012 = opp_2012[opp_2012.School.str.contains("NCAA")]
opp_2013 = opp_2013[opp_2013.School.str.contains("NCAA")]
opp_2014 = opp_2014[opp_2014.School.str.contains("NCAA")]
opp_2015 = opp_2015[opp_2015.School.str.contains("NCAA")]
opp_2016 = opp_2016[opp_2016.School.str.contains("NCAA")]
opp_2017 = opp_2017[opp_2017.School.str.contains("NCAA")]
opp_2018 = opp_2018[opp_2018.School.str.contains("NCAA")]
opp_2019 = opp_2019[opp_2019.School.str.contains("NCAA")]

# Remove NCAA suffix
team_2010['School'] = team_2010['School'].replace("NCAA$", "2010", regex=True)
team_2011['School'] = team_2011['School'].replace("NCAA$", "2011", regex=True)
team_2012['School'] = team_2012['School'].replace("NCAA$", "2012", regex=True)
team_2013['School'] = team_2013['School'].replace("NCAA$", "2013", regex=True)
team_2014['School'] = team_2014['School'].replace("NCAA$", "2014", regex=True)
team_2015['School'] = team_2015['School'].replace("NCAA$", "2015", regex=True)
team_2016['School'] = team_2016['School'].replace("NCAA$", "2016", regex=True)
team_2017['School'] = team_2017['School'].replace("NCAA$", "2017", regex=True)
team_2018['School'] = team_2018['School'].replace("NCAA$", "2018", regex=True)
team_2019['School'] = team_2019['School'].replace("NCAA$", "2019", regex=True)
opp_2010['School'] = opp_2010['School'].replace("NCAA$", "2010", regex=True)
opp_2011['School'] = opp_2011['School'].replace("NCAA$", "2011", regex=True)
opp_2012['School'] = opp_2012['School'].replace("NCAA$", "2012", regex=True)
opp_2013['School'] = opp_2013['School'].replace("NCAA$", "2013", regex=True)
opp_2014['School'] = opp_2014['School'].replace("NCAA$", "2014", regex=True)
opp_2015['School'] = opp_2015['School'].replace("NCAA$", "2015", regex=True)
opp_2016['School'] = opp_2016['School'].replace("NCAA$", "2016", regex=True)
opp_2017['School'] = opp_2017['School'].replace("NCAA$", "2017", regex=True)
opp_2018['School'] = opp_2018['School'].replace("NCAA$", "2018", regex=True)
opp_2019['School'] = opp_2019['School'].replace("NCAA$", "2019", regex=True)

team_2010.to_csv(ROOT + '2010_clean.csv')
team_2011.to_csv(ROOT + '2011_clean.csv')
team_2012.to_csv(ROOT + '2012_clean.csv')
team_2013.to_csv(ROOT + '2013_clean.csv')
team_2014.to_csv(ROOT + '2014_clean.csv')
team_2015.to_csv(ROOT + '2015_clean.csv')
team_2016.to_csv(ROOT + '2016_clean.csv')
team_2017.to_csv(ROOT + '2017_clean.csv')
team_2018.to_csv(ROOT + '2018_clean.csv')
team_2019.to_csv(ROOT + '2019_clean.csv')
opp_2010.to_csv(ROOT + 'opp_2010_clean.csv')
opp_2011.to_csv(ROOT + 'opp_2011_clean.csv')
opp_2012.to_csv(ROOT + 'opp_2011_clean.csv')
opp_2013.to_csv(ROOT + 'opp_2012_clean.csv')
opp_2014.to_csv(ROOT + 'opp_2013_clean.csv')
opp_2015.to_csv(ROOT + 'opp_2014_clean.csv')
opp_2016.to_csv(ROOT + 'opp_2016_clean.csv')
opp_2017.to_csv(ROOT + 'opp_2017_clean.csv')
opp_2018.to_csv(ROOT + 'opp_2018_clean.csv')
opp_2019.to_csv(ROOT + 'opp_2019_clean.csv')
