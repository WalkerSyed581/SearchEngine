import nltk

def buildHitlist(word,document_text):

def parseDocument(document_path,lexicon):
    text = ""
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

    for token in tokens:
        hitlist = buildHitlist(token,tokens)
         
    



def buildForward_Index(datapath,lexicon):
    for (root,_,files) in os.walk(datapath):
        for file in files:
            dataOfOneDoc = parseDocument(os.path.abspath(os.path.join(root,file)),lexicon)
            



