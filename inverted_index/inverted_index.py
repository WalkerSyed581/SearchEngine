"""
Inverted Index module creating all the functions related to it
"""
import json

from config import *
from misc_functions import *

#
# Importing the following modules so as to read the forward index
#

import forward_index.forward_index
from forward_index.forward_index import readBarrels

# This functions creates and inverted barrel from the given forward barrel by using the memory trade-off
def createInvertedBarrel(forwardBarrel):
    invertedBarrel = dict()

    for docID,words in forwardBarrel.items():
        for wordID,hitpositions in words.items():
            invertedBarrel[wordID] = dict()
            invertedBarrel[wordID].update({docID : hitpositions})
    
    return invertedBarrel


# This function will read the forward barrels and create the inverted barrels
def buildInvertedIndex():
    invertedBarrels = dict()

    barrelNum = 0
    # Walking through the forward barrels and creating inverted barrels by passing it to the above function
    for (_,_,files) in os.walk(BARREL_PATH):
            for file in files:
                path = os.path.join(BARREL_PATH,file)
                try:
                    invertedBarrels[barrelNum] = readBarrels(path)
                # If no forward barrel index for this barrel number, we ignore that number
                except (FileNotFoundError, IOError):
                    invertedBarrels[barrelNum] = dict()
                    continue
                
                invertedBarrels[barrelNum] = createInvertedBarrel(invertedBarrels[barrelNum])
                barrelNum += 1

    # Passing all the barrels to this functions which writes all of them to memory
    generateInvertedBarrels(invertedBarrels)