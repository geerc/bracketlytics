from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from tqdm import tqdm

pbar = ProgressBar()

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

teams = pd.read_csv(root + 'data/MTeams.csv')

# Seasons we will be analyzing
year = list(map(str,range(2010,2021)))
cur_year = str(2021)

# team stats
for yr in tqdm(year):
    # URL page we will scraping (see image above)
    url = "https://www.sports-reference.com/cbb/seasons/{}-school-stats.html".format(yr)
    # url = "https://www.sports-reference.com/cbb/seasons/2000-school-stats.html"

    # this is the HTML from the given URL
    html = urlopen(url)

    soup = BeautifulSoup(html, features='lxml') #features ensures runs the same on different systems

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis

    headers = headers[1:]

    # if its the first year, create blank dataframe, need to do here to get headers
    if yr == '2010':
        all_stats = pd.DataFrame(columns=headers)

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
    stats = pd.DataFrame(team_stats, columns = headers)

    # drop na/none values
    stats = stats.dropna(axis='rows')

    # remove the ncaa suffix
    stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)

    # stats['School'].to_csv(root + 'data/stats.csv')
    # teams.to_csv(root + 'data/MTeams.csv')

    # merged = pd.merge(stats, teams, on='School', how='left')
    # merged[['School','TeamID']].to_csv(root + 'data/merged.csv')


    # add year to the end of each school name
    stats['School'] = stats['School'].astype(str) + '_'  + yr

    # append to dataframe
    all_stats = all_stats.append(stats)

for yr in tqdm(year):
    # URL page we will scraping (see image above)
    url = "https://www.sports-reference.com/cbb/seasons/{}-opponent-stats.html".format(yr)
    # url = "https://www.sports-reference.com/cbb/seasons/2000-school-stats.html"

    # this is the HTML from the given URL
    html = urlopen(url)

    soup = BeautifulSoup(html, features='lxml') #features ensures runs the same on different systems

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis

    headers = headers[1:]

    # if its the first year, create blank dataframe, need to do here to get headers
    if yr == '2010':
        opp_stats = pd.DataFrame(columns=headers)

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
    stats = pd.DataFrame(team_stats, columns = headers)

    # drop na/none values
    stats = stats.dropna(axis='rows')

    # remove the ncaa suffix
    stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)

    # stats['School'].to_csv(root + 'data/stats.csv')
    # teams.to_csv(root + 'data/MTeams.csv')

    # merged = pd.merge(stats, teams, on='School', how='left')
    # merged[['School','TeamID']].to_csv(root + 'data/merged.csv')


    # add year to the end of each school name
    stats['School'] = stats['School'].astype(str) + '_'  + yr

    # append to dataframe
    opp_stats = opp_stats.append(stats)



# write new csvs
all_stats.to_csv(root + "data/FF_hist_bbref.csv")
opp_stats.to_csv(root + "data/FF_hist_bbref_opp.csv")


# CURRENT TOURNAMENT FIELD

# TEAM STATS
# URL page we will scraping (see image above)
url = "https://www.sports-reference.com/cbb/seasons/{}-school-stats.html".format(cur_year)
# url = "https://www.sports-reference.com/cbb/seasons/2000-school-stats.html"

# this is the HTML from the given URL
html = urlopen(url)

soup = BeautifulSoup(html, features='lxml') #features ensures runs the same on different systems

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis

headers = headers[1:]

# create blank dataframe, need to do here to get headers
curr_stats = pd.DataFrame(columns=headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
team_stats = [[td.getText() for td in rows[i].findAll('td')]
        for i in range(len(rows))]
stats = pd.DataFrame(team_stats, columns = headers)

# drop na/none values
stats = stats.dropna(axis='rows')

curr_tourn = stats[stats.School.str.contains("NCAA")]
curr_tourn = curr_tourn.copy()

# remove the ncaa suffix
stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)
curr_tourn['School'] = curr_tourn['School'].replace(" NCAA$", "", regex=True)

# add year to the end of each school name
stats['School'] = stats['School'].astype(str) + '_'  + cur_year

# append to dataframe
curr_stats = curr_stats.append(stats)

# write to csv
# curr_stats.to_csv(root + 'data/curr_bbref.csv')
curr_tourn.to_csv(root + 'data/curr_tourn.csv')
