# Arbitrage Bettor

We will implement 2 types of betting:

1. Arbitrage
2. Postive Expected Value (Coming Soon!!)

# Overview
This project pulls moneyline odds from an odds service, converts each price to an implied probability, and searches for cross book pairs where the sum of the two implied probabilities is below one. Such cases indicate a possible risk free arbitrage.

# What is in the repo
getOdds.py fetches data from the service and builds a pandas DataFrame with teams, bookmaker, and odds, then adds helper columns.

impliedProb.py contains small helpers that convert American odds to implied probability.

ARB.py scans the table game by game and prints any pairs that satisfy the arbitrage check.

# Setup
1. Use Python 3.

2. Install required packages
    2.1 requests
    2.2 pandas
    2.3 dotenv (If you purchase a paid API key from Odds.com make sure to use this, this project uses a FREE API key from Odds.com)
   

# Warning

THIS IS NOT FINANCIAL ADVICE
Use at your own discretion. It is possible to be banned from various sports books for Arbitrage betting. Furthermore, do your own due dilligence when sports betting. The creators / contributors of this repo are not responsible for any financial loss that may occur. (This was made for educational purposes only)
