import sys
from wys_parser import *

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('usage: %s filename parsename' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = token_lex(characters)
    parser = globals()[sys.argv[2]]()
    result = parser(tokens, 0)
    print result
