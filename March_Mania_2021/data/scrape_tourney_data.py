from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from tqdm import tqdm
import requests
import csv

pbar = ProgressBar()

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

# create empty list to add teams
list = []

list of seasons
year = list(map(str,range(1993,2021)))

for yr in tqdm(year):

    URL = 'https://www.sports-reference.com/cbb/postseason/{}-ncaa.html'.format(yr)
    # URL = 'https://www.sports-reference.com/cbb/postseason/2000-ncaa.html'
    page = requests.get(URL)

    # create BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')

    # loops through all winner div tags, pulls text, and splits by '\n', appends to the list
    for div in soup.find_all('div', class_='winner'):
        text = div.text
        split = text.split('\n')
        list.append(split)
        # list.append(yr)

# write the list to csv
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(list)

# for winner in winners:
#     print(winner, end='\n'*2)
# print(winners)
