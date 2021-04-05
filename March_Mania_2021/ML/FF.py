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
