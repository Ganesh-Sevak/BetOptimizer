#This file will contain the helper functions for figuring out the potential payout
#Given specific ofss, whether they be positive or negetive


#We will also write a function to find the highest bet on opposite sides



def PosOdds(p):
    
    return float((p)/(p + 100)) #fix this later to return the correct probability at a decimal




def NegOdds(n):
    n = abs(n) #this turns it into a positive number which eseentially  allows us to use the same formula as positive
    
    return float((n)/ (n + 100)) #fix this later to return the correct probability as a decimal






