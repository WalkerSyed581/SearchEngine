import os
import json

from config import *

from misc_functions import *

def readLexicon():
    lexicon = dict()
    with open(LEXICON_PATH,"r",encoding='utf-8') as lexFile:
        lexicon = json.load(lexFile)
    
    return lexicon



def buildLexicon(docIndex):
    lexiconf = dict()
    filtered_tokens = list()
    try:
        isIndexed = readIsIndexed()
    except (FileNotFoundError, IOError):
        isIndexed = list()

    for (_,_,files) in os.walk(DATA_PATH):
            for file in files:
                path = os.path.join(DATA_PATH,file)
                docID = str(docIndex[path])
                if docID not in isIndexed:
                    filtered_tokens += filter_and_tokenize_file(file)
    
    words = set(filtered_tokens)


    try:
        lexiconf = readLexicon()
    except (FileNotFoundError, IOError):
        lexiconf = dict()


    index = 0
    for word in words:
        if lexiconf.get(word) == None:
            lexiconf[word] = index
        index += 1

    with open(LEXICON_PATH,"w+",encoding='utf-8') as lex:
        json.dump(lexiconf,lex)

    return lexiconf

    
