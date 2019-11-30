import json
import os
import nltk

def build_lexicon():
    text = ""
    for (root,_,files) in os.walk('../Data/sample_data'):
        for file in files:
            path = os.path.abspath(os.path.join(root,file))
            with open(path,"r",encoding='utf8') as f:
                data = json.loads(f.read())
                text += " " + data["text"]
    
    tokens = nltk.regexp_tokenize(text,r'\w+')
    tagged = nltk.pos_tag(tokens)

    for i in range(0,len(tokens) - 1):
        if(tagged[i][1] == "IN"):
            tokens.remove(tagged[i][0])

    for token in tokens:
        token.lower()
        if len(token) == 1 or token.isdigit():
            tokens.remove(token)   

    words = set(tokens)
    

    lexiconf = dict()
    lexiconb = dict()
    index = 0

    for word in words:
        lexiconf[word] = index
        lexiconb[str(index)] = word
        index += 1


    print(lexiconf)
    print(lexiconb)


