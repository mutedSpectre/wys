import sys
from lex_tokens import *

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = token_lex(characters)
    for token in tokens:
        print token