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
# YEAR = list(map(str,range(1987,2020)))
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
#     all_stats = all_stats.append(all_stats)
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


# Seasons we will be analyzing
year = list(map(str,range(1987,2020)))

# URL page we will scraping (see image above)
url = "https://www.sports-reference.com/cbb/seasons/{}-school-stats.html".format(year)
# url = "https://www.sports-reference.com/cbb/seasons/2000-school-stats.html"

for yr in tqdm(year):

    # this is the HTML from the given URL
    html = urlopen(url)

    soup = BeautifulSoup(html, features='lxml') #features ensures runs the same on different systems

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis

    headers = headers[1:]
    headers

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
    stats = pd.DataFrame(team_stats, columns = headers)
    stats['Season'] = yr

    stats.head(10)

# write new csv
stats.to_csv(root + "data/bbref.csv")
