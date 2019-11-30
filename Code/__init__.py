import lexicon.lexicon
from lexicon.lexicon import build_lexicon
from lexicon.lexicon import read_lexicon
import forward_index.forward_index
from forward_index.forward_index import buildForwardIndex
import inverted_index.inverted_index
from inverted_index.inverted_index import buildInvertedIndex

if __name__ == "__main__":
    lexicon = build_lexicon()
    buildForwardIndex('../Data/sample_data')
    buildInvertedIndex()