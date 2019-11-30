import nltk
import os
import json
from misc_functions import filter_and_tokenize_file

def buildHitlist(word,document_tokens):

    positions = [i for i, x in enumerate(document_tokens) if x == word]
    count = len(positions)

    hitlist = {"positions": positions,"count" : count}

    return hitlist

def parseDocument(document_path,lexicon):
    document_hits = dict()
    filtered_tokens = filter_and_tokenize_file(document_path)

    for token in filtered_tokens:
        wordID = lexicon[token]
        hitlist = buildHitlist(token,filtered_tokens)
        document_hits[wordID] =  hitlist 

    return document_hits

def buildForwardIndex(datapath,lexicon):
    docID = 0
    forwardIndex = dict()
    for (root,_,files) in os.walk(datapath):
        for file in files:
            forwardIndex[str(docID)] = parseDocument(os.path.abspath(os.path.join(root,file)),lexicon)
            docID += 1

    with open("../Data/forwardIndex.json","w+",encoding='utf-8') as forwardIndexFile:
        json.dump(forwardIndex,forwardIndexFile)



