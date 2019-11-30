import lexicon.lexicon
from lexicon.lexicon import build_lexicon
from lexicon.lexicon import read_lexicon
import forward_index.forward_index
from forward_index.forward_index import buildForwardIndex

if __name__ == "__main__":
    myLexicon = read_lexicon()
    buildForwardIndex("../Data/sample_data",myLexicon)