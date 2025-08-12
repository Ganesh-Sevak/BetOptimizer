import requests
import pandas as pd
from dotenv import load_dotenv
import os
import impliedProb


def main():

    API_KEY = "0137f1c0e853984f2682be05eef2b399"
    sport = 'upcoming'
    region = 'us'  # Options: us, uk, eu, au
    market = 'h2h'  # 'h2h' for moneyline bets

    # Construct the API URL
    url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds' #Dont bother stealing, its a free API key from Odds API

    # Set up query parameters
    params = {
        'apiKey': API_KEY,
        'regions': region,
        'markets': market,
        'oddsFormat': 'american'  # Options: 'american', 'decimal'
    }

    # Make the API request
    response = requests.get(url, params=params) #makes the API call

    rows = []


    # Check for successful response 
    if response.status_code == 200:
        odds_data = response.json()
        for game in odds_data:
            home_team = game['home_team']
            away_team = game['away_team']
            commence_time = game['commence_time']
 
            for bookmaker in game['bookmakers']:

                for market in bookmaker['markets']:
                    if market['key'] == 'h2h':
                        for outcome in market['outcomes']:
        
                            rows.append({ # puts all the data into one big array to eventually turn into a data frame
                                "home_team": game['home_team'],
                                "away_team": game['away_team'],
                                "commence_time": game['commence_time'],
                                "bookmaker": bookmaker['title'],
                                "team": outcome['name'],
                                "odds": outcome['price']
                            })
    else:
        print(f"Failed to fetch odds: {response.status_code} - {response.text}")





    df = pd.DataFrame(rows) #creates the data frame from the rows array

    



    #this adds the space between the differnt games to make viewing alot easier (This was used in development to test fuctionality)
    df['next_home'] = df['home_team'].shift(-1)
    df['next_away'] = df['away_team'].shift(-1) #these 2 lines added to columns to the data frame 

    df['Prob'] = 0.00 #temporarily fill the Prob column with the 0.0 to ensure its a float

    for i, row in df.iterrows():
        if (row['home_team'] != row['next_home']) or (row['away_team'] != row['next_away']):#check if the teams changed,
            
            
            if row['odds']>0: #checks if the odds are postive

                df.at[i,'Prob'] = impliedProb.PosOdds(row['odds']) #makes a call to the function to calculate the implied probability

            else: #checks if the odds are negetive

                df.at[i,'Prob'] = impliedProb.NegOdds(row['odds']) #makes a call to the function to calculate the implied probability
            
            #print()#these prints are for debugging/ visual aid 
            #print()#these prints are for debugging/ visual aid 
            #print()#these prints are for debugging/ visual aid 
            #print()#these prints are for debugging/ visual aid 
            #print()#these prints are for debugging/ visual aid 
            #print()#these prints are for debugging/ visual aid 
        
        else: #if the same teams are playing
            
            if row['odds']>0:

                df.at[i,'Prob'] = impliedProb.PosOdds(row['odds']) # the probabilities will be listed as decimals

            else:

                df.at[i,'Prob'] = impliedProb.NegOdds(row['odds'])
            
            
    return df #This data frame has  next_home       next_away      Prob
