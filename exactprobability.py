'''
The probabilities contained in the 2000.pdf file had been determined by extensive polling for Gore 
winning each of the 17 states (denote by p1,...,p17). Instead of p=0.5, each of the 17 Battleground
States is determined by it own Bernoulli random variable - ie. Wisconsin has p=0.946 while Nevada 
has p=0.146. Using these new probabilities and the Monte Carlo method (using 1 million copies to average),
this code simulates to obtain the probability that Bush would win the election, and the probability
that Gore would win the election, and the probability of a tie
'''
# Import the numpy module 
import numpy as np
# Find the probability that Bush would win the election, and the probability that Gore 
# would win the election, and the probability of a tie. Note: this code takes about 40 
# seconds to run 

# Create a function 'Gore' that calculates Gore's total votes to determine the 
# three probabilities listed above. This function will take as input a dictionary of 
# states and their corresponding EC vote count and probabilities of Gore winning 
def Gore(vote_prob, n):
    # Initiate variables that store values of the total times each occurance of a tie, 
    # Bush winning, or Gore winning would happen during Monte Carlo simulations 
    Ttie = 0
    TGore=0
    TBush = 0

    # Create a for loop that iterates through n for the Monte Carlo simulation
    for j in range(1, n+1):
        # Initiate two variables that represent the amount of votes that Gore and Bush 
        # have already (before the election)
        Gore_votes = 146
        Bush_votes = 210  
        
        # Create a for loop that iterates through each key in the dictionary
        for i in vote_prob:  
            # Create a variable "EC" that represents the EC votes of each state in the 
            # dictionary 
            EC = vote_prob[i][0]
            # Generate independent Bernoulli random variables using the numpy module
            # for binomial distribution and the determined probabilities for as many 
            # times as there are states with electoral votes. With each iteration through 
            # this for loop, the probability will change based on the next state in this 
            # dictionary "vote_prob"
            B = np.random.binomial(1, vote_prob[i][1])
            
            # If the probability generated equals 1, this means that it is a success, 
            # indicating that Gore won the EC votes of that state. So, all the votes 
            # corresponding to that state gets added to Gore's vote count. Otherwise, 
            # Bush won the state, so all the votes would go towards his vote count. 
            if B == 1:
                Gore_votes += EC
            else:
                Bush_votes += EC
        
        # Create three if conditions that determines the number of times a tie occurs, 
        # that Gore wins, or that Bush wins. If the total count of votes that Gore and Bush 
        # have are equal, then there is a tie (both would have 269). If Gore's vote count
        # is greater than Bush's, then update the 'TGore' variable by 1 because Gore has 
        # won for this trial. 'TGore' indicates the number of times Gore would win in 
        # 1,000,000 trials, or whatever value n is set to for Monte Carlo simulations. 
        # If Gore's vote count is less than Bush's, this means that Bush won, so the 
        # number of times he wins in 1000000 trials increases by 1. 
        if Gore_votes == Bush_votes:
            Ttie +=1
        if Gore_votes > Bush_votes:
            TGore+=1
        if Gore_votes < Bush_votes:
            TBush+=1
            
    # Calculate the probability of election copies for which the election was a tie by 
    # dividing the total number of times a tie was yielded by the total number of copies n
    Ptie = float(Ttie/n) 
    # With the same concept, calculate the proportion of election copies for which 
    # Gore and Bush won 
    PGore = float(TGore/n)
    PBush = float(TBush/n)
    
    # Return the probabilities
    return {"Probability that Bush wins": PBush, "Probability that Gore wins": PGore, 
            "Probability of tie": Ptie}


# Create a dictionary of with unique keys of the Battleground states and values of lists
# containing the number of EC votes and the probability determined by polling
vote_prob= {"AR":[6,.395], "DE":[3,.143], "FL":[25,.893], "IL":[22,.999], "IA":[7,.420], 
           "ME": [4,.5], "MI":[18, .997], "MN":[10, .999], "MO":[11,.236], "NV":[4, .146], 
           "NH":[4,.731], "OR":[7,.602], "PA":[23,.989], "TN":[11,.289], "WA":[11,.753], 
           "WV":[5,.302], "WI":[11, .946]}

# Call function 
Gore(vote_prob, 1000000)
