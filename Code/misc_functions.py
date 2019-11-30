import json
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

def filter_and_tokenize_file(path):
    text = ""
    with open(path,"r",encoding='utf8') as f:
        data = json.loads(f.read())
        text += " " + data["text"]

    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()

    
    tokens = nltk.regexp_tokenize(text,r'\w+')


    filtered_tokens = [ps.stem(lemmatizer.lemmatize(token.lower())) for token in tokens if not(len(token) <= 1) and not(token.isdigit())]

    return filtered_tokens