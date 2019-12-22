"""
This file has all the file paths in order to get this project up and running along with a function which creates those paths 
in the project directory
"""

import os


DIRECTORY_PATH = os.path.abspath("Data")
DATA_PATH = os.path.abspath("Data/sample_data")
BARREL_PATH = os.path.abspath("Data/barrels")
SHORT_BARREL_PATH = os.path.abspath("Data/shortBarrels")
INVERTED_BARREL_PATH = os.path.abspath("Data/invertedBarrels")
SHORT_INVERTED_BARREL_PATH = os.path.abspath("Data/shortInvertedBarrels")
MISC_STUFF = os.path.abspath("Data/miscStuff")
DOC_INDEX_PATH = os.path.abspath("Data/miscStuff/documentIndex.json")
IS_INDEXED_PATH = os.path.abspath("Data/miscStuff/isIndexed.pickle")
LEXICON_PATH = os.path.abspath("Data/lexicon.json")


BARRELS_CAPACITY = 16000


def makePaths():
    try:
        os.stat(DIRECTORY_PATH)
    except:
        os.mkdir(DIRECTORY_PATH)

    try:
        os.stat(DATA_PATH)
    except:
        os.mkdir(DATA_PATH)

    try:
        os.stat(BARREL_PATH)
    except:
        os.mkdir(BARREL_PATH)

    try:
        os.stat(SHORT_BARREL_PATH)
    except:
        os.mkdir(SHORT_BARREL_PATH)

    try:
        os.stat(INVERTED_BARREL_PATH)
    except:
        os.mkdir(INVERTED_BARREL_PATH)

    try:
        os.stat(SHORT_INVERTED_BARREL_PATH)
    except:
        os.mkdir(SHORT_INVERTED_BARREL_PATH)

    try:
        os.stat(MISC_STUFF)
    except:
        os.mkdir(MISC_STUFF)

        

    