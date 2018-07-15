'''
Using the 51 Electoral College (EC) numbers that were used in the 2000 USA Presidential Election, estimate
via Monte Carlo simulation (using iid Bernoulli random variables (1/2); e.g., a fair coin flip for each 
state), the number of ways there can be a tie in a presidential election. Repeat for the EC numbers that
were used in the 2004/2008, and in 2012. p = .5
'''
# Import the numpy module 
import numpy as np

# Create a function 'tie' that calculates the number of ways there can be a tie. This 
# function will take as input a list of electoral votes for each state, the number of 
# states, amount of trials for Monte Carlo simulation, and the Bernoulli of 1/2

def tie(EC, states, n, p):
    # Initiate variables to be used later
    total = 0
    T = 0
    
    # Create a for loop that iterates through n for the Monte Carlo simulation
    for j in range(1, n+1):
        # Initiate a variable 'votes' that represents the total number of votes 
        # won based on Bernoulli. This is inside the Monte Carlo for loop because it 
        # will change for each Monte Carlo trial 
        votes = 0
        for i in EC:
            # Generate independent Bernoulli random variables using the numpy extension 
            # for binomial distribution for as many times as there are states with
            # electoral votes (equivalent to the size of the 'EC' list which is 51) 
            B = (np.random.binomial(states, p))/states
            # If B > probability .5, this means that the probability that the candidate 
            # won the state is 1, meaning its a success and the candidate wins all the 
            # votes (i) of that state. Otherwise, the probability is 0, meaning the 
            # candidate lost and the number of votes they win is 0            
            if B > p:
                i  
            else:
                i = 0
            # Add the number of votes from each state to find the total amount won
            votes +=i
        # Create a Bernoulli variable 'total' to indicate the success probability of a tie.
        # If the total vote count is 269, the election is a tie, so the Bernoulli 'total'
        # becomes 1. If not, it indicates a failure, so 'total' becomes 0. This random 
        # variable is generated n times for Monte Carlo simulations
        if votes == 269:
            total = 1
        else:
            total = 0
        # Sum up all the iid copies n times for the 'total' Bernoulli random variables
        T += total
        
    # Create a variable "Ptie" that stores the proportion of the copies out of n that 
    # yield a tie
    Ptie = T/n
    # To find the total number of ties, multiply the probability of getting a tie ('Ptie')
    # with the total number of ways possible (2**51)
    ties = Ptie*(2**51)
    return ties
# Create a list of electoral college votes in 2004, 2008, and 2012            
EC04= [9,3,8,6,54,8,8,3,3,25,13,4,4,22,12,7,6,8,9,4,10,12,18,10,7,11,3,5,4,4,15,5,33,
         14,3,21,8,7,23,4,8,3,11,32,5,3,13,11,5,11,3]
EC08=[9, 3, 10, 6, 55, 9, 7, 3, 3, 27, 15, 4, 4, 21, 11, 7, 6, 8, 9, 4, 10, 12, 17,
      10, 6, 11, 3, 5, 5, 4, 15, 5, 31, 15, 3, 20, 7, 7, 21, 4, 8, 3, 11, 34, 5, 3, 13,
      11, 5, 10, 3]
EC12=[9, 3, 10, 6, 55, 9, 7, 3, 3, 27, 15, 4, 4, 21, 11, 7, 6, 8, 9, 4, 10, 12, 17,
      10, 6, 11, 3, 5, 5, 4, 15, 5, 31, 15, 3, 20, 7, 7, 21, 4, 8, 3, 11, 34, 5, 3, 13,
      11, 5, 10, 3]
print("2004:", tie(EC04, states=51,p=.5, n=1000000))
print("2008:", tie(EC08, states=51,p=.5, n=1000000))
print("2012:", tie(EC12, states=51,p=.5, n=1000000))
