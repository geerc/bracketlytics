from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from tqdm import tqdm
from progressbar import ProgressBar
import requests


# creating progressbar
pbar = ProgressBar()

# create date object to get current year
today = date.today()


# variables
years = [*map(str,range(2010,2021))]
# start_year = input("Start year: ")
# end_year = input("End year: ")
curr_year = str(today.year)
curr_year_int = today.year
root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

def scrape_wins(seasons):

    # years = [*map(str,range(start_year,end_year))]

    # historical tournaments, reset dataframe for each iteration
    tourney_data = pd.DataFrame(columns=['Seed','School'])

    for yr in tqdm(seasons):
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

    return tourney_data

def scrape_team_stats(seasons):

    for yr in tqdm(seasons):
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
        if yr == seasons[0]:
            all_stats = pd.DataFrame(columns=headers)

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        team_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

        stats = pd.DataFrame(team_stats, columns = headers)

        # drop na/none values
        stats = stats.dropna(axis='rows')

        # keep only teams that made the tournament
        stats = stats[stats.School.str.contains("NCAA")]

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

    return all_stats

def scrape_opp_stats(seasons):
    for yr in tqdm(seasons):
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
        if yr == seasons[0]:
            all_stats = pd.DataFrame(columns=headers)

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        team_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

        stats = pd.DataFrame(team_stats, columns = headers)

        # drop na/none values
        stats = stats.dropna(axis='rows')

        # keep only teams that made the tournament
        stats = stats[stats.School.str.contains("NCAA")]

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

    all_stats = all_stats.add_suffix('_opp')
    return all_stats

def scrape_tourn_team_stats(year):
    # URL page we will scraping (see image above)
    url = "https://www.sports-reference.com/cbb/seasons/{}-school-stats.html".format(year)
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
    all_stats = pd.DataFrame(columns=headers)

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

    stats = pd.DataFrame(team_stats, columns = headers)

    # drop na/none values
    stats = stats.dropna(axis='rows')

    # keep only teams that made the tournament
    stats = stats[stats.School.str.contains("NCAA")]

    # remove the ncaa suffix
    stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)

    # stats['School'].to_csv(root + 'data/stats.csv')
    # teams.to_csv(root + 'data/MTeams.csv')

    # merged = pd.merge(stats, teams, on='School', how='left')
    # merged[['School','TeamID']].to_csv(root + 'data/merged.csv')


    # add year to the end of each school name
    stats['School'] = stats['School'].astype(str) + '_'  + year

    # append to dataframe
    all_stats = all_stats.append(stats)

    return all_stats

def scrape_tourn_opp_stats(year):
    # URL page we will scraping (see image above)
    url = "https://www.sports-reference.com/cbb/seasons/{}-opponent-stats.html".format(year)
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
    all_stats = pd.DataFrame(columns=headers)

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    team_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

    stats = pd.DataFrame(team_stats, columns = headers)

    # drop na/none values
    stats = stats.dropna(axis='rows')

    # keep only teams that made the tournament
    stats = stats[stats.School.str.contains("NCAA")]

    # remove the ncaa suffix
    stats['School'] = stats['School'].replace(" NCAA$", "", regex=True)

    # stats['School'].to_csv(root + 'data/stats.csv')
    # teams.to_csv(root + 'data/MTeams.csv')

    # merged = pd.merge(stats, teams, on='School', how='left')
    # merged[['School','TeamID']].to_csv(root + 'data/merged.csv')


    # add year to the end of each school name
    stats['School'] = stats['School'].astype(str) + '_'  + year

    # append to dataframe
    all_stats = all_stats.append(stats)

    all_stats = all_stats.add_suffix('_opp')

    return all_stats


def main():
    # calling scrape statements
    print('\nScraping tournament wins from ' + years[0] + ' to ' + years[-1] + '...')
    wins = scrape_wins(years)
    # print(wins)

    print('\nScraping team stats from ' + years[0] + ' to ' + years[-1] + '...')
    team_stats = scrape_team_stats(years)
    # print(team_stats)

    print('\nScraping opponent stats from ' + years[0] + ' to ' + years[-1] + '...')
    opp_stats = scrape_opp_stats(years)
    # print(opp_stats)

    print('\nScraping ' + curr_year + ' tournament team stats...')
    tourn_team_stats = scrape_tourn_team_stats(curr_year)
    # print(tourn_team_stats)

    print('\nScraping ' + curr_year + ' tournament opponent stats...\n')
    tourn_opp_stats = scrape_tourn_opp_stats(curr_year)
    # print(tourn_opp_stats)

    # write to csv
    wins.to_csv(root + 'data/wins_' + years[0] + '_' + years[-1] + '.csv')
    team_stats.to_csv(root + 'data/team_stats_' + years[0] + '_' + years[-1] + '.csv')
    opp_stats.to_csv(root + 'data/opp_stats_' + years[0] + '_' + years[-1] + '.csv')
    tourn_team_stats.to_csv(root + 'data/tourn_stats_' + curr_year + '.csv')
    tourn_opp_stats.to_csv(root + 'data/tourn_opp_stats_' + curr_year + '.csv')

if __name__ == '__main__':
    main()
