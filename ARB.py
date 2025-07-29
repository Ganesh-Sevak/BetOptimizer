import pandas as pd
import getOdds

df = getOdds.main() # df is now the super data frame including next_home       next_away      Prob columns

print (df)


#Now we loop through the data frame untill we get a new competition
# Append all the probabilities for one team  in Team one prob
# and which row of the DF it sits in in Team one pos
# same for the other team
# do a two sum style loop and check if any combination provides a probability less then one
# if its less then one, go to the their respective positions inside the pos array to find the index of the row
# then we can calulate the stake for each position using functions from another file 


top = 0 # this indicates the top of the posibilites for a certian game
homeProb = []
awayProb = []
homePos = []
awayPos = []
ValuableRows = []
for i, row in df.iterrows():

    if (row['home_team'] != row['next_home']) or (row['away_team'] != row['next_away']):#check if the teams changed
    # if the teams changed then you  check the arrays  
          
        for x in range(len(homeProb)):
            
            for j in range(len(awayProb)):
                
                if (homeProb[x] + awayProb[j]) < 1: # Arbitrage opperturnity if condition is met
                    ValuableRows.append(homePos[x])
                    ValuableRows.append(awayPos[j])

        

        #clears the indicators because theyre in Valuable rows now
        homeProb.clear()
        homePos.clear()
        awayProb.clear()
        awayPos.clear()

        
    
    
    elif(row['home_team'] == row['next_home']) and (row['away_team'] == row['next_away']): # Teams did not change
        
        if row['team'] == row['home_team']: # Wager is on the home team
            homeProb.append(row['Prob'])
            homePos.append(int(i))
        
        if row['team'] != row['home_team']: #wager is on the away team
            awayProb.append(row['Prob'])
            awayPos.append(int(i))
            
    #add a condition to acount for the last block, as of now, the last game is not being checked





for i in ValuableRows:
    print("hi")
    print(df.iloc[i])