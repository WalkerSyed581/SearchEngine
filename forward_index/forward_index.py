"""
This file is the module containing all the functions regarding the forward indexing process
"""

import nltk
import os
import json

from config import *

from misc_functions import *

#
# Importing the buildLexicon to track a few of the changes in case someother documents have been added
# 
import lexicon.lexicon
from lexicon.lexicon import buildLexicon

#
# This functions will read one barrel at the argument path
#
def readBarrels(path):
    barrel = dict()
    with open(path,"r",encoding='utf-8') as forwardBarrel:
        barrel = json.load(forwardBarrel)
    
    return barrel

#
# This functions enumerates over the words and stores all of their positions
#
def buildHitlist(word,document_tokens):

    positions = [i for i, x in enumerate(document_tokens) if x == word]


    return positions

#
# This function will parse the document and create a single entry in the barrel specified through wordID
#
def parseDocument(document_path,lexicon,docID):
    # Reading document
    filtered_tokens = filter_and_tokenize_file(document_path)
    forwardBarrels = dict()

    #
    # This loop will assign all of the wordID in a document to its specific barrel
    #
    for token in filtered_tokens:
        wordID = lexicon[token]
        barrelNumber = int(wordID/BARRELS_CAPACITY)
        positions = buildHitlist(token,filtered_tokens)

        # Following code checks if the specified entries exist in the barrel or not and intializes them
        if forwardBarrels.get(barrelNumber) == None:
            forwardBarrels[barrelNumber] = dict()

        if forwardBarrels[barrelNumber].get(docID) == None:
            forwardBarrels[barrelNumber][docID] =  dict()
        
        #Assigning positions and discarding repetitions of the same wordID
        if forwardBarrels[barrelNumber][docID].get(wordID) == None:
            forwardBarrels[barrelNumber][docID][wordID] = positions
        else:
            continue

    return forwardBarrels

#
# This is the driving function which runs the above functions in order to create the forward index
#
def buildForwardIndex():
    # Retrieving the prerequisites for forward indexing and getting the lexicon and the document index upto date
    docIndex = generateDocIDs()
    lexicon = buildLexicon(docIndex)

    # Reading file which has the information of which document has been indexed
    try:
        isIndexed = readIsIndexed()
    except (FileNotFoundError, IOError):
        isIndexed = list()


    forwardBarrels = dict()

    # Walking through the dataset and created barrels based on its words
    for (_,_,files) in os.walk(DATA_PATH):
        for file in files:
            path = os.path.join(DATA_PATH,file)
            docID = str(docIndex[path])
            # Checking if the document has already been indexed or not
            if docID in isIndexed:
                continue
            
            forwardBarrels = parseDocument(path,lexicon,docID)
            isIndexed.append(docID)

    # Storing the updated isIndexed file by passing in the list of documents that have been indexed
    generateIsIndexed(isIndexed)

    # Parsing the dictionary of barrels into their specified files by using this function
    generateBarrels(forwardBarrels)

    





