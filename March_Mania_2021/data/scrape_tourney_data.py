from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from tqdm import tqdm
import requests
import csv
import pandas as pd

pbar = ProgressBar()

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'


# list of seasons
year = [*map(str,range(1993,2021))]

tourney_data = pd.DataFrame(columns=['Seed','School','Season'])

for yr in tqdm(year):

    URL = 'https://www.sports-reference.com/cbb/postseason/{}-ncaa.html'.format(yr)
    # URL = 'https://www.sports-reference.com/cbb/postseason/2000-ncaa.html'
    page = requests.get(URL)

    # create BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # create empty list to add teams, gets rewrote each loop
    list = []

    # loops through all winner div tags, pulls text, and splits by '\n', appends to the list
    for div in soup.find_all('div', class_='winner'):
        text = div.text
        split = text.split('\n')
        list.append(split)

    list_df = pd.DataFrame(list, columns=['X','Seed','School','Score','X.1'])
    # print(list_df)
    list_df['Season'] = yr
    # print(list_df)
    list_df = list_df[['Seed','School','Season','Score']]

    wins = list_df.School.value_counts()
    wins_df = pd.DataFrame(wins)
    print(wins_df)
    wins_df = wins_df.reset_index()
    print(wins_df)
    # print(type(wins_df))
    # wins_df.rename(columns={'index':'School','School':'Wins'})
    # print(wins_df)

    tourney_data = tourney_data.append(list_df)

tourney_data.to_csv(root + 'data/tourney_data.csv')



# for winner in winners:
#     print(winner, end='\n'*2)
# print(winners)
