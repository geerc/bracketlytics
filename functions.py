import pandas

def create_stats(df):
    # Create four factors statistics
    # Create effective field goal percentage for offense and defense
    df['eFG%'] = (df['FG'] + float(0.5) * df['3P']) / df['FGA']
    df['Opp eFG%'] = (df['Opp FG'] + 0.5 * df['Opp 3P']) / df['Opp FGA']
    df[['eFG%', 'Opp eFG%']] = df[['eFG%', 'Opp eFG%']].round(3)

    # Create offensive and defensive turnover percentage
    df['TOVp'] = df['TOV'] / (df['FGA'] + 0.44 + df['FTA'] + df['TOV'])
    df['Opp TOVp'] = df['Opp TOV'] / (df['Opp FGA'] + 0.44 + df['Opp FTA'] + df['Opp TOV'])
    df[['TOVp', 'Opp TOVp']] = df[['TOVp', 'Opp TOVp']].round(3)

    # Create offensive and defensive rebounding percentage
    df['ORBp'] = df['ORB'] / (df['ORB'] + df['Opp DRB'])
    df['DRBp'] = df['DRB'] / (df['DRB'] + df['Opp DRB'])
    df[['ORBp', 'DRBp']] = df[['ORBp', 'DRBp']].round(3)

    # Create offensive and defensive free throw percentage
    df['FTp'] = df['FT'] / df['FGA']
    df['Opp FTp'] = df['Opp FT'] / df['Opp FGA']
    df[['FTp', 'Opp FTp']] = df[['FTp', 'Opp FTp']].round(3)

def create_bracket():
    round1 = Stack()
# South Region
    try:
        round1.push(season_stats.loc['virginia'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['maryland-baltimore-county'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['creighton'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['kansas-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['kentucky'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['davidson'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['arizona'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['buffalo'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['miami-fl'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['loyola-il'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['tennessee'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['wright-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['nevada'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['texas'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['cincinnati'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['georgia-state'])
    except KeyError:
        round1.push(1)
# West Region
    try:
        round1.push(season_stats.loc['xavier'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['texas-southern'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['missouri'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['florida-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['ohio-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['south-dakota-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['gonzaga'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['north-carolina-greensboro'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['houston'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['san-diego-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['michigan'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['montana'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['texas-am'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['providence'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['north-carolina'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['lipscomb'])
    except KeyError:
        round1.push(1)
# East region
    try:
        round1.push(season_stats.loc['villanova'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['radford'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['virginia-tech'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['alabama'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['west-virginia'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['murray-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['wichita-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['marshall'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['florida'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['st-bonaventure'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['texas-tech'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['sf-austin'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['arkansas'])
    except KeyError:
        round1  .push(1)
    try:
        round1.push(season_stats.loc['butler'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['purdue'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['cal-state-fullerton'])
    except KeyError:
        round1.push(1)
# Midwest region
    try:
        round1.push(season_stats.loc['kansas'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['pennsylvania'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['seton-hall'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['north-carolina-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['clemson'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['new-mexico-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['auburn'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['charleston'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['texas-christian'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['syracuse'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['michigan-state'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['bucknell'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['rhode-island'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['oklahma'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['duke'])
    except KeyError:
        round1.push(1)
    try:
        round1.push(season_stats.loc['iona'])
    except KeyError:
        round1.push(1)
