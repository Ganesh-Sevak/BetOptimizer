import requests
import pandas as pd
# import warnings
# warnings.filterwarnings("ignore", category=UserWarning)
from dotenv import load_dotenv
import os

API_KEY = "0137f1c0e853984f2682be05eef2b399"
sport = 'upcoming'
region = 'us'  # Options: us, uk, eu, au
market = 'h2h'  # 'h2h' for moneyline bets

# Construct the API URL
url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds'

# Set up query parameters
params = {
    'apiKey': API_KEY,
    'regions': region,
    'markets': market,
    'oddsFormat': 'american'  # Options: 'american', 'decimal'
}

# Make the API request
response = requests.get(url, params=params)

rows = []


# Check for successful response 
if response.status_code == 200:
    odds_data = response.json()
    for game in odds_data:
        home_team = game['home_team']
        away_team = game['away_team']
        commence_time = game['commence_time']
        print(f"{away_team} at {home_team} - {commence_time}")
        for bookmaker in game['bookmakers']:
            print(f"  Bookmaker: {bookmaker['title']}")
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    for outcome in market['outcomes']:
                        print(f"    {outcome['name']}: {outcome['price']}")
                        # Add to rows list here, inside the loop
                        rows.append({
                            "home_team": game['home_team'],
                            "away_team": game['away_team'],
                            "commence_time": game['commence_time'],
                            "bookmaker": bookmaker['title'],
                            "team": outcome['name'],
                            "odds": outcome['price']
                        })
        print()
else:
    print(f"Failed to fetch odds: {response.status_code} - {response.text}")




#this creates the data frame
df = pd.DataFrame(rows)
print("\nDataFrame:")
#print(df)


#this adds the space between the differnt games to make viewing alot easier
df['next_home'] = df['home_team'].shift(-1)
df['next_away'] = df['away_team'].shift(-1) #these 2 lines added to columns to the data frame  

for i, row in df.iterrows():
    if (row['home_team'] != row['next_home']) or (row['away_team'] != row['next_away']):#check if the teams changed, if 
        # they did then it is is a new game
        print()
        print()
        print()
        print()
        print()
        print()
    
    else:
        print(row['home_team'],  row['away_team'],  row['bookmaker'], row['team'], row['odds'] ) #prints what the data is looking like, note that we did not add prints into the dataframe it self
