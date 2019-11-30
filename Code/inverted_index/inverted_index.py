import json

import lexicon.lexicon
from lexicon.lexicon import read_lexicon

import forward_index.forward_index
from forward_index.forward_index import readForwardIndex

def numberOfDocuments(wordID,forwardIndex):
    positions = list()

    for key,value in forwardIndex.items():
        if value.get(wordID) != None:
            positions.append(key)

    return positions


def buildInvertedIndex():
    invertedIndex = dict()

    lexicon = read_lexicon()
    forwardIndex = readForwardIndex()

    for key in lexicon:
        invertedIndex[str(lexicon[key])] = numberOfDocuments(str(lexicon[key]),forwardIndex)

    with open("../Data/invertedIndex.json","w+",encoding='utf-8') as invertedIndexFile:
        json.dump(invertedIndex,invertedIndexFile)