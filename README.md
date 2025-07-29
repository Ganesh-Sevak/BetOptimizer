# BetOptimizer

We will implement 2 types of betting:

1. Arbitrage
2. Postive Expected Value

We have all the implied Probabilities all inside of a data frame, check  impliedProb.py to see the math formula. Now we have a good data frame with more data like
the probabilites. Next we will loop over the df to find arb oppertunities,

Work flow ARB->getOdds->impliedProb->getOdds->ARB