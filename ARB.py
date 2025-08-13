import pandas as pd
import getOdds
import copy

df = getOdds.main() #in this file df is the data frame which also has all of the implied probabilities




df['next_home'] = df['home_team'].shift(-1) #these shifted games will be used as a referance to check if we at a new game yet
df['next_away'] = df['away_team'].shift(-1)

#Now we loop through the data frame untill we get a new competition
# Append all the probabilities for one team  in Team one prob
# and which row of the DF it sits in in Team one pos
# same for the other team
# do a two sum style loop and check if any combination provides a probability less then one
# if its less then one, go to the their respective positions inside the pos array to find the index of the row
# then we can calulate the stake for each position using functions from another file 



homeProb = []
awayProb = []
homePos = []
awayPos = []
ValuableRows = [] # this array will contain the arbitrage oppertunites

for i, row in df.iterrows(): # for every row inside the data frame

    if (row['home_team'] != row['next_home']) or (row['away_team'] != row['next_away']):# This is checking if the game changed
        
       
        
        home_prob_min_idx = 0 #this will contain the idx of the min prob in Pos arrays, thus giving the best ROI when betting
        away_prob_min_idx = 0
        
        temp1 = 1 #dummy vars used to calculate the minimum probs
        temp2 = 1
        
        for f in range(len(homeProb)):
            lowest = temp1
            if homeProb[f] < lowest:
                temp1 = homeProb[f]
                home_prob_min_idx = f

        
        for g in range(len(awayProb)):
            lowest = temp2
            if awayProb[g] < lowest:
                temp2 = awayProb[g]
                away_prob_min_idx = g   

       
        if len(homeProb) == 0 or len(awayProb) == 0:
            homeProb.clear(); homePos.clear()
            awayProb.clear(); awayPos.clear()
            continue
        
        if homeProb[home_prob_min_idx] + awayProb[away_prob_min_idx] < 1:
            
            ValuableRows.append(homePos[home_prob_min_idx])
            ValuableRows.append(awayPos[away_prob_min_idx])
        
        home_prob_min_idx = 0 #this will contain the idx of the min prob in Pos arrays
        away_prob_min_idx = 0
        
        
        
        
        #clears the indicators because theyre in Valuable rows now
        homeProb.clear()
        homePos.clear()
        awayProb.clear()
        awayPos.clear()

        
    
    
    elif(row['home_team'] == row['next_home']) and (row['away_team'] == row['next_away']): # If the teams did not change
        
        if row['team'] == row['home_team']: # Wager is on the home team
            homeProb.append(row['Prob']) # homeProb has the value of the implied probability of the bet
            homePos.append(int(i)) #homePos has dataframe index of where this implied probability was found
        
        if row['team'] != row['home_team']: #wager is on the away team
            awayProb.append(row['Prob'])
            awayPos.append(int(i))
            



for row_idx in range(0,len(ValuableRows), 2): # we step by two because when we print we will be printing the groups together
    pair_One = ValuableRows[row_idx] # this is still just an index
    pair_Two = ValuableRows[row_idx + 1] #this is still just an index
    
    # This will print the paired bet you would need to take for the arbitrage oppertunity
    #includes what teams are playing, which book maker you should bet with, and which team to bet on
    print("Home Team: ",df.iloc[pair_One]['home_team'], "  | Away Team: ", df.iloc[pair_One]['away_team'], " | Bookmaker: ", df.iloc[pair_One]['bookmaker'], " | Winner: ", df.iloc[pair_One]['team'], " | Win Probability:", df.iloc[pair_One]['Prob']  )
    print("Home Team: ",df.iloc[pair_Two]['home_team'], "  | Away Team: ", df.iloc[pair_Two]['away_team'], " | Bookmaker: ", df.iloc[pair_Two]['bookmaker'], " | Winner: ", df.iloc[pair_Two]['team'], " | Win Probability:", df.iloc[pair_Two]['Prob']  )
    print("\n")
    
    
    