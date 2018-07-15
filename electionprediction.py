'''
Assuming that each Battleground State (17 states with uncertain outcomes during 2000 election) outcome is 
determined by an iid fair coin toss (Bernoulli random variable = 0.5), this code simulates using Monte Carlo 
(using 1 million copies to average) to obtain the probability that Bush would win the election, and the 
probability that Gore would win the election, and the probability of a tie. See 2000.pdf for electoral college 
(EC) numbers of each Battleground States.
'''

# Find the probability that Bush would win the election, and the probability that Gore 
# would win the election, and the probability of a tie. Note: this code takes about 40 
# seconds to run 

# Create a function 'Gore' that calculates Gore's total votes to determine the 
# three probabilities listed above. This function will take as input the number of states, 
# amount of trials for Monte Carlo simulation, and the Bernoulli of 1/2
def Gore(states, n, p):
    # Initiate variables to be used later
    tie = 0
    Ttie = 0
    Gore=0
    TGore=0
    Bush = 0
    TBush = 0
    # Create a list of all the electoral votes of the 17 Battleground states 
    EC_B= [6, 3, 25, 22, 7, 4, 18, 10, 11, 4, 4, 7, 23, 11, 11, 5, 11] 
    
    # Create a for loop that iterates through n for the Monte Carlo simulation
    for j in range(1, n+1):
        # Initiate a variable 'votes' that represents the total number of votes 
        # won based on Bernoulli. This is inside the Monte Carlo for loop because it 
        # will change for each Monte Carlo trial 
        votes = 0
        Gore_votes = 0
        
        #Create a for loop that iterated through each of the EC votes in the "EC_B" list
        for i in EC_B:
            # Generate independent Bernoulli random variables using the numpy extension 
            # for binomial distribution for as many times as there are states with
            #electoral votes (equivalent to the size of the 'EC_B' list which is 17) 
            B = (np.random.binomial(states, p)/states)
            # If B > probability .5, this means that the probability that Gore won the 
            # state is 1, meaning he wins all the votes (i) of that state. Otherwise,
            # the probability is 0, meaning he lost and wins 0 votes
            if B <= p:
                i =0 
           
            # Add the number of votes from each state to find the total amount won
            votes +=i
            # Gore's final vote count includes the 146 already won from the states already 
            # counted for (not the Battleground states)
        Gore_votes = 146 + votes 
       
        # Create a Bernoulli variable 'tie' to indicate the success probability of a tie.
        # If Gore's total vote count is 269, the election is a tie, so the Bernoulli 'tie'
        # becomes 1. If not, it indicates a failure, so 'tie' becomes 0. This random 
        # variable (along with the following two) is generated n times for Monte Carlo 
        # simulations
        if Gore_votes == 269:
            tie = 1
        else:
            tie = 0
        # Using the same concept, create a Bernoulli variable 'Gore' to indicate the 
        # success probability of Gore winning the state's votes. If Gore's total vote 
        # count is greater than or equal to 270, he wins the state, so the Bernoulli 
        #'Gore' becomes 1. If not, it indicates a failure, so 'Gore' becomes 0.    
        if Gore_votes >= 270:
            Gore = 1
        else:
            Gore = 0
        # If Gore's total vote count is less than or equal to 268, this means that Bush 
        # would win the state. Using the same concept, create a Bernoulli variable 'Bush' 
        # to indicate the success probability of Bush winning the state's votes. If he
        # wins the state, the Bernoulli 'Bush' becomes 1. Otherwise, it indicates a 
        # failure, so 'Bush' becomes 0.    
        if Gore_votes <= 268:
            Bush = 1
        else:
            Bush = 0
        # Sum up all the iid copies n times for the tie, Gore, and Bush Bernoullis
        Ttie += tie
        TGore += Gore
        TBush += Bush 
    # Calculate the probability of election copies for which the election was a tie by 
    # dividing the total number of times a tie was yielded by the total number of copies n
    Ptie = Ttie/n  
    # With the same concept, calculate the proportion of election copies for which 
    # Gore and Bush won 
    PGore = TGore/n
    PBush = TBush/n
    # Return the probabilities 
    return {"Probability that Bush wins": PBush, "Probability that Gore wins": PGore, 
            "Probability of tie": Ptie}
            
# Call function 
Gore(states=17,p=.5, n=1000000)
