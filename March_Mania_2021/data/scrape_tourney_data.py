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

tourney_data = pd.DataFrame(columns=['X','Seed','School','Score','X.1'])

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
        # list.append(yr)

    # write the list to csv
    # with open("output.csv", "w") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(list)

    list_df = pd.DataFrame(list, columns=['X','Seed','School','Score','X.1'])
    # print(list_df)
    list_df['Season'] = yr
    # print(list_df)
    tourney_data = tourney_data.append(list_df)
    # print(tourney_data)
    # list_df.to_csv('my_csv.csv', mode='a', header=False)
    # print(list_df)

tourney_data.to_csv(root + 'data/tourney_data.csv')



# for winner in winners:
#     print(winner, end='\n'*2)
# print(winners)
