import nltk
import os
import json
from misc_functions import filter_and_tokenize_file
from misc_functions import generateDocIDs
import lexicon.lexicon
from lexicon.lexicon import build_lexicon

def readForwardIndex():
    with open("../Data/forwardIndex.json","r",encoding='utf-8') as forwardIndexFile:
       lexicon = json.load(forwardIndexFile)

    return lexicon

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

def buildForwardIndex(datapath):
    docIndex = generateDocIDs()
    lexicon = build_lexicon()
    try:
        forwardIndex = readForwardIndex()
    except (FileNotFoundError, IOError):
        forwardIndex = dict()\

    for (root,_,files) in os.walk(datapath):
        for file in files:
            docID = str(docIndex[os.path.join(root,file)])
            if forwardIndex.get(docID) == None:
                path = os.path.abspath(os.path.join(root,file))
                forwardIndex[docID] = parseDocument(path,lexicon)

    with open("../Data/forwardIndex.json","w+",encoding='utf-8') as forwardIndexFile:
        json.dump(forwardIndex,forwardIndexFile)

    return forwardIndex

def clearDocs():
    os.remove("../Data/forwardIndex.json")
    os.remove("../Data/invertedIndex.json")
    os.remove("../Data/lexicon.json")
    os.remove("../Data/documentIndex.json")



