import os
import json
from misc_functions import filter_and_tokenize_file


def read_lexicon():
    with open("../Data/lexicon.json","r",encoding='utf-8') as lexFile:
       lexicon = json.loads(lexFile.read())

    return lexicon



def build_lexicon():
    filtered_tokens = list()
    for (root,_,files) in os.walk('../Data/sample_data'):
        for file in files:
            path = os.path.abspath(os.path.join(root,file))
            filtered_tokens += filter_and_tokenize_file(path)

    words = set(filtered_tokens)

    lexiconf = dict()
    lexiconb = dict()
    index = 0

    for word in words:
        lexiconf[word] = index
        lexiconb[str(index)] = word
        index += 1

    with open("../Data/lexicon.json","w+",encoding='utf-8') as lex:
        json.dump(lexiconf,lex)



    
