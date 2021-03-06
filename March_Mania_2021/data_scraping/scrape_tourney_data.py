from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from tqdm import tqdm
import requests
import csv
import pandas as pd
from datetime import date

pbar = ProgressBar()

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

# date object for dynamically loading the year
today = date.today()

# lists for season range for regular and four factor analysis
year = [*map(str,range(1997,today.year))]
FF_year = [*map(str,range(2010, today.year))]

# combine into one list
list = [year, FF_year]

cur_year = str(today.year)

#### TODO: Write functions to handle scraping from one file
def scrape_tournaments():
    for yr in tqdm(range):

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

        # blank dataframe for current year tourn
        list_df = pd.DataFrame(list, columns=['X','Seed','School','Score','X.1'])

        # add season to dataframe
        list_df['Season'] = yr

        # drop blank columns and score
        list_df = list_df[['Seed','School','Season']]

        # get number of wins by counting how many times each school is in data
        wins = list_df.School.value_counts()
        # convert to dataframe
        wins_df = pd.DataFrame(wins)

        # reset the index to range
        wins_df = wins_df.reset_index()

        # remove duplicates so only one line item for each school
        list_nodup = list_df[['Seed','School','Season']].drop_duplicates()

        # merge the schools and their win totals
        merged = list_nodup.merge(wins_df, left_on='School', right_on='index')

        # rename the column
        merged = merged.rename(columns={'School_x':'School','School_y':'Wins'})

        # Drop second school column
        merged = merged[['Seed','School','Season','Wins']]

        # Add year suffix to school name for merging later
        merged['School'] = merged['School'].astype(str) + '_'  + yr

        # Remove now unecessary season column
        merged = merged[['Seed','School','Wins']]

        # append to the main dataframe
        tourney_data = tourney_data.append(merged)

def scrape_bbrefFF():


for range in list:
    # historical tournaments, reset dataframe for each iteration
    tourney_data = pd.DataFrame(columns=['Seed','School'])

    for yr in tqdm(range):

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

        # blank dataframe for current year tourn
        list_df = pd.DataFrame(list, columns=['X','Seed','School','Score','X.1'])

        # add season to dataframe
        list_df['Season'] = yr

        # drop blank columns and score
        list_df = list_df[['Seed','School','Season']]

        # get number of wins by counting how many times each school is in data
        wins = list_df.School.value_counts()
        # convert to dataframe
        wins_df = pd.DataFrame(wins)

        # reset the index to range
        wins_df = wins_df.reset_index()

        # remove duplicates so only one line item for each school
        list_nodup = list_df[['Seed','School','Season']].drop_duplicates()

        # merge the schools and their win totals
        merged = list_nodup.merge(wins_df, left_on='School', right_on='index')

        # rename the column
        merged = merged.rename(columns={'School_x':'School','School_y':'Wins'})

        # Drop second school column
        merged = merged[['Seed','School','Season','Wins']]

        # Add year suffix to school name for merging later
        merged['School'] = merged['School'].astype(str) + '_'  + yr

        # Remove now unecessary season column
        merged = merged[['Seed','School','Wins']]

        # append to the main dataframe
        tourney_data = tourney_data.append(merged)

    # print(len(range), '\n', len(year), '\n', len(FF_year))

    if len(range) == len(year):
        tourney_data.to_csv(root + 'data/hist_tourney.csv')
    elif len(range) == len(FF_year):
        tourney_data.to_csv(root + 'data/FF_hist_tourney.csv')
    else:
        print('You done fucked up')
        break
