import requests
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
        print()
else:
    print(f"Failed to fetch odds: {response.status_code} - {response.text}")





    print ("nogger")
    
    
