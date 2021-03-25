import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pprint as pp
from progressbar import ProgressBar
from tqdm import tqdm
pbar = ProgressBar()

pd.options.display.max_columns=1999

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

BASE_URL = 'https://www.sports-reference.com/cbb/seasons/YEAR-school-stats.html'
YEAR = list(map(str,range(1987,2020)))

all_stats = pd.DataFrame(columns=['School','G','W','L','W-L%','SRS','SOS','DELETE','W','L','DELETE','W','L','DELETE','W','L','DELETE','Tm.','Opp.','DELETE','MP','FG','FGA','FG%','3P','3PA','3P%','FT','FTA','FT%','ORB','DRB','AST','STL','BLK','TOV','PF'])
# breakpoint()
for yr in tqdm(YEAR):
    page = requests.get(BASE_URL.replace('YEAR',yr))
    # print(BASE_URL.replace('YEAR',yr))
    # page = requests.get(BASE_URL.replace('YEAR','1987'))
    soup = bs(page.content, 'html.parser')

    # avoid the rows above table
    rows = soup.findAll('tr')[:]

    yr_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    # pp.pprint(these_games)
    yr_stats = pd.DataFrame(yr_stats,columns=['School','G','W','L','W-L%','SRS','SOS','DELETE','W','L','DELETE','W','L','DELETE','W','L','DELETE','Tm.','Opp.','DELETE','MP','FG','FGA','FG%','3P','3PA','3P%','FT','FTA','FT%','ORB','DRB','AST','STL','BLK','TOV','PF'])
    yr_stats['Season'] = yr
    all_stats = all_stats.append(all_stats)
    # pp.pprint(all_games)
# these_games.head()
# all_games.tail()

all_stats.to_csv(root + 'bbref.csv')
