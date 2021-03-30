# import pandas as pd
# from bs4 import BeautifulSoup as bs
# import requests
# import pprint as pp
# from progressbar import ProgressBar
# from tqdm import tqdm
# pbar = ProgressBar()
#
# pd.options.display.max_columns=1999
#
# root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'
#
# BASE_URL = 'https://www.sports-reference.com/cbb/seasons/YEAR-school-stats.html'
# YEAR = list(map(str,range(1993,2020)))
#
# all_stats = pd.DataFrame(columns=['School','G','W','L','W-L%','SRS','SOS','DELETE','W','L','DELETE','W','L','DELETE','W','L','DELETE','Tm.','Opp.','DELETE','MP','FG','FGA','FG%','3P','3PA','3P%','FT','FTA','FT%','ORB','DRB','AST','STL','BLK','TOV','PF'])
# # breakpoint()
# for yr in tqdm(YEAR):
#     page = requests.get(BASE_URL.replace('YEAR',yr))
#     # print(BASE_URL.replace('YEAR',yr))
#     # page = requests.get(BASE_URL.replace('YEAR','1987'))
#     soup = bs(page.content, 'html.parser')
#
#     # avoid the rows above table
#     rows = soup.findAll('tr', limit=2)
#
#     yr_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
#     # pp.pprint(these_games)
#     yr_stats = pd.DataFrame(yr_stats,columns=['School','G','W','L','W-L%','SRS','SOS','DELETE','W','L','DELETE','W','L','DELETE','W','L','DELETE','Tm.','Opp.','DELETE','MP','FG','FGA','FG%','3P','3PA','3P%','FT','FTA','FT%','ORB','DRB','AST','STL','BLK','TOV','PF'])
#     yr_stats['Season'] = yr
#     print(yr_stats)
#     # all_stats = all_stats.append(yr_stats)
#     # pd.concat((yr_stats,all_stats), ignore_index=True)
#
#     # pp.pprint(all_games)
# # these_games.head()
# # all_games.tail()
#
# all_stats.to_csv(root + 'data/bbref.csv')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from tqdm import tqdm

pbar = ProgressBar()

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

teams = pd.read_csv(root + 'data/MTeams.csv')

# Seasons we will be analyzing
year = list(map(str,range(1997,2021)))
cur_year = str(2021)

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
    if yr == '1997':
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


# write new csv
all_stats.to_csv(root + "data/hist_bbref.csv")

# URL page we will scraping (see image above)
url = "https://www.sports-reference.com/cbb/seasons/{}-school-stats.html".format(cur_year)
# url = "https://www.sports-reference.com/cbb/seasons/2000-school-stats.html"
opp_url = "https://www.sports-reference.com/cbb/seasons/{}-opponent-stats.html".format(cur_year)

# this is the HTML from the given URL
html = urlopen(url)
opp_html = urlopen(opp_url)

soup = BeautifulSoup(html, features='lxml') #features ensures runs the same on different systems
opp_soup = BeautifulSoup(opp_html, features='lxml')

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
opp_soup.findAll('tr', limit=2)

# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
opp_headers = [th.getText() for th in opp_soup.findAll('tr', limit=2)[1].findAll('th')]

# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
opp_headers = opp_headers[1:]

# create blank dataframe, need to do here to get headers
curr_stats = pd.DataFrame(columns=headers)
opp_curr_stats = pd.DataFrame(columns=opp_headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
team_stats = [[td.getText() for td in rows[i].findAll('td')]
        for i in range(len(rows))]
stats = pd.DataFrame(team_stats, columns = headers)

opp_rows = opp_soup.findAll('tr')[1:]
opp_tm_stats = [[td.getText() for td in rows[i].findAll('td')]
        for i in range(len(rows))]
opp_stats = pd.DataFrame(opp_tm_stats, columns=opp_headers)

# drop na/none values
stats = stats.dropna(axis='rows')
opp_stats = opp_stats.dropna(axis='rows')

curr_tourn = stats[stats.School.str.contains("NCAA")]
curr_tourn = curr_tourn.copy()
curr_tourn_opp = opp_stats[opp_stats.School.str.contains("NCAA")]
curr_tourn_opp = curr_tourn_opp.copy()

# remove the ncaa suffix
stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)
curr_tourn['School'] = curr_tourn['School'].replace(" NCAA$", "", regex=True)
opp_stats['School'] = opp_stats['School'].replace("NCAA", "", regex=True)
curr_tourn_opp['School'] = curr_tourn_opp['School'].replace("NCAA", "", regex=True)

# stats['School'].to_csv(root + 'data/stats.csv')
# teams.to_csv(root + 'data/MTeams.csv')

# merged = pd.merge(stats, teams, on='School', how='left')
# merged[['School','TeamID']].to_csv(root + 'data/merged.csv')


# add year to the end of each school name
stats['School'] = stats['School'].astype(str) + '_'  + cur_year
opp_stats['School'] = stats['School'].astype(str) + '_' + cur_year

# append to dataframe
curr_stats = curr_stats.append(stats)
opp_curr_stats = opp_curr_stats.append(opp_stats)

# write to csv
# curr_stats.to_csv(root + 'data/curr_bbref.csv')
curr_tourn.to_csv(root + 'data/curr_tourn.csv')
curr_tourn_opp.to_csv(root + 'data/curr_tourn_opp.csv')
