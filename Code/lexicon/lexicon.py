import os
import json
from misc_functions import filter_and_tokenize_file


def read_lexicon():
    with open("../Data/lexicon.json","r",encoding='utf-8') as lexFile:
       lexicon = json.load(lexFile)

    return lexicon



def build_lexicon():
    lexiconf = dict()
    filtered_tokens = list()

    for (root,_,files) in os.walk('../Data/sample_data'):
            for file in files:
                path = os.path.abspath(os.path.join(root,file))
                filtered_tokens += filter_and_tokenize_file(path)
    
    words = set(filtered_tokens)


    try:
        lexiconf = read_lexicon()
    except (FileNotFoundError, IOError):
        lexiconf = dict()



    for word in words:
        if lexiconf.get(word) == None:
            lexiconf[word] = len(lexiconf)

    with open("../Data/lexicon.json","w+",encoding='utf-8') as lex:
        json.dump(lexiconf,lex)

    return lexiconf

    
