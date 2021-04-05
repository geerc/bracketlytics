import pandas as pd

root = '/Users/christiangeer/bracketlytics/March_Mania_2021/'

def four_factor(data, opp_data):
    data = data.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
    opp_data = opp_data.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])

    # Create DRB
    data['DRB'] = data['TRB'] - data['ORB']
    opp_data['DRB'] = opp_data['TRB'] - opp_data['ORB']

    # EFG%
    data['oEFG'] = ((data['FG'] + (0.5 * data['3P'])) / data['FGA']).round(3)
    data['dEFG'] = ((opp_data['FG'] + (0.5 * opp_data['3P'])) / opp_data['FGA']).round(3)

    # Turnovers
    data['oTOV'] = (data['TOV'] / ((data['TOV']) + (0.44 + data['FTA']) + data['TOV'])).round(3)
    data['dTOV'] = (opp_data['TOV'] / ((opp_data['TOV']) + (0.44 + opp_data['FTA']) + opp_data['TOV'])).round(3)

    # Rebounding
    data['oREB'] = (data['ORB'] / (data['ORB'] + opp_data['DRB'])).round(3)
    data['dREB'] = (data['DRB'] / (opp_data['ORB'] + data['DRB'])).round(3)

    # Free Throws
    data['oFT'] = (data['FT'] / data['FGA']).round(3)
    data['dFT'] = (opp_data['FT'] / opp_data['FGA']).round(3)

    # remove old columns
    data = data.drop(data.iloc[:,3:13], axis=1)

    return data

# opp_stats = pd.read_csv(root + 'data/opp_stats_2010_2020.csv')
# team_stats = pd.read_csv(root + 'data/team_stats_2010_2020.csv')
# tourn_stats = pd.read_csv(root + 'data/tourn_stats_2021.csv')
# tourn_opp_stats = pd.read_csv(root + 'data/tourn_opp_stats_2021.csv')
#
# opp_stats = opp_stats.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
# team_stats = team_stats.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
# tourn_stats = tourn_stats.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
# tourn_opp_stats = tourn_opp_stats.drop(columns=['G','W','L','W-L%','\xa0','W.1','L.1','\xa0.1','W.2','L.2','\xa0.2','W.3','L.3','\xa0.3','Tm.','Opp.','\xa0.4','MP','FG%','3P%','FT%','AST','STL','BLK','PF'])
#
# # Create DRB
# team_stats['DRB'] = team_stats['TRB'] - team_stats['ORB']
# opp_stats['DRB'] = opp_stats['TRB'] - opp_stats['ORB']
# tourn_stats['DRB'] = tourn_stats['TRB'] - tourn_stats['ORB']
# tourn_opp_stats['DRB'] = tourn_opp_stats['TRB'] - tourn_opp_stats['ORB']
#
# # EFG%
# team_stats['oEFG'] = ((team_stats['FG'] + (0.5 * team_stats['3P'])) / team_stats['FGA']).round(3)
# team_stats['dEFG'] = ((opp_stats['FG'] + (0.5 * opp_stats['3P'])) / opp_stats['FGA']).round(3)
#
# tourn_stats['oEFG'] = ((tourn_stats['FG'] + (0.5 * tourn_stats['3P'])) / tourn_stats['FGA']).round(3)
# tourn_stats['dEFG'] = ((tourn_opp_stats['FG'] + (0.5 * tourn_opp_stats['3P'])) / tourn_opp_stats['FGA']).round(3)
#
# # Turnovers
# team_stats['oTOV'] = (team_stats['TOV'] / ((team_stats['TOV']) + (0.44 + team_stats['FTA']) + team_stats['TOV'])).round(3)
# team_stats['dTOV'] = (opp_stats['TOV'] / ((opp_stats['TOV']) + (0.44 + opp_stats['FTA']) + opp_stats['TOV'])).round(3)
#
# tourn_stats['oTOV'] = (tourn_stats['TOV'] / ((tourn_stats['TOV']) + (0.44 + tourn_stats['FTA']) + tourn_stats['TOV'])).round(3)
# tourn_stats['dTOV'] = (tourn_opp_stats['TOV'] / ((tourn_opp_stats['TOV']) + (0.44 + tourn_opp_stats['FTA']) + tourn_opp_stats['TOV'])).round(3)
#
# # Rebounding
# team_stats['oREB'] = (team_stats['ORB'] / (team_stats['ORB'] + opp_stats['DRB'])).round(3)
# team_stats['dREB'] = (team_stats['DRB'] / (opp_stats['ORB'] + team_stats['DRB'])).round(3)
#
# tourn_stats['oREB'] = (tourn_stats['ORB'] / (tourn_stats['ORB'] + tourn_opp_stats['DRB'])).round(3)
# tourn_stats['dREB'] = (tourn_stats['DRB'] / (tourn_opp_stats['ORB'] + tourn_stats['DRB'])).round(3)
#
# # Free Throws
# team_stats['oFT'] = (team_stats['FT'] / team_stats['FGA']).round(3)
# team_stats['dFT'] = (opp_stats['FT'] / opp_stats['FGA']).round(3)
#
# tourn_stats['oFT'] = (tourn_stats['FT'] / tourn_stats['FGA']).round(3)
# tourn_stats['dFT'] = (tourn_opp_stats['FT'] / tourn_opp_stats['FGA']).round(3)
#
# # remove old columns
# team_stats = team_stats.drop(team_stats.iloc[:,3:13], axis=1)
# tourn_stats = tourn_stats.drop(tourn_stats.iloc[:,3:13], axis=1)
