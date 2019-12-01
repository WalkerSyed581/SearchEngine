"""
    This will be the starting point of the entire code where the functions to be 
    run will be typed in so that the forward and backward index are created
"""

#Importing modules which contain the functions for creating the forward and backward barrels or indices
import forward_index.forward_index as forward_index

import inverted_index.inverted_index as inverted_index

# Importing the gneralized fucntions and constatns
from config import *


if __name__ == "__main__":
    #If there are no path for the data built then uncomment following line of code
    #makePaths()
    forward_index.buildForwardIndex()
    inverted_index.buildInvertedIndex()
