import json

from config import *
from misc_functions import *

import lexicon.lexicon
from lexicon.lexicon import readLexicon

import forward_index.forward_index
from forward_index.forward_index import readBarrels

def createInvertedBarrel(forwardBarrel):
    invertedBarrel = dict()

    for docID,words in forwardBarrel.items():
        for wordID,hitpositions in words.items():
            invertedBarrel[wordID] = dict()
            invertedBarrel[wordID].update({docID : hitpositions})
    
    return invertedBarrel


def buildInvertedIndex():
    invertedBarrels = dict()

    barrelNum = 0
    for (_,_,files) in os.walk(BARREL_PATH):
            for file in files:
                path = os.path.join(BARREL_PATH,file)
                try:
                    invertedBarrels[barrelNum] = readBarrels(path)
                except (FileNotFoundError, IOError):
                    invertedBarrels[barrelNum] = dict()
                
                invertedBarrels[barrelNum] = createInvertedBarrel(invertedBarrels[barrelNum] )
                barrelNum += 1

    generateInvertedBarrels(invertedBarrels)