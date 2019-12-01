import nltk
import os
import json

from config import *

from misc_functions import *

import lexicon.lexicon
from lexicon.lexicon import buildLexicon

def readBarrels(path):
    barrel = dict()
    with open(path,"r",encoding='utf-8') as invertedBarrel:
        barrel = json.load(invertedBarrel)
    
    return barrel

def buildHitlist(word,document_tokens):

    positions = [i for i, x in enumerate(document_tokens) if x == word]


    return positions

def parseDocument(document_path,lexicon,docID):
    filtered_tokens = filter_and_tokenize_file(document_path)
    forwardBarrels = dict()

    for token in filtered_tokens:
        wordID = lexicon[token]
        barrelNumber = int(wordID/BARRELS_CAPACITY)
        positions = buildHitlist(token,filtered_tokens)

        if forwardBarrels.get(barrelNumber) == None:
            forwardBarrels[barrelNumber] = dict()

        if forwardBarrels[barrelNumber].get(docID) == None:
            forwardBarrels[barrelNumber][docID] =  dict()
        
        if forwardBarrels[barrelNumber][docID].get(wordID) == None:
            forwardBarrels[barrelNumber][docID][wordID] = positions
        else:
            continue

    return forwardBarrels

def buildForwardIndex():
    docIndex = generateDocIDs()
    lexicon = buildLexicon(docIndex)
    try:
        isIndexed = readIsIndexed()
    except (FileNotFoundError, IOError):
        isIndexed = list()

    forwardBarrels = dict()

    for (_,_,files) in os.walk(DATA_PATH):
        for file in files:
            path = os.path.join(DATA_PATH,file)
            docID = str(docIndex[path])
            if docID in isIndexed:
                continue
            
            forwardBarrels = parseDocument(path,lexicon,docID)
            isIndexed.append(docID)

    generateIsIndexed(isIndexed)
    generateBarrels(forwardBarrels)

    





