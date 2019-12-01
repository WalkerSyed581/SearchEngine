import json
import nltk
import os

import pickle

from config import *

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def filter_and_tokenize_file(file):
    text = ""
    path = os.path.join(DATA_PATH,file)
    with open(path,"r",encoding='utf8') as f:
        data = json.loads(f.read())
        text += " " + data["text"]

    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()

    
    tokens = nltk.regexp_tokenize(text,r'\w+')


    filtered_tokens = [ps.stem(lemmatizer.lemmatize(token.lower())) for token in tokens if not(len(token) <= 1) and not(token.isdigit())]

    return filtered_tokens

def generateDocIDs():
    try:
        docIndex = readDocIDs()
    except (FileNotFoundError, IOError):
        docIndex = dict()

    for (_,_,files) in os.walk(DATA_PATH):
        for file in files:
            path = os.path.join(DATA_PATH,file)
            if docIndex.get(path) == None:
                docIndex[path] = str(len(docIndex))


    with open(DOC_INDEX_PATH,"w+",encoding='utf-8') as documentIndexFile:
        json.dump(docIndex,documentIndexFile)   

    return docIndex          

def readDocIDs():
    with open(DOC_INDEX_PATH,"r",encoding='utf-8') as documentIndexFile:
        docIndex = json.load(documentIndexFile)

    return docIndex

def generateBarrels(immediateBarrels):
    for key,value in immediateBarrels.items():
        forwardBarrel = dict()
        try:
            with open(os.path.join(BARREL_PATH,"barrel{}.json".format(key)) ,"r",encoding='utf-8') as forwardBarrelFile:
                forwardBarrel = json.load(forwardBarrelFile)
        except (FileNotFoundError, IOError):
            pass
        
        forwardBarrel.update(value)
        with open(os.path.join(BARREL_PATH,"barrel{}.json".format(key)) ,"w+",encoding='utf-8') as forwardBarrelFile:
            forwardBarrel = json.dump(forwardBarrel,forwardBarrelFile)


def generateIsIndexed(indexedDocs):
    try:
        indexedDocs.append(readIsIndexed())
    except (FileNotFoundError, IOError):
        pass

    
    with open(IS_INDEXED_PATH,"wb+") as isIndexedFile:
        pickle.dump(indexedDocs,isIndexedFile)     
          

def readIsIndexed():
    with open(IS_INDEXED_PATH,"rb") as isIndexedFile:
        isIndexed = pickle.load(isIndexedFile)
    return isIndexed
        

def generateInvertedBarrels(immediateInvertedBarrels):
    for key,value in immediateInvertedBarrels.items():
        invertedBarrel = dict()
        
        invertedBarrel.update(value)
        with open(os.path.join(INVERTED_BARREL_PATH,"barrel{}Inverted.json".format(key)) ,"w+",encoding='utf-8') as invertedBarrelFile:
            json.dump(invertedBarrel,invertedBarrelFile)
