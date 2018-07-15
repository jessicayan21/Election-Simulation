"""
Use recursion to determine the exact number of ties by finding the number of subsets
in which the sum equals the number of votes needed for a tie - 
"""

# Create a function that calculates the number of votes needed for a tie. The value 
# returned will be used as an input for the "recursion" function 
def tie_votes(votes):
    # Initialize variables to be used later 
    total = 0
    I = 0
    # Use a for loop that iterates through every value in the parameter 'votes' and 
    # add up the values and divide the sum by 2 to get the tie. 
    for i in votes:
        total += i
        I = total/2
    return I

# Create a recursive function that takes in the number of EC votes, the number of states,
# and the total number of votes needed for a tie. 
# The code below is explained in details in the paragraph above. 

def recursion(votes, states, tie):
    if states >= len(votes):    
        # If the sum of the subset equals 0, this means that there there is an empty 
        # subset consisting of no elements. This indicates that the number of votes matches 
        # the tie, so return 1, meaning that a subset with a sum of 'tie' has been found. 
        # Otherwise return 0. This value gets stored into 'tie_count' which continues to 
        # update itself everytime a subset has been found 
        if tie == 0:
            return 1
        else:
            return 0
    # The inputs in the first function call now get separated into two cases. The 
    # functions called inside itself will be implemented for an increasing number of states
    # that finds the number of ways there will be a tie with the last state in the 'votes'
    # list and the number of ways there will be a tie without the last state. 
    # If the 'votes' list only contains a state with 0 EC votes, this code must account 
    # for it to make sure that it does not get recursively run through twice. If it goes 
    # through the second recursive call in which the last states' votes are subtracted from 
    # the number of votes needed for a tie, it would still remain as 0, meaning it 
    # would count more subsets than there actually are. So, use an if-statement to make 
    # sure that votes does not equal [0] for the recursive equation to be used. 
    if votes != [0]:
        tie_count = recursion(votes, states + 1, tie)
        tie_count += recursion(votes, states + 1, tie - votes[states])
    else:
        tie_count = recursion(votes, states + 1, tie)
    return tie_count

# Create a list that contains an arbitrary number of votes of 6 states 
votes = [3, 4, 4, 5, 6, 8]

# Call the 'tie' function to get the number of votes needed to for a tie and 
# store this number into the variable "I"
I = tie_votes(votes)

# Call the 'recursion' function 
print("Number of ways to get a tie: ", recursion(votes, 0, I))
